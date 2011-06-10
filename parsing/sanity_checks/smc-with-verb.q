node: IP-SMC*

copy_corpus: t

query: ({1}IP-SMC* idoms RD*|VB*|BE*|MD*|DO*|HV*)

add_leaf_before{1}: (CODE *ZZZ_NOT_SMC*)
