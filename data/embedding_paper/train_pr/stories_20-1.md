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

## restaurant happy 2
* request_restaurant
    - utter_ask_details
* inform{"people": "4"}
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


## Generated Story 460877518176879910
* request_hotel
    - utter_ask_details
* inform{"startdate": "today"}
    - slot{"startdate": "today"}
    - utter_ask_enddate
* did_that_work
    - utter_more_info_hotel
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


## Generated Story 6126634125194604292
* request_hotel
    - utter_ask_details
* inform{"people": "6"}
    - slot{"people": "6"}
    - utter_ask_location
* chitchat
    - utter_chitchat
    - utter_ask_location
* inform{"location": "rome"}
    - slot{"location": "rome"}
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
* did_that_work
    - utter_worked_hotel
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

## Generated Story -3019312067209215162
* request_hotel
    - utter_ask_details
* inform{"startdate": "May 25th"}
    - slot{"startdate": "May 25th"}
    - utter_ask_enddate
* inform{"enddate": "tomorrow"}
    - slot{"enddate": "tomorrow"}
    - utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - utter_ask_location
* did_that_work
    - utter_more_info_hotel
    - utter_ask_location
* explain
    - utter_explain_location_hotel
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

## Generated Story 6126634125194604292
* request_hotel
    - utter_ask_details
* inform{"people": "6"}
    - slot{"people": "6"}
    - utter_ask_location
* chitchat
    - utter_chitchat
    - utter_ask_location
* inform{"location": "rome"}
    - slot{"location": "rome"}
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

## Generated Story 8798487188356031983
* request_hotel
    - utter_ask_details
* inform{"people": "4"}
    - slot{"people": "4"}
    - utter_ask_location
* correct{"people": "2"}
    - slot{"people": "2"}
    - utter_correct_people_hotel
    - utter_ask_location
* chitchat
    - utter_chitchat
    - utter_ask_location
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - utter_ask_startdate
* inform{"startdate": "next week", "enddate": "tomorrow"}
    - slot{"startdate": "next week"}
    - slot{"enddate": "tomorrow"}
    - utter_filled_slots
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* correct{"enddate": "May 26th"}
    - slot{"enddate": "May 26th"}
    - utter_correct_enddate_hotel
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* correct{"location": "rome"}
    - slot{"location": "rome"}
    - utter_correct_location_hotel
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* did_that_work
    - utter_worked_hotel
    - utter_suggest_hotel
* affirm
    - utter_happy

## Generated Story 6377256771280559561
* request_hotel
    - utter_ask_details
* inform{"price": "mid-range", "enddate": "next week"}
    - slot{"price": "mid-range"}
    - slot{"enddate": "next week"}
    - utter_ask_startdate
* explain
    - utter_explain_startdate_hotel
    - utter_ask_startdate
* did_that_work
    - utter_more_info_hotel
    - utter_ask_startdate
* correct{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_correct_price_hotel
    - utter_ask_startdate
* chitchat
    - utter_chitchat
    - utter_ask_startdate
* did_that_work
    - utter_more_info_hotel
    - utter_ask_startdate
* chitchat
    - utter_chitchat
    - utter_ask_startdate
* explain
    - utter_explain_startdate_hotel
    - utter_ask_startdate
* inform{"startdate": "tomorrow"}
    - slot{"startdate": "tomorrow"}
    - utter_ask_location
* inform{"location": "london"}
    - slot{"location": "london"}
    - utter_ask_people
* inform{"people": "4"}
    - slot{"people": "4"}
    - utter_filled_slots
    - action_search_hotel
    - slot{"hotel": "hotel"}
    - utter_suggest_hotel
* affirm
    - utter_happy

## Generated Story 965944888666945465
* request_hotel
    - utter_ask_details
* inform{"enddate": "next week"}
    - slot{"enddate": "next week"}
    - utter_ask_startdate
* chitchat
    - utter_chitchat
    - utter_ask_startdate
* did_that_work
    - utter_more_info_hotel
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

## Generated Story 8731682222915754367
* request_hotel
    - utter_ask_details
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
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
* chitchat
    - utter_chitchat
    - utter_ask_people
* chitchat
    - utter_chitchat
    - utter_ask_people
* chitchat
    - utter_chitchat
    - utter_ask_people
* chitchat
    - utter_chitchat
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

## Generated Story 769607181822342811
* request_hotel
    - utter_ask_details
* inform{"people": "2"}
    - slot{"people": "2"}
    - utter_ask_location
* chitchat
    - utter_chitchat
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

## Generated Story -7342525516064688202
* request_hotel
    - utter_ask_details
* inform{"people": "2"}
    - slot{"people": "2"}
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

## Generated Story -2820988936373814771
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "french"}
    - slot{"cuisine": "french"}
    - utter_ask_price
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - utter_ask_location
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_location
* chitchat
    - utter_chitchat
    - utter_ask_location
* chitchat
    - utter_chitchat
    - utter_ask_location
* chitchat
    - utter_chitchat
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


## Generated Story 4951610683748594432
* request_restaurant
    - utter_ask_details
* inform{"people": "6"}
    - slot{"people": "6"}
    - utter_ask_location
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - utter_ask_price
* chitchat
    - utter_chitchat
    - utter_ask_price
* explain
    - utter_explain_price_restaurant
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
* affirm
    - utter_happy

## Generated Story 4951610683748594432
* request_restaurant
    - utter_ask_details
* inform{"people": "6"}
    - slot{"people": "6"}
    - utter_ask_location
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - utter_ask_price
* chitchat
    - utter_chitchat
    - utter_ask_price
* explain
    - utter_explain_price_restaurant
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


## Generated Story -6924676699065688022
* request_restaurant
    - utter_ask_details
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_ask_people
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_people
* correct{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_correct_price_restaurant
    - utter_ask_people
* inform{"people": "2"}
    - slot{"people": "2"}
    - utter_ask_location
* inform{"location": "paris"}
    - slot{"location": "paris"}
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

## Generated Story 8482744598176193653
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "french"}
    - slot{"cuisine": "french"}
    - utter_ask_price
* explain
    - utter_explain_price_restaurant
    - utter_ask_price
* explain
    - utter_explain_price_restaurant
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

## Generated Story -4390789948531939425
* request_restaurant
    - utter_ask_details
* inform{"people": "1"}
    - slot{"people": "1"}
    - utter_ask_location
* inform{"location": "london"}
    - slot{"location": "london"}
    - utter_ask_price
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - utter_ask_cuisine
* correct{"people": "4"}
    - slot{"people": "4"}
    - utter_correct_people_restaurant
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy


## Generated Story 5030307886271057142
* request_restaurant
    - utter_ask_details
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - utter_ask_people
* explain
    - utter_explain_people_restaurant
    - utter_ask_people
* correct{"location": "paris"}
    - slot{"location": "paris"}
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


