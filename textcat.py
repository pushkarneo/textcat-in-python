import glob
import os
from langFreq import langFreq	

class textcat:
	def __init__(self):
		self.doc_path = '.\\txt\\'
		self.lang_freqs = {}
		self.lang_map = {'bg' : 'Bulgarian','cs' : 'Czech','da' : 'Swedish','de' : 'German','el' : 'Greek','en' : 'English','es' : 'Spanish','et' : 'Estonian','fi' : 'Finnish','fr' : 'French','hu' : 'Hungarian','it' : 'Italian','lt' : 'Lithuanian','lv' : 'Latvian','nl' : 'Dutch','pl' : 'Polish','pt' : 'Portuguese','ro' : 'Romanian','sk' : 'Slovak','sl' : 'Slovenian','sv' : 'Norwegian'}
		self._build_languages_freqs()

	def _build_languages_freqs(self):
		langs = glob.glob("%s*" % self.doc_path)
		for lang_path in langs:
			language = os.path.basename(lang_path)
			
			self.lang_freqs[language] = langFreq(language = language, path = lang_path)
			self.lang_freqs[language].build_lang_freq_file()
	
	
	def language_classify(self,text):
		lang_freq_prof = langFreq(text = text)
		lang_freq_prof.build_lang_freq_text()
		
		min_dist = 100000000
		nearest_lang = ""
		print("Distance of language from input text")
		for lang, langFreq_obj in self.lang_freqs.items():
			distance = self._compare_freq_profs(langFreq_obj.get_lang_prof(),lang_freq_prof.get_lang_prof())
			print(langFreq_obj.get_lang_name() + " : " + str(distance))	
			if distance < min_dist:
				min_dist = distance
				nearest_lang = langFreq_obj.get_lang_name()

		return self.lang_map[nearest_lang]
			

	def _compare_freq_profs(self,cat_prof,doc_prof):
		cat_prof_ngrams = [ngram[0] for ngram in cat_prof]
		doc_prof_ngrams = [ngram[0] for ngram in doc_prof]

		max_out_of_place = len(doc_prof_ngrams)
		doc_distance = 0
		for ngram in doc_prof_ngrams:
			doc_ind = doc_prof_ngrams.index(ngram)
			try:
				cat_prof_ind = cat_prof_ngrams.index(ngram)
			except ValueError:
				cat_prof_ind = max_out_of_place

			ngram_distance = abs(cat_prof_ind - doc_ind)
			doc_distance += ngram_distance

		return doc_distance