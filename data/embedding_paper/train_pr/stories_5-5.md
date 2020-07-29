## Generated Story 7692376286038639225
* request_hotel
    - utter_ask_details
* inform{"startdate": "today", "price": "expensive"}
    - slot{"startdate": "today"}
    - slot{"price": "expensive"}
    - utter_ask_enddate
* inform{"enddate": "10.03.2018"}
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

## Generated Story -446032599677574593
* request_hotel
    - utter_ask_details
* inform{"people": "4"}
    - slot{"people": "4"}
    - utter_ask_location
* did_that_work
    - utter_more_info_hotel
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

## Generated Story 4883852117397942198
* request_hotel
    - utter_ask_details
* inform{"price": "cheap"}
    - slot{"price": "cheap"}
    - utter_ask_people
* inform{"people": "2"}
    - slot{"people": "2"}
    - utter_ask_startdate
* inform{"startdate": "today"}
    - slot{"startdate": "today"}
    - utter_ask_enddate
* correct{"startdate": "today"}
    - slot{"startdate": "today"}
    - utter_correct_startdate_hotel
    - utter_ask_enddate
* explain
    - utter_explain_enddate_hotel
    - utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - utter_ask_location
* inform{"location": "paris"}
    - utter_filled_slots
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* affirm
    - utter_happy

## Generated Story 8055972029495514177
* request_hotel
    - utter_ask_details
* inform{"startdate": "next week"}
    - slot{"startdate": "next week"}
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
* affirm
    - utter_happy

## Generated Story -1636298539059010529
* request_hotel
    - utter_ask_details
* inform{"startdate": "May 25th"}
    - slot{"startdate": "May 25th"}
    - utter_ask_enddate
* correct{"startdate": "May 25th"}
    - slot{"startdate": "May 25th"}
    - utter_correct_startdate_hotel
    - utter_ask_enddate
* chitchat
    - utter_chitchat
    - utter_ask_enddate
* did_that_work
    - utter_more_info_hotel
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

## Generated Story 8910081089962091554
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* correct{"cuisine": "french"}
    - slot{"cuisine": "french"}
    - utter_correct_cuisine_restaurant
    - utter_ask_price
* correct{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_correct_cuisine_restaurant
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_location
* inform{"location": "london"}
    - slot{"location": "london"}
    - utter_ask_people
* inform{"people": "1"}
    - slot{"people": "1"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* did_that_work
    - utter_worked_restaurant
    - utter_suggest_restaurant
* affirm
    - utter_happy

## Generated Story 5854594747809472876
* request_restaurant
    - utter_ask_details
* inform{"people": "6"}
    - slot{"people": "6"}
    - utter_ask_location
* explain
    - utter_explain_location_restaurant
    - utter_ask_location
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - utter_ask_cuisine
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_cuisine
* explain
    - utter_explain_cuisine_restaurant
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