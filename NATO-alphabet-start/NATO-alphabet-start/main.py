
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonectic_dic =    nato_alpha = {row.letter:row.code for (index,row) in data.iterrows()}
word = input("Enter a word:").upper()
output = [phonectic_dic[letter] for letter in word]
print(output)