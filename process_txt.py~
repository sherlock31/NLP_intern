import nltk
def process_txt(filepath):
	"This function accepts a path to a .txt file and returns a lemmatized,tokenized list of words in the imput .txt file"
	
	#SOME PAIN WITH FILE ENCODING THING, MAKE IT MORE SMART, CHECK FOR ENCODINGS AND THEN USE IT, you have downloaded some stuff for it
	
	text_file = open(filepath)														#opening the file located at the filepath
	raw_text_file = text_file.read()												#storing the raw content of file in raw_text_file
	tokens_text_file_list = nltk.word_tokenize(raw_text_file.decode('utf-8'))		#tokenizing the file 

#	wnl = nltk.WordNetLemmatizer()													#inbuit nltk lemmatizer
#	lemmatized_text_file_list = [wnl.lemmatize(t) for t in tokens_text_file_list]	#lemmatizing the tokenized list
#	lemmatized_text_file_list = [w.lower() for w in lemmatized_text_file_list]
	
	return tokens_text_file_list												#returning the lemmatized_text_file_list
	
	
