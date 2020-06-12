## story_MUL0896
* inform{"train_destination": "specific"}
   - request_train
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_SNG01940
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform{"taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL3935
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_departure": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"attraction_name": "specific"}
   - welcome_general
   - bye_general

## story_SNG1070
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform
   - inform_attraction
* bye
   - bye_general

## story_MUL2301
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
* inform
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4946
* inform{"hotel_area": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
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

## story_SNG0471
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
   - reqmore_general
* inform{"restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - select_restaurant
   - inform_booking_restaurant
   - inform_restaurant
   - request_booking_restaurant
* inform
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform
   - book_booking_restaurant
* bye
   - bye_general

## story_MUL1898
* inform{"attraction_type": "specific", "attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_leaveAt": "dontcare"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general

## story_SNG01957
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_stars": "dontcare"}
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - reqmore_general
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - book_booking_hotel
   - reqmore_general
* bye
   - greet_general

## story_MUL0484
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_PMUL3919
* inform{"attraction_type": "specific"}
   - request_attraction
* inform{"attraction_area": "dontcare"}
   - inform_attraction
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform
   - inform_restaurant
* inform
   - inform_restaurant
* bye
   - welcome_general
   - bye_general

## story_PMUL1180
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - request_train
* inform{"train_leaveAt": "dontcare"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_attraction
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4660
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - greet_general
* bye
   - bye_general

## story_MUL2269
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"train_departure": "specific"}
   - inform_hotel
   - offerbook_train
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* bye
   - welcome_general
   - bye_general

## story_SNG0767
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_hotel
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "dontcare"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - book_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_PMUL2942
* inform{"hotel_area": "specific", "attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform
   - select_hotel
* inform{"hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL3672
* inform
   - greet_general
   - reqmore_general
* inform{"train_destination": "specific"}
   - request_train
   - greet_general
* inform{"train_day": "specific", "train_departure": "specific"}
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform
   - recommend_attraction
   - reqmore_general
* bye
   - bye_general

## story_MUL0323
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - recommend_restaurant
* inform
   - inform_restaurant
* bye
   - welcome_general
   - bye_general

## story_SNG0345
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
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

## story_MUL0785
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform{"hotel_name": "specific", "train_destination": "specific", "train_departure": "specific"}
   - inform_train
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
   - bye_general

## story_PMUL4432
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbooked_train
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
* inform{"restaurant_name": "specific"}
   - welcome_general
   - bye_general

## story_MUL0810
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - recommend_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
* inform{"restaurant_food": "specific"}
   - recommend_restaurant
* inform
   - inform_restaurant
* inform
   - welcome_general
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4255
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbooked_train
   - reqmore_general
* inform
   - request_attraction
* inform{"attraction_type": "specific"}
   - request_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* bye
   - welcome_general
   - bye_general

## story_PMUL4131
* inform
   - request_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
   - greet_general
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - request_attraction
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_booking_attraction
* bye
   - bye_general

## story_PMUL4610
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_food": "specific"}
   - recommend_restaurant
   - reqmore_general
* bye
   - welcome_general
   - reqmore_general
   - bye_general

## story_MUL1137
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - select_attraction
   - nooffer_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4059
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_hotel
   - recommend_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform{"hotel_name": "specific", "attraction_type": "specific", "attraction_area": "specific"}
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general

## story_PMUL2195
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
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

## story_SNG01835
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2012
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform{"hotel_area": "specific", "hotel_pricerange": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - select_hotel
   - nooffer_hotel
* inform{"hotel_type": "specific"}
   - inform_hotel
* inform{"hotel_parking": "specific"}
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform
   - request_booking_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
* bye
   - welcome_general
   - bye_general

## story_PMUL0182
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"restaurant_reference": "specific", "restaurant_day": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "dontcare"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform
   - inform_hotel
* inform
   - request_taxi
   - greet_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL2980
* inform
   - request_hotel
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_booking_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - book_booking_hotel
* inform{"attraction_type": "specific"}
   - inform_attraction
   - inform_hotel
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1546
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
* inform{"train_departure": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1420
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - request_train
* inform
   - select_train
   - inform_train
* inform
   - inform_train
* inform
   - request_attraction
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* bye
   - bye_general

## story_PMUL2778
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* bye
   - welcome_general

## story_PMUL1966
* inform
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_day": "specific", "hotel_area": "specific", "hotel_parking": "specific", "hotel_type": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - welcome_general

## story_PMUL4122
* inform
   - inform_attraction
   - request_attraction
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - inform_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - welcome_general
   - bye_general
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2359
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform
   - inform_attraction
* inform{"restaurant_food": "specific", "restaurant_area": "specific", "attraction_name": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - nobook_booking_restaurant
   - reqmore_general
* inform
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - inform_booking_restaurant
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
* inform{"taxi_departure": "specific", "restaurant_name": "specific"}
   - request_taxi
   - greet_general
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general