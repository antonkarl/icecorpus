node: $ROOT

copy_corpus: t

define: def/ICE.def

query: ({1}[1]CP-REL|CP-REL-SPE exists) AND (IP*|PP*|$ROOT idoms [1]CP-REL|CP-REL-SPE)

append_label{1}: -ZZZ-BADCPREL-MAY-BE-ADV
