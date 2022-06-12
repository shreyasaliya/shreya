n =18
number_of_guesses =1
print("number of guesses is limited to only 9 times")

while (number_of_guesses<=9):
    guessnum =int(input("Guess the number:\n"))
    if guessnum<18:
        print("you entered less number please input greater number.\n")
    elif guessnum>18:
        print("you entered greater number please input lesser number.\n")
    else:
        print("you won\n")
        print(number_of_guesses,"no. of guesses you took to finish.")
        break
    
    print(9-number_of_guesses,"no. of guesses left\n")
    number_of_guesses = number_of_guesses+1

if(number_of_guesses>9):
    print("game over")