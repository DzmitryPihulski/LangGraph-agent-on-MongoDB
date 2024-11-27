import uuid
from typing import Any, Dict, List, Optional

import gensim.downloader as api  # type: ignore
import numpy as np
from chromadb import Client
from chromadb.config import Settings

from vector_store.few_shots import MONGO_SHOTS, Shot


class VectorStore:
    """
    A vector store implementation using ChromaDB
    and word embeddings for document storage and retrieval.

    This class provides functionality to:
    - Initialize and manage a ChromaDB collection
    - Generate embeddings for documents using word vectors
    - Store and retrieve documents based on semantic similarity

    Attributes:
        collection_name (str): Name of the ChromaDB collection
        embedding_dim (int): Dimension of the word embeddings
        use_gpu (bool): Flag to indicate whether to use GPU acceleration
    """

    def __init__(
        self,
        collection_name: str = "default_collection",
        embedding_dim: int = 300,
        use_gpu: bool = False,
        is_persistent: Optional[bool] = False,
    ) -> None:
        """
        Initialize the VectorStore with ChromaDB and word embeddings model.

        Args:
            collection_name: Name of the ChromaDB collection
            embedding_dim: Dimension of the word embeddings
            use_gpu: Whether to use GPU acceleration for embeddings
            is_persistent: Defines whether Chroma should persist data or not.

        Raises:
            RuntimeError: If ChromaDB initialization fails
            ValueError: If invalid parameters are provided
        """
        self.collection_name = collection_name
        self.embedding_dim = embedding_dim
        self.use_gpu = use_gpu

        # Initialize ChromaDB
        settings = Settings(is_persistent=is_persistent, anonymized_telemetry=False)
        self.chroma_client = Client(settings)

        try:
            self.collection = self.chroma_client.create_collection(
                name=collection_name, metadata={"dimension": embedding_dim}
            )
        except ValueError:
            # Collection already exists
            self.collection = self.chroma_client.get_collection(name=collection_name)

        # Initialize word embeddings model
        model_name = (
            "word2vec-google-news-300" if use_gpu else "glove-wiki-gigaword-300"
        )
        try:
            self.model = api.load(model_name)  # type: ignore
        except Exception as e:
            raise RuntimeError(f"Failed to load word embeddings model: {str(e)}")  # noqa: B904

    def _get_word_vector(self, word: str) -> np.ndarray:  # type: ignore
        """
        Get the embedding vector for a single word.

        Args:
            word: Input word to get vector for

        Returns:
            Numpy array containing the word vector
        """
        try:
            return self.model[word]  # type: ignore
        except KeyError:
            return np.zeros(self.embedding_dim)

    def _create_embedding(self, text: str) -> List[float]:
        """
        Create embedding for a text string by averaging word vectors.

        Args:
            text: Input text to create embedding for

        Returns:
            List of floats representing the text embedding
        """
        words = text.split()
        if not words:
            return [0.0] * self.embedding_dim

        vectors = [self._get_word_vector(word) for word in words]  # type: ignore
        embedding = np.mean(vectors, axis=0)  # type: ignore
        return embedding.tolist()

    def add_documents(self, documents: List[Shot], batch_size: int = 100) -> None:
        """
        Add multiple documents to the vector store.

        Args:
            documents: List of Document objects to add
            batch_size: Number of documents to process at once

        Raises:
            ValueError: If documents list is empty or contains invalid documents
        """
        if not documents:
            raise ValueError("Documents list cannot be empty")

        # Process documents in batches
        for i in range(0, len(documents), batch_size):
            batch = documents[i : i + batch_size]

            ids = [str(uuid.uuid4()) for _ in batch]
            embeddings = [self._create_embedding(doc.human_input) for doc in batch]
            texts = [doc.human_input for doc in batch]
            metadatas = [{"tool_calls": str(doc.tool_call)} for doc in batch]

            self.collection.add(
                ids=ids,
                embeddings=embeddings,  # type: ignore
                documents=texts,
                metadatas=metadatas,  # type: ignore
            )

    def search(
        self,
        query: str,
        n_results: int = 5,
    ) -> List[Dict[str, Any]]:
        """
        Search for similar documents using the query text.

        Args:
            query: Query text to search for
            n_results: Number of results to return
            metadata_filter: Optional filter to apply on document metadata

        Returns:
            List of dictionaries containing matched documents and their metadata

        Raises:
            ValueError: If n_results is less than 1
        """
        if n_results < 1:
            raise ValueError("n_results must be greater than 0")

        query_embedding = self._create_embedding(query)

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
        )

        # Format results
        formatted_results = []
        for idx in range(len(results["ids"][0])):
            formatted_results.append(  # type: ignore
                {
                    "text": results["documents"][0][idx],  # type: ignore
                    "metadata": eval(results["metadatas"][0][idx]["tool_calls"]),  # type: ignore
                }
            )

        return formatted_results  # type: ignore


vector_db = VectorStore()
vector_db.add_documents(MONGO_SHOTS)
