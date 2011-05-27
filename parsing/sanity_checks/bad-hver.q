node: $ROOT

copy_corpus: t

query: (!WNP* idoms {1}WPRO*|PRO*) AND ({1}WPRO*|PRO* idoms hver*|HVER*|Hver*)

add_leaf_before{1}: (CODE *ZZZ_BADHVER_Q*)