node: $ROOT

copy_corpus: t

query: (WNP* idoms {1}WPRO*|PRO*) AND (WPRO*|PRO* idoms hv*) AND (WNP* idomstotal> 1) AND (WNP* idoms !ADV*|Q*)

append_label{1}: -ZZZ-BADWPRO-WD-OR-WADV
