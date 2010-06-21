node: $ROOT

copy_corpus: t

query: ({1}V* iDoms !*a|*A|*st|*ST|*sjá|*SJÁ|\*|V*|*-fá|*-FÁ|*-gá)

append_label{1}: -ZZZ-NOT_A_VERB
