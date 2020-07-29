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

## Generated Story -7795096423415267175
* request_hotel
    - utter_ask_details
* inform{"people": "1", "location": "rome"}
    - slot{"people": "1"}
    - slot{"location": "rome"}
    - utter_ask_price
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_ask_startdate
* inform{"startdate": "May 25th"}
    - slot{"startdate": "May 25th"}
    - utter_ask_enddate
* inform{"enddate": "10.03.2018"}
    - utter_filled_slots
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* affirm
    - utter_happy

## restaurant happy 4
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "italian"}
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

## Generated Story 876333698881437444
* request_hotel
    - utter_ask_details
* inform{"enddate": "tomorrow"}
    - slot{"enddate": "tomorrow"}
    - utter_ask_startdate
* correct{"enddate": "tomorrow"}
    - slot{"enddate": "tomorrow"}
    - utter_correct_enddate_hotel
    - utter_ask_startdate
* correct{"enddate": "next week"}
    - slot{"enddate": "next week"}
    - utter_correct_enddate_hotel
    - utter_ask_startdate
* correct{"enddate": "next week"}
    - slot{"enddate": "next week"}
    - utter_correct_enddate_hotel
    - utter_ask_startdate
* chitchat
    - utter_chitchat
    - utter_ask_startdate
* inform{"startdate": "today"}
    - slot{"startdate": "today"}
    - utter_ask_location
* explain
    - utter_explain_location_hotel
    - utter_ask_location
* chitchat
    - utter_chitchat
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

## Generated Story 215722250464778445
* request_hotel
    - utter_ask_details
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - utter_ask_people
* correct{"location": "paris"}
    - slot{"location": "paris"}
    - utter_correct_location_hotel
    - utter_ask_people
* inform{"people": "4"}
    - slot{"people": "4"}
    - utter_ask_price
* explain
    - utter_explain_price_hotel
    - utter_ask_price
* chitchat
    - utter_chitchat
    - utter_ask_price
* did_that_work
    - utter_more_info_hotel
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

## Generated Story -7610825832938952225
* request_hotel
    - utter_ask_details
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - utter_ask_people
* correct{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_correct_price_hotel
    - utter_ask_people
* chitchat
    - utter_chitchat
    - utter_ask_people
* explain
    - utter_explain_people_hotel
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

## Generated Story -5728975931820977598
* request_hotel
    - utter_ask_details
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_ask_people
* inform{"people": "4"}
    - slot{"people": "4"}
    - utter_ask_startdate
* inform{"startdate": "today"}
    - slot{"startdate": "today"}
    - utter_ask_enddate
* inform{"enddate": "next week"}
    - slot{"enddate": "next week"}
    - utter_ask_location
* did_that_work
    - utter_more_info_hotel
    - utter_ask_location
* chitchat
    - utter_chitchat
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

## Generated Story 8246622124448048208
* request_hotel
    - utter_ask_details
* inform{"people": "4"}
    - slot{"people": "4"}
    - utter_ask_location
* explain
    - utter_explain_location_hotel
    - utter_ask_location
* correct{"people": "4"}
    - slot{"people": "4"}
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

## Generated Story 8415484272864759934
* request_restaurant
    - utter_ask_details
* inform{"people": "1"}
    - slot{"people": "1"}
    - utter_ask_location
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - utter_ask_price
* chitchat
    - utter_chitchat
    - utter_ask_price
* chitchat
    - utter_chitchat
    - utter_ask_price
* correct{"people": "1"}
    - slot{"people": "1"}
    - utter_correct_people_restaurant
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
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
* affirm
    - utter_happy


## Generated Story 3679034546170012421
* request_restaurant
    - utter_ask_details
* inform{"price": "cheap"}
    - slot{"price": "cheap"}
    - utter_ask_people
* inform{"people": "2"}
    - slot{"people": "2"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* explain
    - utter_explain_location_restaurant
    - utter_ask_location
* chitchat
    - utter_chitchat
    - utter_ask_location
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_location
* correct{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_correct_cuisine_restaurant
    - utter_ask_location
* inform{"location": "london"}
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


## Generated Story -5272153381260553507
* request_restaurant
    - utter_ask_details
* inform{"people": "6"}
    - slot{"people": "6"}
    - utter_ask_location
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_location
* explain
    - utter_explain_location_restaurant
    - utter_ask_location
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - utter_ask_price
* inform{"price": "expensive"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
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
* affirm
    - utter_happy


## Generated Story -3230699913544241199
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "french"}
    - slot{"cuisine": "french"}
    - utter_ask_price
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_ask_location
* chitchat
    - utter_chitchat
    - utter_ask_location
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_location
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_location
* correct{"price": "expensive"}
    - slot{"price": "expensive"}
    - utter_correct_price_restaurant
    - utter_ask_location
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - utter_ask_people
* inform{"people": "2"}
    - slot{"people": "2"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* did_that_work
    - utter_worked_restaurant
    - utter_suggest_restaurant
* affirm
    - utter_happy


## Generated Story 4436622233732960065
* request_restaurant
    - utter_ask_details
* inform{"price": "cheap"}
    - slot{"price": "cheap"}
    - utter_ask_people
* correct{"price": "cheap"}
    - slot{"price": "cheap"}
    - utter_correct_price_restaurant
    - utter_ask_people
* inform{"people": "1"}
    - slot{"people": "1"}
    - utter_ask_cuisine
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_cuisine
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_cuisine
* chitchat
    - utter_chitchat
    - utter_ask_cuisine
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_cuisine
* correct{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_correct_price_restaurant
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "rome"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* chitchat
    - utter_chitchat
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
* explain
    - utter_explain_location_restaurant
    - utter_ask_location
* explain
    - utter_explain_location_restaurant
    - utter_ask_location
* inform{"location": "paris"}
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


