node: NP*|WNP*

copy_corpus: t

define: def/ICE.def

query: (NP* idoms PRO*) AND (NP* idoms {1}CP-THT|CP-THT-[0-9]|CP-THT-SPE|CP-THT-SPE-[0-9])

append_label{1}: -ZZZ
