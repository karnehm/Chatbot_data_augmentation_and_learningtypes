## Generated Story -6821548152705280771
* request_hotel
    - utter_ask_details
* inform{"people": "2", "enddate": "May 26th"}
    - slot{"people": "2"}
    - slot{"enddate": "May 26th"}
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
* affirm
    - utter_happy

## hotel happy 3
* request_hotel
    - utter_ask_details
* inform{"price": "expensive"}
    - utter_ask_people
* inform{"people": "4"}
    - utter_ask_startdate
* inform{"startdate": "10.03.2018"}
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

## Generated Story 1074034796281423152
* request_restaurant
    - utter_ask_details
* inform{"people": "4", "cuisine": "french"}
    - slot{"people": "4"}
    - slot{"cuisine": "french"}
    - utter_ask_price
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_ask_location
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy


## Generated Story 1074034796281423152
* request_restaurant
    - utter_ask_details
* inform{"people": "4", "cuisine": "french"}
    - slot{"people": "4"}
    - slot{"cuisine": "french"}
    - utter_ask_price
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_ask_location
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy


## Generated Story -8797333378697904114
* request_hotel
    - utter_ask_details
* inform{"location": "london"}
    - slot{"location": "london"}
    - utter_ask_people
* explain
    - utter_explain_people_hotel
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

## Generated Story -6544064798950701442
* request_hotel
    - utter_ask_details
* inform{"location": "london"}
    - slot{"location": "london"}
    - utter_ask_people
* correct{"location": "rome"}
    - slot{"location": "rome"}
    - utter_correct_location_hotel
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
* chitchat
    - utter_chitchat
    - utter_suggest_hotel
* chitchat
    - utter_chitchat
    - utter_suggest_hotel
* affirm
    - utter_happy

## Generated Story -5568287998497575386
* request_hotel
    - utter_ask_details
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - utter_ask_people
* correct{"location": "london"}
    - slot{"location": "london"}
    - utter_correct_location_hotel
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

## Generated Story -7619175073147269387
* request_hotel
    - utter_ask_details
* inform{"startdate": "May 25th", "location": "rome"}
    - slot{"startdate": "May 25th"}
    - slot{"location": "rome"}
    - utter_ask_people
* chitchat
    - utter_chitchat
    - utter_ask_people
* chitchat
    - utter_chitchat
    - utter_ask_people
* correct{"startdate": "next week"}
    - slot{"startdate": "next week"}
    - utter_correct_startdate_hotel
    - utter_ask_people
* explain
    - utter_explain_people_hotel
    - utter_ask_people
* inform{"people": "6"}
    - slot{"people": "6"}
    - utter_ask_price
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_ask_enddate
* inform{"enddate": "tomorrow"}
    - slot{"enddate": "tomorrow"}
    - utter_filled_slots
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* affirm
    - utter_happy

## Generated Story 3530936682833259559
* request_hotel
    - utter_ask_details
* inform{"price": "cheap"}
    - slot{"price": "cheap"}
    - utter_ask_people
* correct{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_correct_price_hotel
    - utter_ask_people
* chitchat
    - utter_chitchat
    - utter_ask_people
* did_that_work
    - utter_more_info_hotel
    - utter_ask_people
* inform{"people": "4"}
    - utter_ask_startdate
* inform{"startdate": "10.03.2018"}
    - utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - utter_ask_location
* inform{"location": "paris"}
    - utter_filled_slots
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* did_that_work
    - utter_worked_hotel
    - utter_suggest_hotel
* affirm
    - utter_happy

## Generated Story -9062156691468594191
* request_hotel
    - utter_ask_details
* inform{"people": "4"}
    - slot{"people": "4"}
    - utter_ask_location
* explain
    - utter_explain_location_hotel
    - utter_ask_location
* correct{"people": "1"}
    - slot{"people": "1"}
    - utter_correct_people_hotel
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

## Generated Story 1397011895366220691
* request_hotel
    - utter_ask_details
* inform{"location": "london"}
    - slot{"location": "london"}
    - utter_ask_people
* correct{"location": "rome"}
    - slot{"location": "rome"}
    - utter_correct_location_hotel
    - utter_ask_people
* did_that_work
    - utter_more_info_hotel
    - utter_ask_people
* inform{"people": "1"}
    - slot{"people": "1"}
    - utter_ask_price
* did_that_work
    - utter_more_info_hotel
    - utter_ask_price
* did_that_work
    - utter_more_info_hotel
    - utter_ask_price
* did_that_work
    - utter_more_info_hotel
    - utter_ask_price
* explain
    - utter_explain_price_hotel
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

## Generated Story 6118400076211702408
* request_hotel
    - utter_ask_details
* inform{"startdate": "today", "location": "rome"}
    - slot{"startdate": "today"}
    - slot{"location": "rome"}
    - utter_ask_people
* inform{"people": "6"}
    - slot{"people": "6"}
    - utter_ask_price
* correct{"startdate": "next week"}
    - slot{"startdate": "next week"}
    - utter_correct_startdate_hotel
    - utter_ask_price
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_ask_enddate
* inform{"enddate": "tomorrow"}
    - slot{"enddate": "tomorrow"}
    - utter_filled_slots
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* affirm
    - utter_happy

## Generated Story -1066423376724531861
* request_hotel
    - utter_ask_details
* inform{"startdate": "today"}
    - slot{"startdate": "today"}
    - utter_ask_enddate
* explain
    - utter_explain_enddate_hotel
    - utter_ask_enddate
* correct{"startdate": "next week"}
    - slot{"startdate": "next week"}
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
* chitchat
    - utter_chitchat
    - utter_suggest_hotel
* affirm
    - utter_happy

## Generated Story 2033230819050515992
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_ask_location
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_location
* explain
    - utter_explain_location_restaurant
    - utter_ask_location
* inform{"location":"rome"}
    - utter_ask_people
* inform{"people": "1"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy


## Generated Story -4977951358594275605
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "french"}
    - slot{"cuisine": "french"}
    - utter_ask_price
* explain
    - utter_explain_price_restaurant
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


## Generated Story -1347297960370112371
* request_restaurant
    - utter_ask_details
* inform{"location": "london"}
    - slot{"location": "london"}
    - utter_ask_people
* explain
    - utter_explain_people_restaurant
    - utter_ask_people
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_people
* inform{"people": "4"}
    - slot{"people": "4"}
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
* did_that_work
    - utter_worked_restaurant
    - utter_suggest_restaurant
* did_that_work
    - utter_worked_restaurant
    - utter_suggest_restaurant
* affirm
    - utter_happy

## Generated Story -34984309837927831
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - utter_ask_location
* chitchat
    - utter_chitchat
    - utter_ask_location
* chitchat
    - utter_chitchat
    - utter_ask_location
* inform{"location": "london"}
    - slot{"location": "london"}
    - utter_ask_people
* inform{"people": "4"}
    - slot{"people": "4"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant":"results"}
    - utter_suggest_restaurant
* correct{"people": "4"}
    - slot{"people": "4"}
    - utter_correct_people_restaurant
    - action_search_restaurant
    - slot{"restaurant":"results"}
    - utter_suggest_restaurant
* correct{"location": "rome"}
    - slot{"location": "rome"}
    - utter_correct_location_restaurant
    - action_search_restaurant
    - slot{"restaurant":"results"}
    - utter_suggest_restaurant
* did_that_work
    - utter_worked_restaurant
    - utter_suggest_restaurant
* affirm
    - utter_happy

## Generated Story -5037852676024300992
* request_restaurant
    - utter_ask_details
* inform{"people": "4"}
    - slot{"people": "4"}
    - utter_ask_location
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - utter_ask_price
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_ask_cuisine
* inform{"cuisine": "french"}
    - slot{"cuisine": "french"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant":"results"}
    - utter_suggest_restaurant
* correct{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_correct_price_restaurant
    - action_search_restaurant
    - slot{"restaurant":"results"}
    - utter_suggest_restaurant


## Generated Story 8982539339425187761
* request_restaurant
    - utter_ask_details
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - utter_ask_people
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_people
* inform{"people": "6"}
    - slot{"people": "6"}
    - utter_ask_price
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_price
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_price
* explain
    - utter_explain_price_restaurant
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* inform{"cuisine": "french"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy


## Generated Story -1007374986053400669
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_price
* correct{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
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
* chitchat
    - utter_chitchat
    - utter_suggest_restaurant
* affirm
    - utter_happy


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


## Generated Story -1007374986053400669
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_price
* correct{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
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
* chitchat
    - utter_chitchat
    - utter_suggest_restaurant
* affirm
    - utter_happy


