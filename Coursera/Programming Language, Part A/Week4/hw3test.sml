(* Homework3 Simple Test *)
(* These are basic test cases. Passing these tests does not guarantee that your code will pass the actual homework grader *)
(* To run the test, add a new line to the top of this file: use "homeworkname.sml"; *)
(* All the tests should evaluate to true. For example, the REPL should say: val test1 = true : bool *)

use "hw3solution.sml";

val test1 = only_capitals ["A","B","C"] = ["A","B","C"]

val test2 = longest_string1 ["A","bc", "ba", "C"] = "bc"

val test3 = longest_string2 ["A","bc", "ba", "C"] = "ba"

val test4a = longest_string3 ["A","bc","C"] = "bc"

val test4b = longest_string4 ["A","B","C"] = "C"

val test5 = longest_capitalized ["A","bc","C"] = "A"

val test6 = rev_string "abc" = "cba"

val test7 = first_answer (fn x => if x > 3 then SOME x else NONE) [1,2,3,4,5] = 4

val test8 = all_answers (fn x => if x = 1 then SOME [x] else NONE) [2,3,4,5,6,7] = NONE

val test9a = count_wildcards Wildcard = 1

val test9b = count_wild_and_variable_lengths (Variable("a")) = 1

val test9c = count_some_var ("x", Variable("x")) = 1
val test9c_1 = count_some_var ("Wild",ConstructorP ("wild",Wildcard)) = 0
val test9c_2 = count_some_var ("x",TupleP[Wildcard,ConstP 17,Variable "x",UnitP,TupleP[UnitP,UnitP,UnitP],ConstructorP ("",UnitP),TupleP[],ConstructorP ("wild",Wildcard),TupleP[Wildcard,ConstP 17,Variable "x",UnitP,TupleP[UnitP,UnitP,UnitP],ConstructorP ("",UnitP),TupleP[],ConstructorP ("wild",Wildcard)]]) = 2
val test9c_3 = count_some_var ("y",TupleP[Wildcard,ConstP 17,Variable "x",UnitP,TupleP[UnitP,UnitP,UnitP],ConstructorP ("",UnitP),TupleP[],ConstructorP ("wild",Wildcard),TupleP[Wildcard,ConstP 17,Variable "x",UnitP,TupleP[UnitP,UnitP,UnitP],ConstructorP ("",UnitP),TupleP[],ConstructorP ("wild",Wildcard)]]) = 0

val test10 = check_pat (Variable("x")) = true
val test10_1 = check_pat (TupleP[Variable "x",Variable "x"]) = false
val test10_2 = check_pat (TupleP[TupleP[Variable "x",ConstructorP ("wild",Wildcard)],Variable "x"]) = false
val test10_3 = check_pat (ConstructorP ("hi",TupleP[Variable "x",Variable "x"])) = false

val test11 = match (Const(1), UnitP) = NONE

val test12 = first_match Unit [UnitP] = SOME []
