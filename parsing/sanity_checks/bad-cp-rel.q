node: $ROOT

copy_corpus: t

define: def/ICE.def

query: ({1}[1]CP-REL|CP-DEG|CP-DEG-SPE|CP-REL-SPE exists) AND (IP*|PP*|$ROOT idoms [1]CP-REL|CP-DEG|CP-DEG-SPE|CP-REL-SPE)

add_leaf_before{1}: (CODE *ZZZ_BADCPREL_MAY_BE_ADV*)
