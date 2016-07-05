from process_txt import process_txt
from ngrams import correct 
def run_spell_check(file_path):
	"This function accepts path to a text file as input runs spell check on it"
	correct_path = file_path.replace('.txt', '_spell_checked.txt')
	f = open(correct_path, 'w')
	tokens = process_txt(file_path)
	word_corrected = []
	
	for word in tokens:
		temp = correct(word)
		word_corrected.append(temp)
		f.write(temp)
		
	
			 
