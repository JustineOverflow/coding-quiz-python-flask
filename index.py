import random


class Question:
    def __init__(self, question, correctAnswer, otherAnswers):
        self.question = question
        self.correctAnswer = correctAnswer
        self.otherAnswers = otherAnswers


questionsList = [Question("Which of the following is not a programming language?", "Cobra", ["Python", "Swift"]),
                 Question("Which language is dedicated to code iOS programs?", "Swift", ["C#", "Java", "Kotlin"]),
                 Question("Which of the following time complexity is the most efficient?", "O(log N)",
                          ["O(nlogn)", "O(n)"])]

score = 0

random.shuffle(questionsList)

for qItem in questionsList:
    print(qItem.question)
    print("Here are the possible answers:")
    possible = qItem.otherAnswers + [qItem.correctAnswer]
    random.shuffle(possible)
    count = 0
    while count < len(possible):
        print(str(count + 1) + ": " + possible[count])
        count += 1
    print("Please enter the number of your answer:")
    userAnswer = raw_input()
    while not userAnswer.isdigit() or not 0 < int(userAnswer) <= len(possible):
        print("Try again - please enter a valid number:")
        userAnswer = raw_input()
    userAnswer = int(userAnswer)
    if possible[userAnswer - 1] == qItem.correctAnswer:
        print("Correct answer!")
        score += 1
    else:
        print("Wrong answer")
        print("Correct answer was: " + qItem.correctAnswer)
        print("")
print("The quiz is over! your score is: " + str(score))
