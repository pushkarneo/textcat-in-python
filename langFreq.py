import re
import operator
import glob

class langFreq:
	def __init__(self,language = "",path = "",text = ""):
		self.lang_freq = {}
		self.lang_name = language
		self.path      = path
		self.text      = text

	def _tokenisor(self,text):
	    tokens = re.split('\s+|\n\s',text)
	    reg = re.compile(r'[0-9\[\]\,]')
	    filtered = [i for i in tokens if not reg.search(i)]
	    return filtered

	def _ngrams(self,word,n):
	    if n > 1:
	        word = "_" + word
	    for i in range(n-1):
	        word = word + "_"
	    ngrams = [word[i:i+n] for i in range(len(word)-n+1)]
	    return ngrams

	def _ngrams_sentence(self,text):
		tokens = self._tokenisor(text)
		ngrams = []
		for word in tokens:
			for i in range(1,6):
				ngrams = ngrams + self._ngrams(word,i)
		return ngrams
				
	def _add_sentence_lang_freq(self,text):
		ngrams = self._ngrams_sentence(text)
		for ngm in ngrams:
			if ngm not in self.lang_freq:
				self.lang_freq.update({ngm:1})
			else:
				ngm_occurrences = self.lang_freq[ngm]
				self.lang_freq.update({ngm:ngm_occurrences+1})
	
	def get_lang_name(self):
		return self.lang_name

	def get_lang_prof(self):
		return self.lang_freq

	def build_lang_freq_file(self):
		files = glob.glob("%s\\*" % self.path)
		for file in files:
			lines = open(file, mode = 'r', encoding = 'utf-8').readlines()
			for line in lines:
				self._add_sentence_lang_freq(line)
		self._sort_lang_freq()
	
	def build_lang_freq_text(self):
		self._add_sentence_lang_freq(self.text)
		self._sort_lang_freq()

	def _sort_lang_freq(self):
		self.lang_freq = sorted(self.lang_freq.items(),key=operator.itemgetter(1),reverse=True)[0:300]
		#print(self.lang_freq)
	