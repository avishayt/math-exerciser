#!/usr/bin/python

import argparse
import colorama
from colorama import Fore, Back, Style
import emoji
import os
import random

colorama.init(autoreset=True)
bgcolors = [Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN]
emojis = [':thumbs_up:', ':v:', ':revolving_hearts:', ':sparkling_heart:', ':laughing:',
          ':blush:', ':grinning:', ':stuck_out_tongue:', ':stuck_out_tongue_closed_eyes:',
          ':star2:', ':smile_cat:', ':heart_eyes_cat:', ':monkey_face:', ':hibiscus:',
          ':tulip:', ':balloon:', ':white_check_mark:', ':heart_decoration:',
          ':ice_cream:', ':icecream:', ':birthday:', ':ribbon:', ':gift:', ':rabbit:',
          ':baby_chick:', ':panda_face:', ':bear:', ':dog:', ':joy_cat:']

parser = argparse.ArgumentParser()
parser.add_argument("nums", help="numbers")
parser.add_argument("count", help="numbers")
parser.add_argument("--worksheet", action="store_true")
args = parser.parse_args()

nums = [int(x) for x in args.nums.split(',')]
nums2 = range(1, 11)
hundred = range(2,100)
thousand = range(101,1000)
operators = ['mul', 'div']
#operators = ['add', 'sub', 'mul', 'div']
#operators = ['bet']
add_max = 5
sub_max = 5
bet_max = 5

i = 0
adds = 0
subs = 0
bets = 0
while i < int(args.count):
    op = random.choice(operators)

    if op == 'add':
        if adds > add_max:
            continue
        operands = [random.choice(thousand), random.choice(thousand)]
        answer = operands[0] + operands[1]
        problem = '%s\n+ %s\n  ___\n' % (str(operands[0]).rjust(5), str(operands[1]).rjust(3))
        adds += 1
    elif op == 'sub':
        if subs > sub_max:
            continue
        bigger = random.choice(thousand)
        smaller = random.choice(range(1, bigger))
        answer = bigger - smaller
        problem = '%s\n- %s\n  ___\n' % (str(bigger).rjust(5), str(smaller).rjust(3))
        subs += 1
    elif op == 'bet':
        if bets > bet_max:
            continue
        bigger = random.choice(hundred)
        smaller = random.choice(range(101, bigger))
        answer = 0
        problem = '%s < ___ < %s' % (smaller, bigger)
        bets += 1
    elif op == 'mul':
        operands = [random.choice(nums), random.choice(nums2)]
        product = operands[0] * operands[1]
        first = random.choice([0,1])
        second = 0 if first == 1 else 1

        variable = random.choice([0,4])
        if variable == 0:
            answer = operands[first]
            problem = '? X %d = %d\t____' % (operands[second], product)
        elif variable == 1:
            answer = operands[second]
            problem = '%d X ? = %d\t____' % (operands[first], product)
        else:
            answer = product
            problem = '%d X %d = ?\t____' % (operands[first], operands[second])
    else:  # div
        operands = [random.choice(nums), random.choice(nums2)]
        product = operands[0] * operands[1]
        first = random.choice([0,1])
        second = 0 if first == 1 else 1

        answer = operands[second]
        problem = '%d : %d = ?\t____' % (product, operands[first])

    attempt = -1
    if args.worksheet:
        print(problem + '\n')
        i = i + 1
        continue

    while (op == 'bet' and (attempt <= smaller or attempt >= bigger)) or (op != 'bet' and attempt != answer):
        attempt = input(random.choice(bgcolors) + problem + Style.RESET_ALL + '\t')
        try:
            attempt = int(attempt)
        except:
            attempt = -1

        if (op == 'bet' and (attempt > smaller and attempt < bigger)) or (op != 'bet' and attempt == answer):
            print(emoji.emojize(random.choice(emojis), use_aliases=True) +
                  " " + str(int(args.count) - i - 1) + " left")
        else:
            print("")
    i = i + 1

if not args.worksheet:
    print('Great job Libi!!!')
