node: $ROOT

copy_corpus: t

query: (!NP-POS* iDoms {1}PRO*) AND (PRO* iDoms *-minn|*-þinn|*-sinn|*-vor)

add_leaf_before{1}: (CODE *ZZZ_MISS_NPPOS*)
