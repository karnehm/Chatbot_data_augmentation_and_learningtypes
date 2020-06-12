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