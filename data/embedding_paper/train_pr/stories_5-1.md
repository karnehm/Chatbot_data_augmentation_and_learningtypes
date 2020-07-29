## hotel happy 1
* request_hotel
    - utter_ask_details
* inform{"location": "paris"}
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

## Generated Story 1993489198506904049
* request_hotel
    - utter_ask_details
* inform{"enddate": "next week"}
    - slot{"enddate": "next week"}
    - utter_ask_startdate
* did_that_work
    - utter_more_info_hotel
    - utter_ask_startdate
* explain
    - utter_explain_startdate_hotel
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

## Generated Story 276978480102911357
* request_hotel
    - utter_ask_details
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - utter_ask_people
* chitchat
    - utter_chitchat
    - utter_ask_people
* inform{"people": "1"}
    - slot{"people": "1"}
    - utter_ask_price
* chitchat
    - utter_chitchat
    - utter_ask_price
* correct{"people": "1"}
    - slot{"people": "1"}
    - utter_correct_people_hotel
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
* chitchat
    - utter_chitchat
    - utter_suggest_hotel
* affirm
    - utter_happy

## Generated Story 6738253362774247051
* request_hotel
    - utter_ask_details
* inform{"people": "4", "enddate": "tomorrow"}
    - slot{"people": "4"}
    - slot{"enddate": "tomorrow"}
    - utter_ask_location
* correct{"enddate": "next week"}
    - slot{"enddate": "next week"}
    - utter_correct_enddate_hotel
    - utter_ask_location
* explain
    - utter_explain_location_hotel
    - utter_ask_location
* inform{"location": "london"}
    - slot{"location": "london"}
    - utter_ask_startdate
* inform{"startdate": "May 25th"}
    - slot{"startdate": "May 25th"}
    - utter_ask_price
* inform{"price": "cheap"}
    - slot{"price": "cheap"}
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

## Generated Story 2354048503062275729
* request_hotel
    - utter_ask_details
* inform{"startdate": "today"}
    - slot{"startdate": "today"}
    - utter_ask_enddate
* chitchat
    - utter_chitchat
    - utter_ask_enddate
* explain
    - utter_explain_enddate_hotel
    - utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_location
* inform{"location": "paris"}
    - utter_ask_people
* inform{"people": "4"}
    - utter_filled_slots
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* affirm
    - utter_happy

## Generated Story 8816761424745395625
* request_restaurant
    - utter_ask_details
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_ask_people
* correct{"price": "expensive"}
    - slot{"price": "expensive"}
    - utter_correct_price_restaurant
    - utter_ask_people
* inform{"people": "6"}
    - slot{"people": "6"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_location
* explain
    - utter_explain_location_restaurant
    - utter_ask_location
* inform{"location": "paris"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* did_that_work
    - utter_worked_restaurant
    - utter_suggest_restaurant
* affirm
    - utter_happy

## Generated Story 7486960989920511211
* request_restaurant
    - utter_ask_details
* inform{"people": "2"}
    - slot{"people": "2"}
    - utter_ask_location
* explain
    - utter_explain_location_restaurant
    - utter_ask_location
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_location
* inform{"location": "paris"}
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* chitchat
    - utter_chitchat
    - utter_suggest_restaurant
* chitchat
    - utter_chitchat
    - utter_suggest_restaurant
* affirm
    - utter_happy
