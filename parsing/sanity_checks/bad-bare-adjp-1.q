node: IP*

copy_corpus: t

define: def/ICE.def

query: (IP* iDoms {1}ADJP)
   AND (IP* iDoms finiteVerb)
   AND (IP* iDoms !B*|R*)
   AND (IP* iDomsMod V*|M*|R* !linkingVerb|þyk*|gerast|gerist|blif*|blíf*|heit*|hét*)

add_leaf_before{1}: (CODE *ZZZ_BARE_ADJP*)