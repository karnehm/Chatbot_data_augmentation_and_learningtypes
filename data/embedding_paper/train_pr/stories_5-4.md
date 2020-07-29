## hotel happy 5
* request_hotel
    - utter_ask_details
* inform{"enddate": "10.03.2018"}
    - utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - utter_ask_location
* inform{"location": "paris"}
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_people
* inform{"people": "4"}
    - utter_filled_slots
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* affirm
    - utter_happy

## Generated Story 9173004962293499764
* request_hotel
    - utter_ask_details
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - utter_ask_people
* chitchat
    - utter_chitchat
    - utter_ask_people
* inform{"people": "2"}
    - slot{"people": "2"}
    - utter_ask_startdate
* chitchat
    - utter_chitchat
    - utter_ask_startdate
* inform{"startdate": "next week"}
    - slot{"startdate": "next week"}
    - utter_ask_enddate
* explain
    - utter_explain_enddate_hotel
    - utter_ask_enddate
* inform{"enddate": "tomorrow"}
    - slot{"enddate": "tomorrow"}
    - utter_ask_location
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - utter_filled_slots
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* did_that_work
    - utter_worked_hotel
    - utter_suggest_hotel
* affirm
    - utter_happy

## Generated Story 3734868848816599930
* request_hotel
    - utter_ask_details
* inform{"enddate": "May 26th"}
    - slot{"enddate": "May 26th"}
    - utter_ask_startdate
* inform{"startdate": "next week"}
    - slot{"startdate": "next week"}
    - utter_ask_location
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - utter_ask_price
* chitchat
    - utter_chitchat
    - utter_ask_price
* explain
    - utter_explain_price_hotel
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_people
* inform{"people": "4"}
    - utter_filled_slots
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* chitchat
    - utter_chitchat
    - utter_suggest_hotel
* affirm
    - utter_happy

## Generated Story 4981076060672777254
* request_hotel
    - utter_ask_details
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - utter_ask_people
* inform{"people": "6"}
    - slot{"people": "6"}
    - utter_ask_price
* inform{"price": "cheap"}
    - slot{"price": "cheap"}
    - utter_ask_startdate
* correct{"price": "expensive"}
    - slot{"price": "expensive"}
    - utter_correct_price_hotel
    - utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - utter_filled_slots
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* chitchat
    - utter_chitchat
    - utter_suggest_hotel
* chitchat
    - utter_chitchat
    - utter_suggest_hotel
* affirm
    - utter_happy

## Generated Story -6175087097443004415
* request_hotel
    - utter_ask_details
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - utter_ask_people
* correct{"location": "rome"}
    - slot{"location": "rome"}
    - utter_correct_location_hotel
    - utter_ask_people
* did_that_work
    - utter_more_info_hotel
    - utter_ask_people
* chitchat
    - utter_chitchat
    - utter_ask_people
* did_that_work
    - utter_more_info_hotel
    - utter_ask_people
* explain
    - utter_explain_people_hotel
    - utter_ask_people
* inform{"people": "4"}
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - utter_filled_slots
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* affirm
    - utter_happy

## Generated Story 5703123541088815095
* request_restaurant
    - utter_ask_details
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - utter_ask_people
* correct{"location": "rome"}
    - slot{"location": "rome"}
    - utter_correct_location_restaurant
    - utter_ask_people
* chitchat
    - utter_chitchat
    - utter_ask_people
* correct{"location": "rome"}
    - slot{"location": "rome"}
    - utter_correct_location_restaurant
    - utter_ask_people
* inform{"people": "4"}
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy

## Generated Story 4623050297171388983
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_price
* correct{"cuisine": "french"}
    - slot{"cuisine": "french"}
    - utter_correct_cuisine_restaurant
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_location
* inform{"location": "paris"}
    - utter_ask_people
* inform{"people": "4"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy