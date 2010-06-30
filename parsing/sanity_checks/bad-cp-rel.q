node: $ROOT

copy_corpus: t

define: def/ICE.def

query: ({1}CP-REL* exists) AND (IP*|PP*|$ROOT idoms CP-REL*)

append_label{1}: -ZZZ-BADCPREL-MAY-BE-ADV
