import random
print("------------ROCK PAPER SCISSOR GAME--------------")
print()
usr_score = 0
comp_score = 0
ties = 0
name = str(input("Enter your name : "))
print("""
Winning Rules :
    Rock vs Scissor ---> Rock
    Paper vs Rock ---> Paper
    Scissor vs Paper ---> Scissor""")
while True:
    print("""
choices are : 
  1).Rock
  2).Paper
  3).Scissor""")
    choices = int(input("Enter your choice(1-3) : "))
    print()
    if choices == 1:
        usr_choice = "Rock"
    elif choices == 2:
        usr_choice = "Paper"
    elif choices == 3:
        usr_choice = "Scissor"
    else:
        print("Invalid choice. Please try again")
        continue
    computer = random.randint(1,3)
    if computer == 1:
        comp_score = "Rock"
    elif computer == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissor"
    print(name,"choice : ",usr_choice,"|","Computer Choice :",comp_choice)
    if(usr_choice == "Rock" and comp_choice == "Scissor") or (usr_choice == "Scissor" and comp_choice == "Rock"):
        result = "Rock"
    elif(usr_choice == "Paper" and comp_choice == "Rock") or (usr_choice == "Rock" and comp_choice == "Paper"):
        result = "Paper"
    elif(usr_choice == comp_choice):
        result = "Tie"
    else:
        result = "scissor"
    if result == "Tie":
        print()
        print("---it's a tie---")
        ties += 1
    elif result == usr_choice:
        print()
        print("---You Win---")
        usr_score += 1
    else:
        print()
        print("---Computer Win---")
        comp_score += 1
    print()
    print("Score are : ")
    print("---------------------------")
    print(" "*4 + name, ":",usr_score,"|","Computer : ",comp_score,"|","Ties Are ; ",ties)
    print("---------------------------")
    print()
    repeat = str(input("Do you want to play again Yes/No :"))
    if repeat == "No" or repeat == "no":
        break
print()
if usr_score > comp_score:
    print(name,"Win with",usr_score,"Points!")
elif usr_score < comp_score:
    print("Computer Win with",comp_score,"Points!")
else:
    print("It's a Tie! You both win with",ties,"Points")
print()
