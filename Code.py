import random
word_list = ["summer", "winter", "monsoon", "spring"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

placeholder= ""
word_length= len(chosen_word)
for position in range(word_length):
    placeholder+="_"

display= ""
for letter in chosen_word:
    if letter== guess:
        display+=letter
    else:
        display+= "_"

print(display)
