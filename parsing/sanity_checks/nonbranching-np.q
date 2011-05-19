node: NP*

copy_corpus: t

// define: EME.def

query: (!NP-ADV* iDoms [2]NP)
   AND ([1]NP* iDoms [2]{1}NP)
   AND ([1]NP* iDoms !CONJP*)
   AND ([2]NP idoms !\*T*|\*ICH*)
   AND ([1]NP* idoms !OTHER*)

add_leaf_before{1}: (CODE *ZZZ_NONBRANCH*)
