MONGO_DB_SCHEME = """
{
  "listing_url": str,
  "name": str,
  "summary": str,
  "neighborhood_overview": str,
  "notes": str,
  "transit": str,
  "access": str,
  "interaction": str,
  "house_rules": str,
  "property_type": str,
  "room_type": str,
  "bed_type": str,
  "minimum_nights": str,
  "maximum_nights": str,
  "cancellation_policy": str,
  "last_scraped": str,
  "calendar_last_scraped": str,
  "first_review": str,
  "last_review": str,
  "accommodates": str,
  "bedrooms": str,
  "beds": str,
  "number_of_reviews": str,
  "bathrooms": str,
  "amenities": [str],
  "price": str,
  "security_deposit": str,
  "cleaning_fee": str,
  "extra_people": str,
  "guests_included": str,
  "images": {
    "thumbnail_url": str,
    "medium_url": str,
    "picture_url": str,
    "xl_picture_url": str
  },
  "host": {
    "host_id": str,
    "host_url": str,
    "host_name": str,
    "host_location": str,
    "host_about": str,
    "host_response_time": str,
    "host_thumbnail_url": str,
    "host_picture_url": str,
    "host_neighbourhood": str,
    "host_response_rate": str,
    "host_is_superhost": bool,
    "host_has_profile_pic": bool,
    "host_identity_verified": bool,
    "host_listings_count": str,
    "host_total_listings_count": str,
    "host_verifications": [str]
  },
  "address": {
    "street": str,
    "suburb": str,
    "government_area": str,
    "market": str,
    "country": str,
    "country_code": str,
    "location": {
      "type": str,
      "coordinates": [int],
      "is_location_exact": bool
    }
  },
  "availability": {
    "availability_30": str,
    "availability_60": str,
    "availability_90": str,
    "availability_365": str
  },
  "review_scores": {
    "review_scores_accuracy": str,
    "review_scores_cleanliness": str,
    "review_scores_checkin": str,
    "review_scores_communication": str,
    "review_scores_location": str,
    "review_scores_value": str
    "review_scores_rating": str
  },
  "reviews": [
    {
      "date": str,
      "listing_id": str,
      "reviewer_id": str,
      "reviewer_name": str,
      "comments": str
    }
  ]
}
"""

SAMPLE_DOCUMENT = """
{
  "_id": "10006546",
  "listing_url": "https://www.airbnb.com/rooms/10006546",
  "name": "Ribeira Charming Duplex",
  "summary": "Fantastic duplex apartment",
  "space": "Privileged views of the Douro River",
  "description": "Fantastic duplex apartment",
  "neighborhood_overview": "In the neighborhood of the river",
  "notes": "Lose yourself in the narrow streets",
  "transit": "Transport: • Metro station ",
  "access": "We are always available to help guests. ",
  "interaction": "Cot - 10 € / night Dog - € 7,5 / night",
  "house_rules": "Make the house your home...",
  "property_type": "House",
  "room_type": "Entire home/apt",
  "bed_type": "Real Bed",
  "minimum_nights": "2",
  "maximum_nights": "30",
  "cancellation_policy": "moderate",
  "last_scraped": "1550293200000",
  "calendar_last_scraped": "1550293200000",
  "first_review": "1451797200000",
  "last_review": "1547960400000",
  "accommodates": "8",
  "bedrooms": "3",
  "beds": "5",
  "number_of_reviews": "51",
  "bathrooms": "1.0",
  "amenities": [
    "TV",
    "Cable TV",
    "Wifi",
    "Kitchen",
    "Paid parking off premises",
    "Smoking allowed",
    "Pets allowed",
    "Buzzer/wireless intercom",
    "Heating",
    "Family/kid friendly",
    "Washer",
    "First aid kit",
    "Fire extinguisher",
    "Essentials",
    "Hangers",
    "Hair dryer",
    "Iron",
    "Pack ’n Play/travel crib",
    "Room-darkening shades",
    "Hot water",
    "Bed linens",
    "Extra pillows and blankets",
    "Microwave",
    "Coffee maker",
    "Refrigerator",
    "Dishwasher",
    "Dishes and silverware",
    "Cooking basics",
    "Oven",
    "Stove",
    "Cleaning before checkout",
    "Waterfront"
  ],
  "price": "80.00",
  "security_deposit": "200.00",
  "cleaning_fee": "35.00",
  "extra_people": "15.00",
  "guests_included": "6",
  "images": {
    "thumbnail_url": "",
    "medium_url": "",
    "picture_url": "https://a0.muscache.com/im/",
    "xl_picture_url": ""
  },
  "host": {
    "host_id": "51399391",
    "host_url": "https://www.airbnb.com/users/show/51399391",
    "host_name": "Ana&Gonçalo",
    "host_location": "Porto, Porto District, Portugal",
    "host_about": "Gostamos de passear, de viajar",
    "host_response_time": "within an hour",
    "host_thumbnail_url": "https://a0.muscache.com/im/",
    "host_picture_url": "https://a0.muscache.com/im/",
    "host_neighbourhood": "",
    "host_response_rate": "100",
    "host_is_superhost": false,
    "host_has_profile_pic": true,
    "host_identity_verified": true,
    "host_listings_count": "3",
    "host_total_listings_count": "3",
    "host_verifications": [
      "email",
      "phone",
      "reviews",
      "jumio",
      "offline_government_id",
      "government_id"
    ]
  },
  "address": {
    "street": "Porto, Porto, Portugal",
    "suburb": "",
    "government_area": "Cedofeita, Ildefonso, Sé",
    "market": "Porto",
    "country": "Portugal",
    "country_code": "PT",
    "location": {
      "type": "Point",
      "coordinates": [
        -8.61308,
        41.1413
      ],
      "is_location_exact": false
    }
  },
  "availability": {
    "availability_30": "28",
    "availability_60": "47",
    "availability_90": "74",
    "availability_365": "239"
  },
  "review_scores": {
    "review_scores_accuracy": "9",
    "review_scores_cleanliness": "9",
    "review_scores_checkin": "10",
    "review_scores_communication": "10",
    "review_scores_location": "10",
    "review_scores_value": "9",
    "review_scores_rating": "89"
  },
  "reviews": [
    {
      "_id": "58663741",
      "date": "1451797200000",
      "listing_id": "10006546",
      "reviewer_id": "51483096",
      "reviewer_name": "Cátia",
      "comments": "A casa da Ana."
    }
  ]
}
"""
