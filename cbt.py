from questions import questions
from line import generate

questionList = questions
response = input('Are you ready (y/n): ')

score = 0
index = 0


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

  if correctAnswer == answer:
    score += 1
  if index + 1 >= len(questionList):
    generate(20)
    generate(20)
    scorePercentage = (score/len(questionList))*100
    print(f'You scored {scorePercentage}%')
    generate(20)
    generate(20)
  else:
    index += 1
    initTest(index, score)
  

def initTest(index, score):
  startTest(index, score)


if response == 'y' or 'Y' :
  initTest(index, score)
