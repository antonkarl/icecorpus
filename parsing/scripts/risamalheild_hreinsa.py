#!python3
# -*- coding: utf-8 -*-

### Processes a batch of XML files from Risamálheild and creates
### .lemmatized (tagged and lemmatized) files.

import sys
import os
import time
from bs4 import BeautifulSoup

grunnmappa = sys.argv[1] # mappa þar sem log-skrár birtast
mappa_textar = sys.argv[2] # mappa með upprunalegu XML-textunum
mappa_hreinsadir_textar = sys.argv[3] # mappa þar sem hreinsaðir textar (markaðir og lemmaðir) vistast
hreinsad_skra = sys.argv[4] # log-skrá – listi af skrám sem voru hreinsaðar
ohreinsad_skra = sys.argv[5] # log-skrá – listi af skrám sem ekki tókst að hreinsa

hreinsad_listi = []
ohreinsad_listi = []

for greinarnafn in os.listdir(mappa_textar):
	try:
		timastrengur = time.strftime("%Y%m%d")
		grein = open(mappa_textar + greinarnafn, 'r')
		greinXML = grein.read()
		grein.close()
		soup = BeautifulSoup(greinXML, 'lxml')
		
		# a list of tagged and lemmatized words of the form
		# [WORD] [TAG] [LEMMA]
		# with spaces between parameters, line breaks between words
		words_lemmatized = []
		
		# a list of the same words, only tagged, of the form
		# [WORD] [TAG]
		# with spaces between parameters, line breaks between words
		#words_tagged = []
		
		for sentence in soup.find_all('s'):
			for word in sentence.findChildren():
			    if(word.name == 'w'):
			        words_lemmatized.append(word.string + ' ' + word['type'] + ' ' + word['lemma'])
			        #words_tagged.append(word.string + ' ' + word['type'])
			    else:
			        words_lemmatized.append(word.string + ' ' + word.string + ' ' + word.string)
			        #words_tagged.append(word.string + ' ' + word.string)
			# cause double line break at end of the sentence
			words_lemmatized.append('')
			#words_tagged.append('')
		
		hreinsud_grein_lemmatized = open(mappa_hreinsadir_textar + greinarnafn[:-4] + '.lemmatized', 'w')
		hreinsud_grein_lemmatized.write('\n'.join(words_lemmatized))
		hreinsud_grein_lemmatized.close()
		
		#hreinsud_grein_tagged = open(mappa_hreinsadir_textar + greinarnafn[:-4] + '.tagged', 'w')
		#hreinsud_grein_tagged.write('\n'.join(words_tagged))
		#hreinsud_grein_tagged.close()
		
		hreinsad_listi.append(greinarnafn + '\t' + timastrengur)
	except Exception as e:
		ohreinsad_listi.append(greinarnafn + '\t' + timastrengur)

hreinsadFile = open(grunnmappa + hreinsad_skra,'w')
hreinsadFile.write('\n'.join(hreinsad_listi))
hreinsadFile.close()

ohreinsadFile = open(grunnmappa + ohreinsad_skra,'w')
ohreinsadFile.write('\n'.join(ohreinsad_listi))
ohreinsadFile.close()
