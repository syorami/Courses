fun is_older (date1 : int*int*int, date2 : int*int*int) =
    if (#1 date1) < (#1 date2) then true
    else if (#1 date1) > (#1 date2) then false
    else if (#2 date1) < (#2 date2) then true
    else if (#2 date1) > (#2 date2) then false
    else if (#3 date1) < (#3 date2) then true
    else false

fun number_in_month (dates : (int * int * int) list, month : int) =
    if null dates
    then 0
    else if #2 (hd dates) <> month
    then number_in_month(tl dates, month)
    else 1 + number_in_month(tl dates, month)
	
fun number_in_months (dates : (int * int * int) list, months : int list) =
    if null months
    then 0
    else if number_in_month(dates, hd months) > 0
    then 1 + number_in_months(dates, tl months)
    else  number_in_months(dates, tl months)

fun dates_in_month (dates : (int * int * int) list, month : int) =
    if null dates
    then []
    else if #2 (hd dates) = month
    then (hd dates) :: dates_in_month(tl dates, month)
    else dates_in_month(tl dates, month)
		       
fun dates_in_months (dates : (int * int * int) list, months : int list) =
    if null months
    then []
    else dates_in_month(dates, hd months) @ dates_in_months(dates, tl months)

fun get_nth (l_str : string list, n : int) = 
    if n = 1
    then hd l_str
    else get_nth(tl l_str, n-1)

fun date_to_string (date : int * int * int) =
    let val months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    in
	get_nth(months, #2 date) ^ " " ^ Int.toString(#3 date) ^ ", " ^ Int.toString(#1 date)								    
    end
	
fun number_before_reaching_sum (sum : int, int_l : int list) =
    if sum > hd int_l
    then 1 + number_before_reaching_sum(sum - hd int_l, tl int_l)
    else 0
	
fun what_month (day_of_year : int) =
    let val days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    in
	1 + number_before_reaching_sum (day_of_year, days_in_months)							    
    end

fun month_range (day1 : int, day2 : int) =
    if day1 > day2
    then []
    else what_month(day1) :: month_range(day1 + 1, day2)

fun oldest (dates : (int * int * int) list) =
    if null dates
    then NONE
    else
	let val tl_ans = oldest(tl dates)
	in if isSome tl_ans andalso is_older(valOf tl_ans, hd dates)
	   then tl_ans
	   else SOME (hd dates)
	end
	    	      
