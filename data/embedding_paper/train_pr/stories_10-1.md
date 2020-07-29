## hotel happy 2
* request_hotel
    - utter_ask_details
* inform{"people": "4"}
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
* affirm
    - utter_happy

## restaurant happy 1
* request_restaurant
    - utter_ask_details
* inform{"location": "paris"}
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

## Generated Story 34765273882144065
* request_hotel
    - utter_ask_details
* inform{"people": "4"}
    - slot{"people": "4"}
    - utter_ask_location
* explain
    - utter_explain_location_hotel
    - utter_ask_location
* inform{"location": "london"}
    - slot{"location": "london"}
    - utter_ask_price
* chitchat
    - utter_chitchat
    - utter_ask_price
* inform{"price": "cheap"}
    - slot{"price": "cheap"}
    - utter_ask_startdate
* inform{"startdate": "today"}
    - slot{"startdate": "today"}
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

## Generated Story 6510365135677203478
* request_hotel
    - utter_ask_details
* inform{"startdate": "next week"}
    - slot{"startdate": "next week"}
    - utter_ask_enddate
* correct{"startdate": "May 25th"}
    - slot{"startdate": "May 25th"}
    - utter_correct_startdate_hotel
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

## Generated Story -2016230675575359615
* request_hotel
    - utter_ask_details
* inform{"startdate": "today"}
    - slot{"startdate": "today"}
    - utter_ask_enddate
* did_that_work
    - utter_more_info_hotel
    - utter_ask_enddate
* chitchat
    - utter_chitchat
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
* did_that_work
    - utter_worked_hotel
    - utter_suggest_hotel
* affirm
    - utter_happy

## Generated Story -1274354813326186979
* request_hotel
    - utter_ask_details
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - utter_ask_people
* inform{"people": "4"}
    - slot{"people": "4"}
    - utter_ask_startdate
* inform{"startdate": "today"}
    - slot{"startdate": "today"}
    - utter_ask_enddate
* correct{"people": "4"}
    - slot{"people": "4"}
    - utter_correct_people_hotel
    - utter_ask_enddate
* chitchat
    - utter_chitchat
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

## Generated Story 6414425509425784419
* request_hotel
    - utter_ask_details
* inform{"startdate": "next week"}
    - slot{"startdate": "next week"}
    - utter_ask_enddate
* inform{"enddate": "May 26th"}
    - slot{"enddate": "May 26th"}
    - utter_ask_price
* correct{"enddate": "next week"}
    - slot{"enddate": "next week"}
    - utter_correct_enddate_hotel
    - utter_ask_price
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_ask_location
* explain
    - utter_explain_location_hotel
    - utter_ask_location
* chitchat
    - utter_chitchat
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

## Generated Story -4377383468731851742
* request_hotel
    - utter_ask_details
* inform{"location": "london"}
    - slot{"location": "london"}
    - utter_ask_people
* chitchat
    - utter_chitchat
    - utter_ask_people
* inform{"people": "1"}
    - slot{"people": "1"}
    - utter_ask_price
* correct{"people": "2"}
    - slot{"people": "2"}
    - utter_correct_people_hotel
    - utter_ask_price
* correct{"people": "4"}
    - slot{"people": "4"}
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
* did_that_work
    - utter_worked_hotel
    - utter_suggest_hotel
* affirm
    - utter_happy

## Generated Story 8538074372841459949
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "french"}
    - slot{"cuisine": "french"}
    - utter_ask_price
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_price
* did_that_work
    - utter_more_info_restaurant
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
* chitchat
    - utter_chitchat
    - utter_suggest_restaurant
* affirm
    - utter_happy

## Generated Story 4803662585436590829
* request_restaurant
    - utter_ask_details
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_ask_people
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_people
* explain
    - utter_explain_people_restaurant
    - utter_ask_people
* inform{"people": "4"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - utter_ask_location
* inform{"location": "paris"}
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
* chitchat
    - utter_chitchat
    - utter_suggest_restaurant
* affirm
    - utter_happy

## Generated Story 8407838656397991270
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "french"}
    - slot{"cuisine": "french"}
    - utter_ask_price
* inform{"price": "cheap"}
    - slot{"price": "cheap"}
    - utter_ask_location
* inform{"location": "london"}
    - slot{"location": "london"}
    - utter_ask_people
* inform{"people": "2"}
    - slot{"people": "2"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant":"results"}
    - utter_suggest_restaurant
* correct{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_correct_cuisine_restaurant
    - action_search_restaurant
    - slot{"restaurant":"results"}
    - utter_suggest_restaurant
* correct{"people": "2"}
    - slot{"people": "2"}
    - utter_correct_people_restaurant
    - action_search_restaurant
    - slot{"restaurant":"results"}
    - utter_suggest_restaurant
* correct{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_correct_price_restaurant
    - action_search_restaurant
    - slot{"restaurant":"results"}
    - utter_suggest_restaurant
* correct{"people": "4"}
    - slot{"people": "4"}
    - utter_correct_people_restaurant
    - action_search_restaurant
    - slot{"restaurant":"results"}
    - utter_suggest_restaurant
* did_that_work
    - utter_worked_restaurant
    - utter_suggest_restaurant
* affirm
    - utter_happy

## Generated Story -8694893665571774584
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "french"}
    - slot{"cuisine": "french"}
    - utter_ask_price
* correct{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_correct_cuisine_restaurant
    - utter_ask_price
* chitchat
    - utter_chitchat
    - utter_ask_price

## Generated Story 8130156986372571232
* request_restaurant
    - utter_ask_details
* inform{"people": "4", "location": "paris"}
    - slot{"people": "4"}
    - slot{"location": "paris"}
    - utter_ask_price
* chitchat
    - utter_chitchat
    - utter_ask_price
* chitchat
    - utter_chitchat
    - utter_ask_price
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* did_that_work
    - utter_worked_restaurant
    - utter_suggest_restaurant
* affirm
    - utter_happy