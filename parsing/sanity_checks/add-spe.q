node: IP*SPE*|CP*SPE*

define: def/ICE.def

copy_corpus: t

query: (IP*SPE* doms {1}CP-ADV|CP-ADV|CP-ADV-XXX|CP-CAR|CP-CMP|CP-CMP-XXX|CP-DEG|CP-DEG-XXX|CP-EOP|CP-EOP-XXX|CP-FRL|CP-QUE|CP-QUE-ADV|CP-QUE-XXX|CP-REL|CP-REL-XXX|CP-THT|CP-THT-XXX|CP-TMC|CP-TMP|CP-XXX|IP-ABS|IP-ABS-XXX|IP-IMP|IP-IMP-XXX|IP-INF|IP-INF-XXX|IP-MAT|IP-MAT-XXX|IP-PPL|IP-PPL-XXX|IP-SMC|IP-SMC-XXX|IP-SUB|IP-SUB-XXX|IP-SUB-ZZZ)

append_label{1}: -SPE
