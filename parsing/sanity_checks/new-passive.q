node: $ROOT

copy_corpus: t

query: (VAN* hasSister NP-OB*) AND ({1}NP-OB* idoms *-A)

append_label{1}: -ZZZ-NEW-PASSIVE
