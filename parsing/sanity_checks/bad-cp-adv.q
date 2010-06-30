node: $ROOT

copy_corpus: t

define: def/ICE.def

query: ({1}CP-ADV* exists) AND (!IP*|PP*|$ROOT idoms CP-ADV*)

append_label{1}: -ZZZ-BADCPADV-MAY-BE-REL
