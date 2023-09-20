import controller
import question

name = input("Enter player name: ")

player = controller.Player(name)
question = question.Question()

while player.next_question(question):
    print(question.question)
    answer = input("True or False? ")
    if player.check_answer(question=question, answer=answer):
        print("Correct!")
    else:
        print("Incorrect!")
    print(f"Your score is {player.score} out of {player.max_score}\n")

print(f"Game over! Your final score is {player.score} out of {player.max_score}")

with open("high_score.txt") as f:
    data = f.read().split()
    high_score = int(data[0])    
    high_score_holder = data[1]
    
if player.score > high_score:
    with open("high_score.txt", "w") as f:
        f.write(f"{player.score} {player.name}")
    print("You set a new high score!")
else:
    print(f"The current high score is {high_score} held by {high_score_holder}")