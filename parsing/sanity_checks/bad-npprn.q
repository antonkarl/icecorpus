node: IP*

copy_corpus: t

define: def/ICE.def

query: (IP* iDoms {1}NP-PRN)
   AND (IP* idoms NP-SBJ*)
   AND (NP-SBJ* idoms !\**)
   AND (IP* iDomsMod V*|M*|R*|B* linkingVerb|*-þykja|*-gerast|*-blifa|*-blífa|*-heita)

add_leaf_before{1}: (CODE *ZZZ_MAYBE_PRD*)