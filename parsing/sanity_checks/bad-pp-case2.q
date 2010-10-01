node: IP*
define: def/ICE.def

copy_corpus: t

query: ((P hasSister NP)
AND (NP idoms *-D|*-G)
AND (P idoms um-um|gegnum-gegnum|kringum-kringum|umfram-umfram|umhverfis-umhverfis))
OR ((P hasSister NP)
AND (NP idoms *-A|*-G)
AND (P idoms frá-frá|að-að|af-af|andspænis-andspænis|ásamt-ásamt|gagnvart-gagnvart|gegn-gegn|gegnt-gegnt|handa-handa|hjá-hjá|meðfram-meðfram|undan-undan|úr-úr))
OR ( ({1}[1]PP idoms P)
AND ([2]PP idoms ![1]PP)
AND (P hasSister NP)
AND (NP idoms *-A|*-D)
AND (P idoms til-til|auk-auk|austan-austan|án-án|handan-handan|innan-innan|meðal-meðal|milli-milli|millum-millum|neðan-neðan|norðan-norðan|ofan-ofan|sakir-sakir|sunnan-sunnan|sökum-sökum|utan-utan|vegna-vegna|vestan-vestan))

append_label{1}: -ZZZ-BAD-PP-CASE
