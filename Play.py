#!/usr/bin/python
# simple flash card game
import operator, random, sys, time
TRIALS_PER_GAME = 10
DIFFICULTY = { # 1 = Easy, 2 = Medium, 3 = Hard
    '1' : { 'universe' : range(0, 10+1), 'preprocess' : lambda x : sorted(x, reverse=True), 'operations' : [ [operator.add, '+'], [operator.sub, '-'],] },
    '2' : { 'universe' : range(0, 30+1), 'preprocess' : lambda x : sorted(x, reverse=True), 'operations' : [ [operator.add, '+'], ] },
    '3' : { 'universe' : range(0, 100+1), 'preprocess' : lambda x : sorted(x, reverse=True), 'operations' : [ [operator.add, '+'], [operator.sub, '-'],] },
    '4' : { 'universe' : range(0, 100+1), 'preprocess' : lambda x : x, 'operations' : [ [operator.add, '+'], [operator.sub, '-'],] },
    'q' : None,
    }

def slow_print(s):
    for letter in s: sys.stdout.write(letter) ; sys.stdout.flush() ; time.sleep(.04)

def main():
    difficulty = welcome_message()
    if difficulty == 'q': return
    print ""
    number_correct = 0
    for i in range(0, TRIALS_PER_GAME): number_correct += flash_card(difficulty)
    print "number correct = " + str(number_correct) + "/" + str(TRIALS_PER_GAME)

def flash_card(difficulty):
    mylist = DIFFICULTY[difficulty]['preprocess']([random.choice(DIFFICULTY[difficulty]['universe']), random.choice(DIFFICULTY[difficulty]['universe'])])
    op = random.choice(DIFFICULTY[difficulty]['operations'])
    try: return 1 if int(raw_input("%d%s%d = " % tuple(mylist[0:1] + [op[1]] + mylist[1:2]))) == op[0](mylist[0],mylist[1]) else 0
    except ValueError: return 0

WELCOME_MESSAGE = """
Welcome to Flashcards! Please select difficulty
  1) Easy
  2) Medium
  3) Hard
  4) Very Hard
  q) Quit

Enter your choice ==> """
def welcome_message():
    slow_print(WELCOME_MESSAGE)
    choice = raw_input()
    if choice not in DIFFICULTY.keys():
        print "did not understand " + str(choice) + ", auto-choosing 1"
        choice = '1'
    return choice
main()
