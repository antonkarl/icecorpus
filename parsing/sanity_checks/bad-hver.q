node: $ROOT

copy_corpus: t

query: (!WNP* idoms {1}WPRO*|PRO*) AND ({1}WPRO*|PRO* idoms hver*|HVER*|Hver*)

append_label{1}: -ZZZ-BADHVER-Q