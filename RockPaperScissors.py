games = 0
won = 0
lost = 0
tie = 0
  
print("Welcome to Rock,Paper and Scissors.")

print("Best of Luck")

choice = "Y"
while choice == 'Y':
    ans = int(input('Enter 1-Rock 2-Paper 3-Scissor : '))
    comp = random.randint(1, 3)
    if ans == comp:
        print ("tie !!!!!!!!")
        
        tie += 1
    if ans == 1:
        if(comp == 3):
            print("You Won")
            
            won += 1
        elif(comp == 2):
            print("You lost")
            
            lost += 1
    if(ans == 2):
        if(comp == 1):
            print("You Won")
            time.sleep(1)
            won += 1
        elif(comp == 3):
            print("You Lost")
           
            lost += 1
    if(ans == 3):
        if(comp == 2):
            print("You Won")
           
            won += 1
        elif(comp == 1):
            print("You Lost")
            
            lost += 1
    elif(ans >> 3):
        print("Invalid")
    games += 1
    choice = input("Want to play more( Y/N) :").upper()
    
print("Thank you for playing")
print("Total games played : ", games)
print("Total Wins : ", won)
print("Total defeats : ", lost)
print("Total Ties : ", tie)
rec_2 = "Rock,Paper and Scissors:- " + " Games Played: " + str(games) + "Games Won: " + str(won) + "Games Lost: " + str(lost) + "Games Tied: " + str(tie)
