
node: $ROOT

copy_corpus: t

query: (!IP*|VP|RRC*|FRAG iDoms {1}*-SBJ*|*-OB[12]*)

add_leaf_before{1}: (CODE *ZZZ_BAD_ARG*)
