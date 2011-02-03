copy_corpus:t

define: def/ICE.def
node:IP*
query: (IP* idoms [1]{1}BEP*|VBP*) AND ([1]BEP*|VBP* idoms er-*|Er-*) AND (IP* idoms NP-SBJ) AND (IP* idoms [2]finiteVerb) AND ([1]BEP*|VBP* iprecedes NP-SBJ) AND (NP-SBJ iprecedes [2]finiteVerb)

replace_label{1}: C