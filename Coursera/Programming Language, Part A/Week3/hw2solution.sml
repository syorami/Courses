(* Dan Grossman, Coursera PL, HW2 Provided Code *)

(* if you use this function to compare two strings (returns true if the same
   string), then you avoid several of the functions in problem 1 having
   polymorphic types that may be confusing *)
fun same_string(s1 : string, s2 : string) =
    s1 = s2

(* put your solutions for problem 1 here *)
fun all_except_option (x, ys) =
	let
		fun iter_compare (ys) =
			case ys of
				[] => []
				| y::ys' => if same_string(x, y) 
							then iter_compare(ys') 
							else y::iter_compare(ys')
		val return = iter_compare(ys)
	in
		if return = ys then NONE else SOME(return)
	end

fun get_substitutions1 (xss, y) =
	case xss of
		[] => []
		| xs::xss' => case all_except_option(y, xs) of
						NONE => get_substitutions1(xss', y)
						| SOME xs' => xs' @ get_substitutions1(xss', y)

fun get_substitutions2 (xss, y) =
	let
		fun helper (xss, res) =
			case xss of
				[] => res
				| xs::xss' => case all_except_option(y, xs) of
								NONE => helper(xss', res)
								| SOME xs' => helper(xss', res @ xs')
	in
		helper(xss, [])
	end

fun similar_names (xss, r) =
	let
		val {first=f, last=l, middle=m} = r
		fun helper (xs) =
			case xs of
				[] => []
				| x::xs' => {first=x, last=l, middle=m}::helper(xs')
	in
		r::helper(get_substitutions2(xss, f))
	end

(* you may assume that Num is always used with values 2, 3, ..., 10
   though it will not really come up *)
datatype suit = Clubs | Diamonds | Hearts | Spades
datatype rank = Jack | Queen | King | Ace | Num of int 
type card = suit * rank

datatype color = Red | Black
datatype move = Discard of card | Draw 

exception IllegalMove

(* put your solutions for problem 2 here *)
fun card_color (c) =
	case c of
		(Clubs, _) => Black
		| (Diamonds, _) => Red
		| (Hearts, _) => Red
		| (Spades, _) => Black

fun card_value (c) =
	case c of
		(_, Num n) => n
		| (_, Ace) => 11
		| (_, _) => 10

fun remove_card (cs, c: card, e) =
	case cs of
		[] => raise e
		| c'::cs' => if c' = c then cs' else c'::remove_card(cs', c, e)

fun all_same_color (cs) =
	case cs of
		[] => true
		| _::[] => true
		| c::c'::cs' => (card_color(c) = card_color(c')) andalso all_same_color(c'::cs')

fun sum_cards (cs) =
	let
		fun helper (cs, sum) =
			case cs of
				[] => sum
				| c::cs' => helper(cs', sum + card_value(c))
	in
		helper(cs, 0)
	end

fun score (cs, goal) =
	let
		val sum = sum_cards(cs)
		val prelimiary = if sum > goal then 3 * (sum - goal) else goal - sum
	in
		if all_same_color(cs) then prelimiary div 2 else prelimiary
	end

fun officiate (cards, moves, goal) =
	let
		fun helper (cards, helds, moves) =
			case moves of
				[] => score(helds, goal)
				| Draw::moves' => (case cards of
									[] => score(helds, goal)
									| card::cards' => if sum_cards(card::helds) > goal
														then score(card::helds, goal)
														else helper(cards', card::helds, moves'))
				| (Discard card)::moves' => helper(cards, remove_card(helds, card, IllegalMove), moves')
	in
		helper(cards, [], moves)
	end

(* solutions for challenge *)
fun possible_sums (cs) =
	let
		fun ace_num (cs) =
			case cs of
				[] => 0
				| (_, Ace)::cs' => 1 + ace_num(cs')
				| _::cs' => ace_num(cs')
		fun combs (num, sum, lists) =
			case num of
				0 => lists
				| _ => combs(num - 1, sum - 10, (sum - 10)::lists)
	in
		combs(ace_num(cs), sum_cards(cs), [sum_cards(cs)])
	end

fun score_challenge (cs, goal) =
	let
		val sums = possible_sums(cs)
		val same_color = all_same_color(cs)
		fun mini_score (same_color, sum, goal) =
			let
				val prelimiary = if sum > goal then 3 * (sum - goal) else goal - sum
			in
				if same_color then prelimiary div 2 else prelimiary
			end
		fun helper (sums, min) =
			case sums of
				[] => min
				| sum::sums' => helper(sums', Int.min(mini_score(same_color, sum, goal), min))
	in
		helper(sums, score(cs, goal))
	end

fun officiate_challenge (cards, moves, goal) =
	let
		fun helper (cards, helds, moves) =
			case moves of
				[] => score_challenge(helds, goal)
				| Draw::moves' => (case cards of
									[] => score_challenge(helds, goal)
									| card::cards' => if sum_cards(card::helds) > goal
														then score_challenge(card::helds, goal)
														else helper(cards', card::helds, moves'))
				| (Discard card)::moves' => helper(cards, remove_card(helds, card, IllegalMove), moves')
	in
		helper(cards, [], moves)
	end
