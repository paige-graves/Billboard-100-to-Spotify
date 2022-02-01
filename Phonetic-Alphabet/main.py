import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dictionary)

phonetic_output = True

while phonetic_output:

    word = input("What is your name?").upper()
    try:
        output_list = [phonetic_dictionary[letter] for letter in word]
        print(output_list)
        phonetic_output = False
    except KeyError:
        print("Sorry, only letters in the alphabet please")


