import random
class QA:
  def __init__(self, question, correctAnswer, otherAnswers):
    self.question = question
    self.corrAnsw = correctAnswer
    self.otherAnsw = otherAnswers
fileout = open("data.txt", "w")
qaList = [QA("The inaugural ipl season was won by which team?", "Rajasthan Royals", ["Deccan Chargers", "Chennai Super Kings","Mumbai Indians"]),
QA("Who scored the first ipl century?", "Brandon McCullum", ["A B Devilliers", "Chris Gayle", "Sachin Tendulkar"]),
QA("Who took the fastest 100 wickets in ipl?", "Lasith Malinga", ["Bhuvneshwar Kumar", "Yuzvendra Chahal", "Amit Mishra"]),
QA("Most catches taken by a player in ipl history?", "Suresha Raina", ["Virat kohli", "Setve Smith","Rohit Sharma"]),
QA("Most dismissals by a wicket keeper in ipl?", "Mahendra Singh Dhoni",["Dinesh Kartik", "Parthiv Patel", "Robin Uthappa"])]
name = input("Enter your name:")
print("Hello " + name + "! Best of Luck!")

corrCount = 0
random.shuffle(qaList)
for qaItem in qaList:
  print(qaItem.question)
  print("Possible answers are:")
  possible = qaItem.otherAnsw + [qaItem.corrAnsw]
  random.shuffle(possible)
  count = 0 
  while count < len(possible):
    print(str(count+1) + ": " + possible[count])
    count += 1
  print("Please enter the number of your answer:")  
  userAnsw = input()
  while not userAnsw.isdigit():
    print("That was not a number. Please enter the number of your answer:")    
    userAnsw = input()
  userAnsw = int(userAnsw)
  while not (userAnsw > 0 and userAnsw <= len(possible)):
    print("That number doesn't correspond to any answer. Please enter the number of your answer:")    
    userAnsw = int(input())
    
  if possible[userAnsw-1] == qaItem.corrAnsw:
    print("Your answer was correct.")    
    corrCount += 1
  else:
    print("Your answer was wrong.")    
    print("Correct answer was: " + qaItem.corrAnsw)
print("You answered " + str(corrCount) + " of " + str(len(qaList)) + " questions correctly.")
print("Thank you for playing")
rec = "Sports Quiz:- " + "Correct answers: " + str(corrCount) + "Games Played: " + str(count) + '\n'
fileout.write(rec)

