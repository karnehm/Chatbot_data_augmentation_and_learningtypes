## story_PMUL1316
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"attraction_type": "specific", "train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* bye
   - bye_general

## story_MUL0937
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_booking_restaurant
   - request_restaurant
* inform{"restaurant_day": "specific", "restaurant_area": "dontcare"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"restaurant_name": "specific", "attraction_area": "specific"}
   - recommend_attraction
* inform
   - inform_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL3012
* inform{"attraction_name": "specific"}
   - inform_attraction
   - greet_general
* inform
   - select_attraction
   - inform_attraction
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform{"restaurant_pricerange": "specific"}
   - request_restaurant
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0212
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - select_restaurant
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
* inform
   - inform_restaurant
   - request_booking_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* bye
   - welcome_general

## story_PMUL2215
* inform
   - request_restaurant
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - recommend_attraction
* inform
   - inform_attraction
* inform
   - inform_attraction
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_SNG01270
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - greet_general

## story_MUL2119
* inform{"hotel_parking": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - request_hotel
* inform{"hotel_area": "specific", "hotel_pricerange": "dontcare"}
   - select_hotel
   - inform_hotel
* inform
   - inform_hotel
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* bye
   - bye_general

## story_PMUL4622
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - bye_general

## story_MUL2491
* inform{"restaurant_food": "specific"}
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
   - greet_general
* inform
   - inform_restaurant
* inform{"attraction_area": "specific"}
   - select_attraction
   - inform_attraction
* inform
   - select_attraction
   - select_restaurant
* inform
   - recommend_attraction
   - reqmore_general
* inform{"taxi_departure": "specific"}
   - inform_attraction
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL2703
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - greet_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
* bye
   - inform_attraction

## story_PMUL4356
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
   - greet_general
* inform{"restaurant_area": "specific"}
   - select_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - greet_general
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
   - greet_general
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - bye_general

## story_PMUL3162
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - select_restaurant
* inform{"restaurant_pricerange": "dontcare"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform{"train_destination": "specific"}
   - offerbook_train
* bye
   - bye_general

## story_SNG01679
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform{"taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi

## story_PMUL3494
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific", "restaurant_food": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - recommend_restaurant
   - book_booking_restaurant
* inform{"restaurant_food": "specific", "restaurant_name": "specific"}
   - bye_general

## story_SNG0006
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_MUL0831
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform
   - nooffer_restaurant
* inform
   - recommend_restaurant
* inform{"restaurant_food": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0466
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* bye
   - bye_general

## story_PMUL2286
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform
   - inform_restaurant
   - recommend_restaurant
   - reqmore_general
* inform
   - inform_booking_restaurant
   - inform_restaurant
   - greet_general
* inform
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform
   - welcome_general
   - bye_general
* bye
   - welcome_general
   - bye_general

## story_PMUL0745
* inform
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - bye_general

## story_PMUL4515
* inform
   - request_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"hotel_type": "specific"}
   - select_hotel
* inform{"hotel_pricerange": "specific"}
   - request_hotel
* inform{"hotel_area": "dontcare"}
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* bye
   - welcome_general

## story_SNG0360
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL2239
* inform
   - request_restaurant
   - greet_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform
   - inform_attraction
* inform
   - request_taxi
* inform
   - greet_general
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - greet_general
   - reqmore_general
* bye
   - bye_general

## story_SNG1048
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_stars": "dontcare", "hotel_type": "specific"}
   - nooffer_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_PMUL4318
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "dontcare"}
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"hotel_name": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_type": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform{"taxi_destination": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_PMUL2497
* inform{"restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - nooffer_attraction
   - reqmore_general
* inform{"attraction_type": "specific"}
   - select_attraction
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_MUL1276
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform
   - inform_booking_restaurant
   - inform_restaurant
* inform{"hotel_area": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_type": "specific"}
   - inform_hotel
* inform
   - welcome_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG1026
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_internet": "specific"}
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
   - reqmore_general
* inform
   - inform_hotel
* inform
   - inform_hotel
* bye
   - bye_general

## story_MUL2347
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
* inform
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - recommend_attraction
   - greet_general
   - reqmore_general
* inform
   - recommend_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4077
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform
   - recommend_hotel
* inform{"hotel_area": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_internet": "specific"}
   - inform_hotel
   - recommend_hotel
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_area": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_PMUL0457
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform{"hotel_parking": "specific"}
   - inform_hotel
* inform
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2116
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - request_hotel
   - greet_general
* inform{"hotel_area": "dontcare", "hotel_parking": "specific", "hotel_pricerange": "dontcare"}
   - select_hotel
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - greet_general
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
   - reqmore_general
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - greet_general
   - welcome_general
   - bye_general

## story_PMUL1982
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_hotel
* inform{"hotel_name": "specific", "hotel_internet": "specific"}
   - inform_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - welcome_general
   - bye_general

## story_PMUL1091
* inform{"train_day": "specific"}
   - inform_train
* inform
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"attraction_area": "specific"}
   - request_attraction
* inform{"attraction_type": "specific"}
   - recommend_attraction
* bye
   - bye_general

## story_PMUL4388
* inform
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general

## story_MUL1228
* inform
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"hotel_area": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_PMUL1762
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1746
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - bye_general

## story_MUL2637
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific"}
   - inform_hotel
   - recommend_hotel
* inform{"hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - inform_attraction
   - bye_general