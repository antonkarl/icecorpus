node: $ROOT

copy_corpus: t

query: (!NP-PRN* idoms {1}PRO*) AND (PRO* idoms *-sjálfur)

append_label{1}: -ZZZ
