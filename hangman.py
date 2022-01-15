import random
word_list = [aviral, vaibhav, ishaan, ali]
guess = random.choice(word_list)
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")    
