import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
user_input = input("enter a word: ").upper()
output = [new_dict[letter] for letter in user_input]
print(output)
