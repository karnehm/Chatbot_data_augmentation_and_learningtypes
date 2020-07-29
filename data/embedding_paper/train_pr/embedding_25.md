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
    
## Generated Story -4597439819468904984
* request_restaurant
    - utter_ask_details
* inform{"people": "2", "cuisine": "french"}
    - slot{"people": "2"}
    - slot{"cuisine": "french"}
    - utter_ask_price
* inform{"price": "cheap"}
    - slot{"price": "cheap"}
    - utter_ask_location
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
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
* inform{"price": "expensive"}
    - slot{"price":"expensive"}
    - utter_ask_cuisine
* inform{"cuisine": "french"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* affirm
    - utter_happy


## Generated Story 2120810106318217739
* request_hotel
    - utter_ask_details
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - utter_ask_people
* did_that_work
    - utter_more_info_hotel
    - utter_ask_people
* chitchat
    - utter_chitchat
    - utter_ask_people
* correct{"location": "paris"}
    - slot{"location": "paris"}
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
* did_that_work
    - utter_worked_hotel
    - utter_suggest_hotel
* did_that_work
    - utter_worked_hotel
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

## Generated Story 2628958171188267867
* request_hotel
    - utter_ask_details
* inform{"location": "paris"}
    - slot{"location": "paris"}
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
* did_that_work
    - utter_worked_hotel
    - utter_suggest_hotel
* affirm
        - utter_happy

## Generated Story 1685090242406500402
* request_hotel
    - utter_ask_details
* inform{"startdate": "next week"}
    - slot{"startdate": "next week"}
    - utter_ask_enddate
* inform{"enddate": "tomorrow"}
    - slot{"enddate": "tomorrow"}
    - utter_ask_price
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_ask_location
* correct{"enddate": "next week"}
    - slot{"enddate": "next week"}
    - utter_correct_enddate_hotel
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
* did_that_work
    - utter_worked_hotel
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

## Generated Story -417820108794993882
* request_hotel
    - utter_ask_details
* inform{"location": "london"}
    - slot{"location": "london"}
    - utter_ask_people
* inform{"people": "4"}
    - slot{"people": "4"}
    - utter_ask_price
* correct{"location": "london"}
    - slot{"location": "london"}
    - utter_correct_location_hotel
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

## Generated Story 8569607195157226943
* request_hotel
    - utter_ask_details
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_ask_people
* inform{"people": "4"}
    - slot{"people": "4"}
    - utter_ask_startdate
* chitchat
    - utter_chitchat
    - utter_ask_startdate
* correct{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_correct_price_hotel
    - utter_ask_startdate
* chitchat
    - utter_chitchat
    - utter_ask_startdate
* chitchat
    - utter_chitchat
    - utter_ask_startdate
* inform{"startdate": "next week"}
    - slot{"startdate": "next week"}
    - utter_ask_enddate
* correct{"price": "mid-range"}
    - slot{"price": "mid-range"}
    - utter_correct_price_hotel
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

## Generated Story -1976434779256682036
* request_hotel
    - utter_ask_details
* inform{"location": "paris"}
    - slot{"location": "paris"}
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
* did_that_work
    - utter_worked_hotel
    - utter_suggest_hotel
* did_that_work
    - utter_worked_hotel
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

## Generated Story -4892544019489261987
* request_hotel
    - utter_ask_details
* inform{"people": "2"}
    - slot{"people": "2"}
    - utter_ask_location
* explain
    - utter_explain_location_hotel
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
* did_that_work
    - utter_worked_hotel
    - utter_suggest_hotel
* did_that_work
    - utter_worked_hotel
    - utter_suggest_hotel
* did_that_work
    - utter_worked_hotel
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

## Generated Story -984969290790501507
* request_hotel
    - utter_ask_details
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - utter_ask_people
* chitchat
    - utter_chitchat
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

## Generated Story -248636324534589386
* request_hotel
    - utter_ask_details
* inform{"location": "rome"}
    - slot{"location": "rome"}
    - utter_ask_people
* explain
    - utter_explain_people_hotel
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

## Generated Story 3166112699919947742
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* explain
    - utter_explain_price_restaurant
    - utter_ask_price
* inform{"price": "expensive"}
    - slot{"price": "expensive"}
    - utter_ask_location
* inform{"location": "paris"}
    - slot{"location": "paris"}
    - utter_ask_people
* did_that_work
    - utter_more_info_restaurant
    - utter_ask_people
* explain
    - utter_explain_people_restaurant
    - utter_ask_people
* inform{"people": "4"}
    - utter_filled_slots
    - action_search_restaurant
    - slot{"restaurant": "restaurant"}
    - utter_suggest_restaurant
* did_that_work
    - utter_worked_restaurant
    - utter_suggest_restaurant
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

## Generated Story -1455208811812364750
* request_restaurant
    - utter_ask_details
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* explain
    - utter_explain_price_restaurant
    - utter_ask_price
* inform{"price": "mid-range"}
    - slot{"price": "mid-range"}
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

## Generated Story 1873242173921385874
* request_hotel
    - utter_ask_details
* inform{"location": "london"}
    - slot{"location": "london"}
    - utter_ask_people
* correct{"location": "rome"}
    - slot{"location": "rome"}
    - utter_correct_location_hotel
    - utter_ask_people
* correct{"location": "paris"}
    - slot{"location": "paris"}
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
    