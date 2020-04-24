(* Coursera Programming Languages, Homework 3, Provided Code *)

exception NoAnswer

datatype pattern = Wildcard
		 | Variable of string
		 | UnitP
		 | ConstP of int
		 | TupleP of pattern list
		 | ConstructorP of string * pattern

datatype valu = Const of int
	      | Unit
	      | Tuple of valu list
	      | Constructor of string * valu

fun g f1 f2 p =
	let 
		val r = g f1 f2 
	in
		case p of
			Wildcard          	=> f1 ()
		  | Variable x        => f2 x
		  | TupleP ps         => List.foldl (fn (p,i) => (r p) + i) 0 ps
		  | ConstructorP(_,p) => r p
		  | _                 => 0
	end

(**** for the challenge problem only ****)

datatype typ = Anything
	     | UnitT
	     | IntT
	     | TupleT of typ list
	     | Datatype of string

(**** you can put all your code here ****)

(* Problem 1 *)
fun only_capitals strs =
    List.filter (fn s => Char.isUpper (String.sub(s, 0))) strs

(* Problem 2 *)
fun longest_string1 strs =
	foldl (fn (x, acc) => if size x > size acc then x else acc) "" strs

(* Problem 3 *)
fun longest_string2 strs =
	foldl (fn (x, acc) => if size x >= size acc then x else acc) "" strs

(* Problem 4 *)
fun longest_string_helper f =
	foldl (fn (x, acc) => if f(size x, size acc) then x else acc) ""

val longest_string3 = longest_string_helper (fn (x1, x2) => x1 > x2) 
val longest_string4 = longest_string_helper (fn (x1, x2) => x1 >= x2)

(* Problem 5 *)
val longest_capitalized = longest_string3 o only_capitals

(* Problem 6 *)
val rev_string = String.implode o rev o String.explode

(* Problem 7 *)
fun first_answer f xs =
	case xs of
		[] => raise NoAnswer
		| x::xs' => case f x of
									SOME v => v
									| NONE => first_answer f xs'

(* Problem 8 *)
fun all_answers f xs =
	let
		fun helper f acc xs =
			case xs of
				[] => acc
				| x::xs' => case f x of
							NONE => NONE
							| SOME lstn => helper f (SOME (lstn @ valOf acc)) xs'
	in
		helper f (SOME []) xs
	end

(* Problem 9 *)
val count_wildcards = g (fn _ => 1) (fn _ => 0)
val count_wild_and_variable_lengths = g (fn _ => 1) size

fun count_some_var (s, p) =
	g (fn _ => 0) (fn x => if x = s then 1 else 0) p

(* Problem 10 *)
fun check_pat p =
	let
		fun get_all_var p =
			case p of
				Variable s => [s]
				| ConstructorP(_,p') => get_all_var p'
				| TupleP ps => foldl (fn (x, acc) => (get_all_var x) @ acc) [] ps
				| _ => []

		fun is_duplicate xs =
			case xs of
				[] => false
				| x::xs' => List.exists (fn e: string => e = x) xs' orelse is_duplicate xs'
	in
		(not o is_duplicate o get_all_var) p
	end

(* Problem 11 *)
fun match tuple =
	case tuple of
		(_, Wildcard) => SOME []
		| (v, Variable p) => SOME [(p, v)]
		| (Unit, UnitP) => SOME []
		| (Const v, ConstP p) => if v = p then SOME [] else NONE
		| (Tuple vs, TupleP ps) => if List.length vs = List.length ps
									then (all_answers match (ListPair.zip(vs, ps)))
									else NONE
		| (Constructor (s1, v), ConstructorP (s2, p)) => if s1 = s2 then match (v, p) else NONE
		| _ => NONE

(* Problem 12 *)
fun first_match v ps =
    (SOME (first_answer (fn p => match (v, p)) ps)) handle NoAnswer => NONE
