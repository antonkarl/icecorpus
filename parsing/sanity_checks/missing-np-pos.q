node: $ROOT

copy_corpus: t

query: (!NP-POS* iDoms {1}PRO*) AND (PRO* iDoms *-minn|*-þinn|*-sinn|*-vor)

append_label{1}: -ZZZ-MISS_NPPOS
