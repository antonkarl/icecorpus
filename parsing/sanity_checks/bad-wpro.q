node: $ROOT

copy_corpus: t

query: (WNP* idoms {1}WPRO*|PRO*) AND (WPRO*|PRO* idoms hv*) AND (WNP* idomstotal> 1) AND (WNP* idoms !ADV*|Q*|*-PRN*)

add_leaf_before{1}: (CODE *ZZZ_BADWPRO_WD_OR_WADV*)
