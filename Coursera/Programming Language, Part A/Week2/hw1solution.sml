fun is_older (d1: int * int * int, d2: int * int * int) =
	if not (#1 d1 = #1 d2)
	then #1 d1 < #1 d2
	else if not (#2 d1 = #2 d2)
	then #2 d1 < #2 d2
	else #3 d1 < #3 d2

fun number_in_month (dates: (int * int * int) list, month: int) =
	if null dates
	then 0
	else let
		val num = number_in_month (tl dates, month)
	in
		if (#2 (hd dates)) = month then num + 1 else num
	end

fun number_in_months (dates: (int * int * int) list, months: int list) =
	if null months
	then 0
	else let 
		val num = number_in_month (dates, hd months)
	in
		num + number_in_months (dates, tl months)
	end

fun dates_in_month (dates: (int * int * int) list, month: int) =
	if null dates
	then []
	else let
		val lists = dates_in_month(tl dates, month)
	in
		if (#2 (hd dates)) = month then (hd dates) :: lists else lists
	end

fun dates_in_months (dates: (int * int * int) list, months: int list) =
    if null months
    then []
    else dates_in_month(dates, hd months) @ dates_in_months(dates, tl months)

fun get_nth (strings: string list, n: int) =
	if n = 1
	then hd strings
	else get_nth (tl strings, n - 1)

fun date_to_string (date: (int * int * int)) =
	let
		val month_lists = ["January", "February", "March", "April", "May",
						"June", "July", "August", "September", "October",
						"November", "December"]
		val month = get_nth (month_lists, #2 date)
	in
		month ^ " " ^ Int.toString(#3 date) ^ ", " ^ Int.toString(#1 date)
	end

fun number_before_reaching_sum (sum: int, lists: int list) =
	if sum <= hd lists 
	then 0
	else 1 + number_before_reaching_sum (sum - hd lists, tl lists)

fun what_month (day: int) =
	let
		val days_cnt = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	in
		number_before_reaching_sum (day, days_cnt) + 1
	end

fun month_range (day1: int, day2: int) =
	if day1 > day2
	then []
	else what_month(day1)::month_range(day1 + 1, day2)

fun oldest (dates: (int * int * int) list) =
	if null dates
	then NONE
	else let
		val tl_oldest = oldest(tl dates)
	in
		if isSome tl_oldest andalso is_older (valOf tl_oldest, hd dates)
		then tl_oldest
		else SOME (hd dates)
	end

fun in_list (item: int, lists: int list) =
	not (null lists) andalso (item = hd lists orelse in_list(item, tl lists))

fun rm_dup (lists: int list) =
	if null lists
	then []
	else
		let
			val tl_lists = rm_dup (tl lists)
		in
			if in_list (hd lists, tl_lists)
			then tl_lists
			else (hd lists) :: tl_lists
		end

fun number_in_months_challenge (dates: (int * int * int) list, months: int list) =
	number_in_months(dates, rm_dup(months))

fun dates_in_months_challenge (dates: (int * int * int) list, months: int list) =
	dates_in_months(dates, rm_dup(months))

fun reasonable_date (date: int * int * int) =
	let
		fun return_nth (n: int, lists: int list) =
			if n = 1 then hd lists else return_nth(n - 1, tl lists)

		val year = #1 date
		val month = #2 date
		val day = #3 date
		val is_leap = (year mod 400 = 0) orelse (year mod 4 = 0 andalso year mod 100 <> 0)
		val cnt = if is_leap then 29 else 28
		val days_cnt = [31, cnt, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

		val year_valid = year > 0
		val month_valid = month >= 1 andalso month <= 12
		val days_valid = month_valid andalso day >= 1 andalso day <= return_nth(month, days_cnt)
	in
		year_valid andalso month_valid andalso days_valid
	end