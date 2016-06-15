import nltk
import enchant
from enchant.checker import SpellChecker

def spell_checker(text_path):
	"This function accepts path to a text file and runs spell check on it using enchant module"
	
	eng_checker = SpellChecker("en_US")
	text_data = open(text_path)
	raw_text = text_data.read()
	
	


