# Summary: Plays a mini text based Jeopardy variant.
# author: Jake Bennett
# date: 09 Dec 2022


import random
import csv

#Constant representing the CSV
QUESTION_FILENAME = "jeopardy.csv"

# Constants for the parts of a question
CATEGORY = 0
VALUE = 1
QUESTION = 2
ANSWER = 3

# Constant representing a used question
NO_QUESTION = "____"



# Copy your getInfo function from the minitask
def getInfo(question, whichInfo):
    if question == NO_QUESTION:
        getInfoReturn = NO_QUESTION
        return getInfoReturn
    else:
        getInfoQuestion = questionList[question].split(",")
        getInfoReturn = getInfoQuestion[whichInfo]
        return getInfoReturn



# Read in a file and return a list containing the lines in the file
# parameter: filename - name of CSV file to read
# return: list containing stripped lines of the file

def loadCSV(QUESTION_FILENAME):
    with open('jeopardy.csv',encoding='utf-8') as file:
        #strips newline from each line in the list
        reader = csv.reader(file,dialect=csv.excel,delimiter=",")
        #goes down entire CSV list to append to the lists stored
        for row in reader:
            for i in range (-1, 3):
                listList[i + 1].append(row[i + 1])
            CSVList.append(row)
    return[CSVList]



# Takes a list containing every line from the question csv list
# Returns a new list containing only the categories
# parameter:  fileList - list containing lines of a CSV file containing quiz data
# return : list of strings containing exactly 3 unique categories of questions
def getCategoryList(categList):
    threeCat = []
    [threeCat.append(x) for x in categList if x not in threeCat]
    Cat3 = []
    for i in range (0, 3):
        Cat3.append(threeCat [random.randint(0, 103)])
    return (Cat3)

# Takes a list containing every line from the question csv list
# Returns a new list containing only the questions whose category is in categoryList
# parameter:  fileList - list containing lines of a CSV file containing quiz data
#             categoryList - list containing categories from which to choose questions
# return : list of exactly 9 strings containing CSV formatted question info
#                  from only the categories contained in categoryList
def getQuestionList(fileList, categoryList):
    return []



# Prints question board
# For example:
# Q0($100)  Q1($200)  Q2($400)
# Q3($200)  Q4($150)  Q5($600)
# Q6($200)  Q7($150)  Q8($600)
#
# parameter:  questionList - list of 9 CSV formatted questions
def printBoard(questionList):
    print("PRINTING BOARD")
    


# Checks question list for a valid question
# If every element is NO_QUESTION, return false
# If at least one element has text, return true
# parameter:  questionList - list of 9 CSV formatted questions
# return: true if at least one question is unused, false otherwise
def hasQuestions(questionList):
    return True


# Asks user which question he/she wants to answer
# See Day 26 slides for example try/except
# parameter:  questionList - list of 9 CSV formatted questions
# return: a valid index into questionList
def getQuestionIndex(CSVList):
    catList = []
    
    return 0





##########################################
## Main
##################################

# Put your main game loop code here!

# Constant for filename
QUESTION_FILENAME = "jeopardy.csv"
#Calls loadCSV to get and store the list.
QUESTION_FILENAME = "jeopardy.csv"
CSVList = []
categList = []
pointList = []
questList = []
ansList = []
listList = [categList, pointList, questList, ansList]
CSVList = loadCSV(QUESTION_FILENAME)

###############################################
#=================TEST========================#
