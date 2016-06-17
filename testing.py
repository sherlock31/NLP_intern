from process_txt import process_txt
import norvig_spell
import ngrams.py

txt_data = process_txt('/home/sherlock31/Desktop/Intern/2016_06_14/unique/labfiles-set1_0001.txt')

corr_data=[]
for word in txt_data:
	corr_data.append(ngrams.correct(word))
	
	
print corr_data