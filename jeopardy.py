#/bin/python3

from random import randint
import os
import time

TOTAL_CATEGORIES = 3
TOTAL_QUESTIONS = 9
CATEGORY = 0
VALUE = 1
QUESTION = 2
ANSWER = 3
NO_QUESTION = "_"*4


def getInfo(quesInfo, whichInfo):
    if quesInfo[VALUE] == NO_QUESTION:
        return NO_QUESTION
    else:
        return quesInfo[whichInfo]

def loadCSV(filename):
    outputList = []
    
    try:
        source = open(filename, "r", encoding="UTF-8")
        sourceList = source.readlines()
        
        for i in sourceList:
            i_no_newline = i.strip()
            i_list = i_no_newline.split(",")

            outputList.append(i_list)
        
        source.close
    
    except FileNotFoundError:
        print("Unable to open input file: " + filename)
        outputList = []

    return outputList

def getCategoryList(fileList):
    category_list = []
    
    while True:
        random_number = randint(0,len(fileList)-1)
        category = fileList[random_number][CATEGORY]
        
        if category == "#NAME?":
            continue

        if category not in category_list:
            category_list.append(category)
    
            if len(category_list) == TOTAL_CATEGORIES:
                break
    
    return category_list

def getQuestionList(input_list, category_list):
    possible_questions = []
    
    for row in input_list:
        
        if row[CATEGORY] in category_list:
            possible_questions.append(row)
    
    questionList = []
    
    while True:
        random_number = randint(0, len(possible_questions)-1)
        
        if possible_questions[random_number] not in questionList:
            questionList.append(possible_questions[random_number])
        
        if len(questionList) == TOTAL_QUESTIONS:
        
            break

    return questionList

def printBoard(questions_list):
    max_columns = 3
    board = [[],[],[]]
    for idx, item in enumerate(questions_list):
        board_tile = "Q"+str(idx)+"($"+str(item[VALUE]+")")
        row_idx = int(idx / max_columns)
        board[row_idx].append(board_tile)
    for row in board:
        print('   '.join(row))
    
def getCategories(input_list):
    all_categories = []
    last_row = ""
    for row in input_list:
        if row[0] == "#NAME?":
            continue
        if last_row == row[0]:
            continue
        last_row = row[0]
        all_categories.append(row[0])
    print(all_categories)

def hasQuestions(questionList):
    for each in questionList:
        
        if NO_QUESTION != each[VALUE]:
            
            return True
    
    return False


def getQuestionIndex(questionList):
    while True:
        question_selection = input("Choose a question (0-8)\n")
        try:
            if int(question_selection) < len(questionList):
                if questionList[int(question_selection)][VALUE] != NO_QUESTION:
                    break
                else:
                    print("Question no longer available, try again")
                    continue
            else:
                print("invalid selection, try again")
        except ValueError:
            print("invalid selection, try again")

    return int(question_selection)


def main():
    os.system('clear')
    big_list = loadCSV('jeopardy.csv')
    categories = getCategoryList(big_list)
    questions = getQuestionList(big_list, categories)
    print(f"todays game will be using the following categories: {categories[0]}, {categories[1]}, and {categories[2]}\n\n\n")
    player_score = 0
    while True:
        if not hasQuestions(questions):
            break
        else:
            printBoard(questions)
            print(f"\nScore: {player_score}\n")
            question_number = getQuestionIndex(questions)
            question = questions[question_number]
            print(f"For {question[VALUE]}, the category is {question[CATEGORY]}, and the question is:\n{question[QUESTION]}")
            answer = input("Answer: ").lower()
            if question[ANSWER].lower() == answer:
                print(f"Correct, awarding {question[VALUE]}")
                player_score += int(question[VALUE])
            else:
                print(f"Incorrect, the answer was {question[ANSWER]}")
            questions[question_number][VALUE] = NO_QUESTION
            time.sleep(3)
            os.system('clear')

    print(f"Game over\nScore: {player_score}")
    
if __name__ == "__main__":
    main()