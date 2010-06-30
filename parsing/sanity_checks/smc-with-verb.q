node: IP-SMC*

copy_corpus: t

query: ({1}IP-SMC* idoms RD*|VB*|BE*|MD*|DO*|HV*)

append_label{1}: -ZZZ-NOT_SMC
