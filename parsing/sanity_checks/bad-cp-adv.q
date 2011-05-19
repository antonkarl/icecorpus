node: $ROOT

copy_corpus: t

define: def/ICE.def

query: ({1}CP-ADV* exists) AND (!IP*|PP*|$ROOT|CONJP*|CP-ADV* idoms CP-ADV*)

add_leaf_before{1}: (CODE *ZZZ_BADCPADV_MAY_BE_REL*)
