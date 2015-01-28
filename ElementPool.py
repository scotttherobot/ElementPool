# A parser for an amateur radio licensing exam element pool.
# 
# You can find these pools here:
# http://www.arrl.org/question-pools
#
# This was built and tested against the Technician pool.
# By Scott Vanderlind, January 2015
import re

class Question:

   def __init__(self, number):
      self.number = number
      self.correct = ""
      self.choices = {}
      self.figure = ""
      self.prompt = ""

   def addChoice(self, choice, text):
      self.choices[choice] = text

   def __str__(self):
      properties = {
            "id":self.number, 
            "correct":self.correct,
            "figure": self.figure,
            "choices": self.sortedChoices(),
            "prompt": self.prompt
            }
      return str(properties)

   def __repr__(self):
      return self.__str__()

   def sortedChoices(self):
      return sorted(self.choices.items())


class ElementPool:

   questions = {}

   def __init__(self, file):
      self.parse(file)
      return

   def parse(self, file):
      f = open(file, 'r')
      
      # Match the question header
      qr = re.compile("([A-Z][1-9][A-Z][0-9]{2})\s\(([A-D])\)")
      # Match a figure in a question
      fr = re.compile(".*figure\s(.*)\?")
      # Match a choice
      cr = re.compile("([A-Z])\.\s(.*)\r")

      currentQuestion = ""
      for line in f:
         isQuestion = qr.match(line)
         if isQuestion:
            number = isQuestion.group(1)
            correct = isQuestion.group(2)
            question = Question(number)
            question.correct = correct

            # Get the actual prompt from the next line
            question.prompt = next(f).strip('\r\n')

            # See if it has a figure
            figure = fr.match(question.prompt)
            if figure:
               fig = figure.group(1)
               question.figure = fig

            self.questions[number] = question
            # Update the current question so we can add answers to it
            currentQuestion = number
            # Skip the next steps if we found a question header
            continue

         isChoice = cr.match(line)
         if isChoice:
            choice = isChoice.group(1)
            text = isChoice.group(2)
            question = self.questions[currentQuestion]
            question.addChoice(choice, text)

   def sortedQuestions(self, reverse = False):
      return sorted(self.questions.items())

   def __str__(self):
      return str(self.sortedQuestions())

   def __repr__(self):
      self.__str__()

