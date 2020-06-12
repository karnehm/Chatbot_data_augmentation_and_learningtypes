## story_SNG0073
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL4648
* inform
   - nooffer_restaurant
   - request_restaurant
* inform
   - inform_restaurant
   - request_restaurant
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform
   - inform_restaurant
* inform
   - bye_general
* bye
   - bye_general

## story_PMUL2437
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform
   - reqmore_general
* inform
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_food": "specific", "restaurant_name": "specific", "attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_MUL2499
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* inform
   - bye_general
* bye
   - bye_general

## story_MUL1575
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general
   - bye_general

## story_MUL0671
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - offerbook_train
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_PMUL2636
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
* inform{"attraction_type": "specific"}
   - nooffer_attraction
   - request_attraction
* inform
   - inform_attraction
* inform
   - inform_attraction
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
   - reqmore_general
   - bye_general

## story_PMUL3027
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "dontcare"}
   - recommend_attraction
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* inform
   - request_train
* inform
   - reqmore_general
* inform
   - welcome_general
* bye
   - welcome_general
   - bye_general

## story_MUL1489
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_pricerange": "specific", "restaurant_name": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - inform_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - greet_general

## story_SNG01608
* inform{"restaurant_food": "specific"}
   - inform_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - recommend_restaurant
* inform
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - welcome_general
   - bye_general

## story_SNG0888
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - request_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_MUL2305
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "dontcare"}
   - inform_attraction
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_area": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - inform_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_MUL2321
* inform
   - request_restaurant
   - greet_general
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1812
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* inform
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_pricerange": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
   - reqmore_general
* bye
   - welcome_general

## story_MUL2569
* inform{"attraction_type": "specific"}
   - select_attraction
   - inform_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_stars": "dontcare"}
   - recommend_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_MUL1491
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_MUL1060
* inform{"hotel_parking": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_internet": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"attraction_name": "specific", "attraction_area": "specific"}
   - nooffer_attraction
* inform
   - nooffer_attraction
   - reqmore_general
* inform{"attraction_type": "specific"}
   - select_attraction
   - inform_attraction
* inform{"attraction_name": "specific"}
   - nooffer_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - greet_general

## story_PMUL3647
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
   - greet_general
* inform{"restaurant_day": "specific", "restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"attraction_area": "specific"}
   - inform_attraction
   - recommend_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1045
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform{"taxi_destination": "specific", "attraction_name": "specific"}
   - request_taxi
* inform{"hotel_parking": "specific"}
   - inform_hotel
* inform{"hotel_area": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - inform_hotel
   - book_booking_hotel
   - reqmore_general
* inform{"hotel_name": "specific"}
   - bye_general

## story_SNG01936
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - welcome_general

## story_MUL1642
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - select_train
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - reqmore_general
* bye
   - bye_general

## story_MUL2320
* inform{"attraction_type": "specific"}
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_attraction
* bye
   - welcome_general
   - bye_general

## story_PMUL0550
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* bye
   - welcome_general
   - bye_general

## story_MUL1612
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"restaurant_name": "specific"}
   - select_restaurant
   - inform_restaurant
* inform
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_area": "specific"}
   - nobook_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform
   - inform_restaurant
   - reqmore_general
* bye
   - bye_general

## story_MUL0088
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
   - request_hotel
* inform
   - nooffer_hotel
   - reqmore_general
* inform{"hotel_pricerange": "specific"}
   - nooffer_hotel
   - reqmore_general
* inform
   - select_hotel
   - inform_hotel
* inform{"restaurant_name": "specific", "hotel_area": "dontcare"}
   - inform_booking_restaurant
   - inform_hotel
* inform
   - inform_hotel
* inform{"hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_MUL0469
* inform{"train_departure": "specific"}
   - inform_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform{"attraction_type": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_area": "dontcare"}
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - welcome_general
   - bye_general
* bye
   - welcome_general
   - bye_general

## story_MUL1926
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"attraction_area": "specific"}
   - select_attraction
   - inform_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1526
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - request_hotel
* inform{"hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - welcome_general
   - bye_general
* bye
   - welcome_general
   - bye_general

## story_SNG0689
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "specific"}
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* bye
   - bye_general

## story_PMUL4626
* inform{"train_departure": "specific"}
   - inform_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
* inform
   - inform_train
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL1283
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2376
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_MUL1024
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - recommend_attraction
* inform
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - reqmore_general
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - inform_booking_hotel
* inform
   - inform_hotel
* inform
   - nobook_booking_hotel
* inform
   - inform_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0263
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - request_train
* inform
   - inform_train
   - reqmore_general
* bye
   - bye_general

## story_MUL1350
* inform{"hotel_area": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_parking": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - reqmore_general
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
* inform
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific", "restaurant_area": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general

## story_MUL1799
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* bye
   - greet_general
   - welcome_general
   - bye_general

## story_MUL2405
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform
   - inform_booking_restaurant
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "dontcare"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - greet_general
* bye
   - bye_general

## story_SNG0515
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* bye
   - bye_general

## story_MUL2294
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_area": "specific", "hotel_parking": "specific"}
   - inform_booking_hotel
* inform
   - inform_hotel
* inform
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general
   - bye_general

## story_MUL1066
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - nobook_booking_hotel
* inform
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "dontcare"}
   - recommend_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform{"taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_SNG01386
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* bye
   - bye_general

## story_MUL2290
* inform
   - request_train
   - greet_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform{"hotel_parking": "specific"}
   - inform_hotel
   - reqmore_general
* inform
   - inform_hotel
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
   - greet_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2162
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform{"hotel_pricerange": "specific"}
   - request_hotel
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_parking": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "dontcare"}
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - greet_general
   - welcome_general
   - bye_general

## story_SNG0991
* inform{"hotel_parking": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - select_hotel
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_PMUL3596
* inform
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_parking": "specific", "hotel_pricerange": "specific", "hotel_internet": "specific"}
   - recommend_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_MUL0409
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_MUL1192
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - inform_hotel
   - book_booking_hotel
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform
   - welcome_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL2755
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - recommend_hotel
   - nooffer_hotel
* inform{"hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_day": "specific", "hotel_pricerange": "dontcare"}
   - recommend_hotel
* inform{"hotel_name": "specific", "attraction_type": "specific", "attraction_area": "specific"}
   - select_attraction
   - inform_attraction
* inform
   - inform_booking_hotel
   - recommend_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - request_taxi
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_taxi
   - reqmore_general
* inform
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_PMUL3126
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general

## story_MUL1650
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform
   - inform_booking_restaurant
   - inform_restaurant
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0451
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL3868
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform{"hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
* inform{"hotel_pricerange": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_area": "specific"}
   - inform_hotel
   - reqmore_general
* bye
   - bye_general

## story_MUL2177
* inform{"hotel_internet": "dontcare", "hotel_type": "specific"}
   - inform_hotel
   - nooffer_hotel
* inform{"hotel_parking": "specific"}
   - request_hotel
* inform{"hotel_pricerange": "dontcare"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "dontcare", "hotel_stars": "dontcare"}
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
   - reqmore_general
* inform
   - inform_hotel
* inform
   - inform_hotel
   - request_hotel
* inform
   - nobook_booking_hotel
   - reqmore_general
* inform
   - inform_hotel
   - reqmore_general
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - inform_hotel
   - book_booking_hotel
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* bye
   - bye_general

## story_PMUL1276
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
   - greet_general
* inform
   - inform_attraction
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - request_train
* inform
   - inform_train
* inform
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_MUL0264
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform{"restaurant_food": "dontcare"}
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
* bye
   - greet_general
   - bye_general

## story_PMUL4134
* inform{"attraction_type": "specific", "attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - request_train
* inform
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform
   - bye_general
* bye
   - welcome_general

## story_MUL2675
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform
   - welcome_general
* inform
   - inform_booking_hotel
   - inform_hotel
* inform{"attraction_area": "specific"}
   - recommend_attraction
* inform{"attraction_type": "specific", "attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL1883
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - reqmore_general
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"hotel_name": "specific"}
   - inform_hotel
* inform{"hotel_parking": "specific"}
   - inform_hotel
* inform
   - welcome_general
* bye
   - bye_general

## story_MUL1139
* inform{"hotel_parking": "specific", "hotel_pricerange": "specific"}
   - inform_hotel
* inform{"hotel_internet": "specific"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - recommend_hotel
   - book_booking_hotel
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - recommend_attraction
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_MUL1064
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
   - reqmore_general
* inform{"attraction_type": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform{"hotel_name": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_PMUL4643
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
* inform
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - request_hotel
* inform{"hotel_area": "specific", "hotel_internet": "specific"}
   - request_hotel
* inform{"hotel_type": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - welcome_general

## story_PMUL3890
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_leaveAt": "dontcare"}
   - inform_train
   - offerbook_train
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform{"hotel_area": "dontcare", "hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform
   - reqmore_general
* inform{"restaurant_area": "specific"}
   - welcome_general

## story_PMUL0286
* inform
   - inform_hotel
* inform{"hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific", "restaurant_area": "specific", "hotel_pricerange": "specific", "hotel_type": "specific"}
   - inform_hotel
   - nooffer_restaurant
* inform{"taxi_departure": "specific", "restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_booking_taxi
   - inform_restaurant
* inform
   - inform_booking_taxi
   - inform_restaurant
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1690
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
* inform{"train_departure": "specific"}
   - inform_train
   - reqmore_general
* inform
   - inform_train
   - offerbook_train
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
   - reqmore_general
* bye
   - bye_general

## story_PMUL2124
* inform
   - request_restaurant
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_area": "dontcare"}
   - recommend_restaurant
   - request_restaurant
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"attraction_area": "specific"}
   - request_attraction
* inform
   - request_attraction
* inform
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_PMUL0265
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "dontcare"}
   - inform_restaurant
   - recommend_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4919
* inform{"attraction_type": "specific"}
   - select_attraction
   - inform_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform
   - reqmore_general
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - nooffer_train
   - request_train
* inform
   - select_train
* bye
   - inform_train

## story_SNG0681
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - recommend_restaurant
   - nooffer_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
   - reqmore_general
* bye
   - bye_general

## story_PMUL1374
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - nooffer_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_SNG0085
* inform
   - request_taxi
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - bye_general

## story_SNG0898
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform
   - nooffer_hotel
   - request_hotel
* inform{"hotel_pricerange": "specific"}
   - inform_hotel
* inform
   - request_hotel
* inform
   - inform_booking_hotel
   - recommend_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform
   - welcome_general
   - bye_general
* bye
   - welcome_general
   - bye_general

## story_MUL0842
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_name": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"attraction_area": "specific"}
   - select_attraction
* inform{"attraction_type": "specific"}
   - nooffer_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_MUL1818
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - welcome_general
   - bye_general
* inform
   - request_train
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_leaveAt": "dontcare"}
   - inform_train
   - offerbook_train
* inform
   - reqmore_general
* bye
   - welcome_general

## story_SNG0601
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_name": "specific"}
   - bye_general

## story_SNG02153
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - greet_general

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

## story_MUL1008
* inform{"hotel_pricerange": "specific", "hotel_internet": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_parking": "specific"}
   - select_hotel
   - inform_hotel
* inform
   - inform_hotel
   - reqmore_general
* inform
   - inform_hotel
   - greet_general
* inform{"attraction_area": "specific"}
   - inform_hotel
   - recommend_attraction
   - greet_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_SNG01323
* inform{"hotel_parking": "specific", "hotel_internet": "specific", "hotel_type": "specific"}
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific", "hotel_type": "specific"}
   - inform_hotel
   - recommend_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - welcome_general

## story_PMUL0095
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
* inform{"hotel_name": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
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

## story_MUL1870
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - inform_train
   - reqmore_general
* bye
   - welcome_general

## story_MUL2665
* inform{"hotel_internet": "specific", "hotel_type": "specific"}
   - request_hotel
* inform
   - recommend_hotel
* inform{"hotel_name": "specific", "hotel_area": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"attraction_type": "specific"}
   - recommend_attraction
* inform
   - inform_attraction
* bye
   - bye_general

## story_PMUL3668
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
   - recommend_restaurant
   - greet_general
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - greet_general
   - reqmore_general
* inform{"attraction_area": "specific"}
   - request_attraction
* inform
   - recommend_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* bye
   - welcome_general
   - bye_general

## story_PMUL1247
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform
   - inform_attraction
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - inform_train
* bye
   - bye_general

## story_SNG0391
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific"}
   - inform_train
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* bye
   - bye_general

## story_PMUL3376
* inform{"train_destination": "specific"}
   - request_train
   - greet_general
* inform{"train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - greet_general
   - reqmore_general
* bye
   - greet_general
   - welcome_general
   - bye_general

## story_PMUL2483
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "specific"}
   - inform_attraction
   - recommend_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific", "attraction_name": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - welcome_general
   - bye_general

## story_PMUL2704
* inform{"attraction_area": "specific"}
   - recommend_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - nobook_booking_attraction
* inform{"hotel_internet": "specific"}
   - request_hotel
* inform
   - request_hotel
* inform{"hotel_area": "specific"}
   - inform_booking_hotel
   - recommend_hotel
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0309
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform
   - inform_restaurant
* inform{"train_day": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - reqmore_general
* bye
   - welcome_general

## story_PMUL4306
* inform{"restaurant_pricerange": "specific", "restaurant_area": "specific"}
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - recommend_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* bye
   - welcome_general

## story_PMUL3336
* inform{"attraction_area": "specific"}
   - recommend_attraction
   - greet_general
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - recommend_hotel
* inform{"restaurant_name": "specific"}
   - inform_restaurant
   - reqmore_general
* bye
   - greet_general
   - bye_general

## story_PMUL4819
* inform{"train_day": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_departure": "specific"}
   - inform_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - reqmore_general
* inform{"hotel_pricerange": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_parking": "specific"}
   - inform_hotel
   - reqmore_general
* inform{"hotel_day": "specific", "hotel_name": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - bye_general

## story_SNG0611
* inform{"restaurant_food": "specific", "restaurant_area": "specific"}
   - select_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific", "restaurant_pricerange": "specific"}
   - nobook_booking_restaurant
   - request_booking_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_booking_restaurant
   - recommend_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - nobook_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - inform_restaurant
   - book_booking_restaurant
   - reqmore_general
* inform
   - welcome_general
* bye
   - bye_general

## story_PMUL0674
* inform
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - inform_booking_restaurant
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - request_booking_restaurant
* inform
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
* inform
   - inform_train
* bye
   - bye_general

## story_MUL1883
* inform{"train_departure": "specific"}
   - request_train
* inform
   - inform_train
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
* inform{"attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform
   - inform_attraction
* inform
   - reqmore_general
* bye
   - bye_general

## story_PMUL3737
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform
   - inform_train
   - nooffer_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
   - nooffer_attraction
   - reqmore_general
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform
   - inform_attraction
   - recommend_attraction
   - reqmore_general
* bye
   - bye_general

## story_SNG01752
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform
   - request_taxi
* inform{"taxi_destination": "specific"}
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_SNG0775
* inform
   - inform_hotel
   - recommend_hotel
* inform{"hotel_area": "specific", "hotel_internet": "specific"}
   - select_hotel
   - inform_hotel
* inform{"hotel_day": "specific", "hotel_pricerange": "dontcare", "hotel_type": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* inform{"hotel_name": "specific"}
   - inform_hotel
* bye
   - greet_general

## story_MUL0515
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform{"attraction_area": "specific"}
   - inform_attraction
   - request_attraction
* inform{"attraction_type": "dontcare"}
   - recommend_attraction
* inform
   - reqmore_general
* bye
   - welcome_general

## story_PMUL1739
* inform{"train_destination": "specific", "train_day": "specific"}
   - request_train
* inform{"train_departure": "specific"}
   - request_train
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_train
   - offerbooked_train
   - reqmore_general
* inform{"train_reference": "specific"}
   - offerbooked_train
   - reqmore_general
* inform
   - inform_hotel
   - request_hotel
* inform{"hotel_area": "specific"}
   - request_hotel
* inform{"hotel_pricerange": "dontcare", "hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
   - recommend_hotel
* inform
   - inform_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
* bye
   - bye_general

## story_SNG0348
* inform
   - request_train
* inform{"train_destination": "specific"}
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - reqmore_general
* bye
   - bye_general

## story_MUL0818
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - nooffer_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_food": "specific"}
   - inform_restaurant
   - request_restaurant
* inform{"restaurant_pricerange": "specific"}
   - inform_restaurant
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - inform_attraction
* inform{"taxi_destination": "specific", "taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* inform
   - inform_taxi
   - reqmore_general
* bye
   - bye_general

## story_PMUL1137
* inform{"attraction_type": "specific"}
   - inform_attraction
* inform
   - recommend_attraction
   - reqmore_general
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - select_train
   - inform_train
* inform
   - inform_train
* inform
   - reqmore_general
* inform
   - inform_train
* bye
   - welcome_general
   - bye_general

## story_PMUL4884
* inform{"train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific", "train_day": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - request_train
* inform{"hotel_name": "specific"}
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - inform_hotel
   - offerbooked_train
* inform
   - inform_hotel
* inform
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL2609
* inform{"attraction_name": "specific"}
   - inform_attraction
* inform
   - welcome_general
* inform
   - bye_general
* inform{"hotel_pricerange": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform{"hotel_parking": "specific"}
   - select_hotel
   - inform_hotel
   - request_booking_hotel
* inform{"hotel_name": "specific"}
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL0004
* inform{"restaurant_name": "specific"}
   - inform_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"hotel_type": "specific"}
   - inform_hotel
* inform
   - select_hotel
* inform{"hotel_parking": "specific", "hotel_internet": "specific"}
   - inform_booking_hotel
   - inform_hotel
* inform
   - inform_hotel
* inform
   - welcome_general
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_PMUL4239
* inform{"attraction_type": "specific", "attraction_name": "specific"}
   - inform_attraction
   - reqmore_general
* inform
   - inform_attraction
* inform{"train_destination": "specific"}
   - inform_train
   - request_train
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
   - offerbook_train
   - reqmore_general
* inform
   - action_book_train
   - slot{"train_trainID": "specific", "train_reference": "specific"}
   - offerbooked_train
* bye
   - welcome_general

## story_SNG01819
* inform{"taxi_destination": "specific"}
   - request_taxi
* inform{"taxi_departure": "specific"}
   - request_taxi
* inform
   - action_book_taxi
   - slot{"taxi_type": "specific"}
   - inform_taxi
* bye
   - bye_general

## story_MUL0297
* inform{"restaurant_food": "specific", "restaurant_pricerange": "specific"}
   - inform_restaurant
* inform{"restaurant_name": "specific"}
   - request_booking_restaurant
* inform{"restaurant_day": "specific"}
   - action_book_restaurant
   - slot{"restaurant_name": "specific", "restaurant_reference": "specific"}
   - book_booking_restaurant
   - reqmore_general
* inform{"train_day": "specific", "train_departure": "specific"}
   - inform_train
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
* inform
   - inform_train
* inform
   - inform_train
   - offerbook_train
* inform
   - inform_train
* bye
   - greet_general

## story_SNG0840
* inform{"hotel_internet": "specific"}
   - nooffer_hotel
   - reqmore_general
* inform{"hotel_pricerange": "specific"}
   - select_hotel
   - inform_hotel
* inform
   - inform_booking_hotel
   - inform_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - request_booking_hotel
* inform
   - nobook_booking_hotel
   - request_booking_hotel
* inform{"hotel_day": "specific"}
   - nobook_booking_hotel
   - request_booking_hotel
* inform
   - nobook_booking_hotel
   - nooffer_hotel
   - reqmore_general
* inform{"hotel_day": "specific"}
   - action_book_hotel
   - slot{"hotel_name": "specific", "hotel_reference": "specific"}
   - book_booking_hotel
   - reqmore_general
* bye
   - welcome_general
   - bye_general

## story_MUL1800
* inform{"train_day": "specific", "train_departure": "specific"}
   - request_train
* inform{"train_destination": "specific"}
   - inform_train
   - offerbook_train
* inform
   - inform_train
* inform
   - offerbook_train
   - request_train
* inform{"attraction_type": "specific", "attraction_area": "specific"}
   - inform_attraction
* inform{"attraction_name": "specific"}
   - inform_attraction
   - inform_booking_attraction
   - request_booking_attraction
* inform
   - inform_attraction
   - reqmore_general
* bye
   - bye_general

## story_MUL1806
