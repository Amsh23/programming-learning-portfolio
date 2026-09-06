import random
options = ["rock" , "paper" , "scissors"]
user_win = 0
pc_win = 0 
ties = 0
for i in range(10):
    print(f"Round {i+1}")
    computer = random.choice(options)
    user=input("your choice (rock OR paper OR Scissors): ")
    print (f"Computer: {computer}")
    print (f"you: {user}")
    if user == computer:
        print("Tie!")
        ties+=1
    elif (user == "rock"and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissoirs" and computer == "paper"):
        print("You win!")
        user_win+=1
    else:
        print("You lose!")
        pc_win+=1 
print(f"Wins: {user_win}")
print(f"Ties: {ties}")
print(f"Losses: {pc_win}")

if user_win>pc_win:
    print("user_win")
elif user_win<pc_win:
    print("pc_win")
else:
    print("tie")