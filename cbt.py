from questions import questions
from line import generate 
from math import fabs
from random import shuffle
from scoreStatus import *

# Sorts questions list
shuffle(questions)

# Re-assigns it to this variable
questionList = questions

# Intro
generate(30)
print(f'Welcome to the CBT Test designed by Fisayo Obadina.  This test covers HTML5, CSS3, JavaScript and Python. Answer the question below to proceed')
generate(30)

response = input('Are you ready (y/n): ')
response2 = input('Enter your Name: ')

score = 0
index = 0

# Print Test No:
generate(20)
print(f'You have {len(questionList)} questions to answer:')
generate(20)

def startTest(index, score):
  currentQuestion = questionList[index]
  questionTitle = currentQuestion['question']
  questionOptionsList = []
  correctAnswer = ''
  for opt in currentQuestion['options']:
    if opt['correct'] == True:
      correctAnswer = opt['id']
    questionOptionsList.append({'opt': opt['opt'], 'id': opt['id']})

  
  # Print Question
  generate(20)
  print(f'{index+1}. {questionTitle}')
  
  # Print Options
  for option in questionOptionsList:
    id = option['id']
    opt = option['opt']
    print(f'  {id}. {opt}')
    
  generate(20)

  # Input Answer
  answer = input('Enter your answer: ')

  if correctAnswer.upper() == answer.upper():
    score += 1
  if index + 1 >= len(questionList):
    generate(20)
    generate(20)
    scorePercentage = fabs((score/len(questionList))*100)

    scoreStatus = ''

    if scorePercentage >= 90:
      scoreStatus = status_90
    elif scorePercentage >= 80:
      scoreStatus = status_80
    elif scorePercentage >= 65:
      scoreStatus = status_65
    elif scorePercentage >= 50:
      scoreStatus = status_50
    elif scorePercentage >= 30:
      scoreStatus = status_30
    elif scorePercentage >= 15:
      scoreStatus = status_15
    elif scorePercentage >= 8 or scorePercentage == 0:
      scoreStatus = status_0

    print(f'Congrats {response2}, you scored {scorePercentage}%. {scoreStatus}')
    generate(20)
    generate(20)
  else:
    index += 1
    initTest(index, score)
  

def initTest(index, score):
  startTest(index, score)

if response == 'y' or 'Y' or response != '' :
  initTest(index, score)
else:
  exit()
