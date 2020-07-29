## hotel happy 4
* request_hotel
    - utter_ask_details
* inform{"startdate": "10.03.2018"}
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

## Generated Story 8298432240511047795
* request_hotel
    - utter_ask_details
* inform{"people": "2"}
    - slot{"people": "2"}
    - utter_ask_location
* correct{"people": "2"}
    - slot{"people": "2"}
    - utter_correct_people_hotel
    - utter_ask_location
* did_that_work
    - utter_more_info_hotel
    - utter_ask_location
* explain
    - utter_explain_location_hotel
    - utter_ask_location
* inform{"location": "paris"}
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

## Generated Story 1847998520898611037
* request_hotel
    - utter_ask_details
* inform{"location": "london"}
    - slot{"location": "london"}
    - utter_ask_people
* explain
    - utter_explain_people_hotel
    - utter_ask_people
* did_that_work
    - utter_more_info_hotel
    - utter_ask_people
* did_that_work
    - utter_more_info_hotel
    - utter_ask_people
* chitchat
    - utter_chitchat
    - utter_ask_people
* chitchat
    - utter_chitchat
    - utter_ask_people
* did_that_work
    - utter_more_info_hotel
    - utter_ask_people
* correct{"location": "rome"}
    - slot{"location": "rome"}
    - utter_correct_location_hotel
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

## Generated Story -7886542752391645811
* request_hotel
    - utter_ask_details
* inform{"startdate": "May 25th"}
    - slot{"startdate": "May 25th"}
    - utter_ask_enddate
* explain
    - utter_explain_enddate_hotel
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
* did_that_work
    - utter_worked_hotel
    - utter_suggest_hotel
* affirm
    - utter_happy

## Generated Story 2794466410122766925
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* inform{"price": "cheap"}
    - slot{"price": "cheap"}
    - utter_ask_location
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_location
* explain
    - utter_explain_location_restaurant
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

## Generated Story -800153815489499233
* request_restaurant
    - utter_ask_details
* inform{"people": "6"}
    - slot{"people": "6"}
    - utter_ask_location
* chitchat
    - utter_chitchat
    - utter_ask_location
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - utter_ask_price
* correct{"location": "rome"}
    - slot{"location": "rome"}
    - utter_correct_location_restaurant
    - utter_ask_price
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_price
* chitchat
    - utter_chitchat
    - utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* did_that_work
    - utter_worked_restaurant
    - utter_suggest_restaurant
* affirm
    - utter_happy