#!/usr/bin/python
# simple flash card game
import operator
import random

TRIALS_PER_GAME = 10
DIFFICULTY = {
    # 1 = Easy, 2 = Medium, 3 = Hard
    '1' : {
        'universe' : range(0, 10+1),
        'preprocess' : sorted,
        'operations' : [ [operator.add, '+'], [operator.sub, '-'],]
        },
    '2' : {
        'universe' : range(0, 30+1),
        'preprocess' : sorted,
        'operations' : [ [operator.add, '+'], ]
        },
    '3' : {
        'universe' : range(0, 100+1),
        'preprocess' : sorted,
        'operations' : [ [operator.add, '+'], [operator.sub, '-'],]
        },
    '4' : {
        'universe' : range(0, 100+1),
        'preprocess' : lambda x : x,
        'operations' : [ [operator.add, '+'], [operator.sub, '-'],]
        },
    }

def main():
    difficulty = welcome_message()
    number_correct = 0
    for i in range(0, TRIALS_PER_GAME):
        number_correct += flash_card(difficulty)
    print "number correct = " + str(number_correct) + "/" + str(TRIALS_PER_GAME)

def flash_card(difficulty):
    mylist = []
    mylist.append(random.choice(DIFFICULTY[difficulty]['universe']))
    mylist.append(random.choice(DIFFICULTY[difficulty]['universe']))
    mylist = DIFFICULTY[difficulty]['preprocess'](mylist)
    mylist.reverse()
    operation_list = random.choice(DIFFICULTY[difficulty]['operations'])
    mylist.insert(1, operation_list[1])
    answer = raw_input("%d%s%d = " % tuple(mylist))
    try:
        answer = int(answer)
        correct_answer = operation_list[0](mylist[0],mylist[2])
        if answer == correct_answer:
            return 1
        else:
            return 0
    except ValueError:
        return 0
    pass

def welcome_message():
    print ""
    print "Welcome to Flashcards! Please select difficulty"
    print "  1) Easy"
    print "  2) Medium"
    print "  3) Hard"
    print "  4) Very Hard"
    print ""
    choice = raw_input("Enter your choice (1, 2, 3, or 4) ==> ")
    if choice not in ['1', '2', '3', '4']:
        print "did not understand " + str(choice) + ", auto-choosing 1"
        choice = 1
    print ""
    return choice

main()
