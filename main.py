from textcat import textcat
import sys	
		
if __name__ == '__main__':
	texcat = textcat()
	input_file = sys.argv[1]
	text = ""
	with open(input_file,'r') as file:
		for line in file:
			text = text + line
	output = texcat.language_classify(text)
	print("Detected Language : %s" % output)
