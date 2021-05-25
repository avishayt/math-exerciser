#!/usr/bin/python

import argparse
import colorama
from colorama import Fore, Back, Style
import emoji
import os
import random
import yaml

colorama.init(autoreset=True)
bgcolors = [Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN]
emojis = [':thumbs_up:', ':v:', ':revolving_hearts:', ':sparkling_heart:', ':laughing:',
          ':blush:', ':grinning:', ':stuck_out_tongue:', ':stuck_out_tongue_closed_eyes:',
          ':star2:', ':smile_cat:', ':heart_eyes_cat:', ':monkey_face:', ':hibiscus:',
          ':tulip:', ':balloon:', ':white_check_mark:', ':heart_decoration:',
          ':ice_cream:', ':icecream:', ':birthday:', ':ribbon:', ':gift:', ':rabbit:',
          ':baby_chick:', ':panda_face:', ':bear:', ':dog:', ':joy_cat:']

def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help='a configuration file in YAML format')
    args = parser.parse_args()

    options = {'name': '',
               'count': 20,
               'operands': range(2, 10),
               'addition_range': range(101,1000),
               'operations': ['mul', 'div']}

    if args.config:
        with open(args.config, 'r') as ymlfile:
            cfg = yaml.safe_load(ymlfile)

        print(cfg)
        if 'name' in cfg:
            options['name'] = cfg['name']
        if 'count' in cfg:
            options['count'] = int(cfg['count'])
        if 'operands' in cfg:
            options['operands'] = cfg['operands']
        if 'operations' in cfg:
            options['operations'] = cfg['operations']

    return options

def addition(addition_range):
    operands = [random.choice(addition_range), random.choice(addition_range)]
    answer = operands[0] + operands[1]
    problem = '%s\n+ %s\n  ___\n' % (str(operands[0]).rjust(5), str(operands[1]).rjust(3))
    get_and_check_solution(problem, answer)

def subtraction(addition_range):
    bigger = random.choice(addition_range)
    smaller = random.choice(range(1, bigger))
    answer = bigger - smaller
    problem = '%s\n- %s\n  ___\n' % (str(bigger).rjust(5), str(smaller).rjust(3))
    get_and_check_solution(problem, answer)

def multiplication(operands):
    operands = [random.choice(operands), random.choice(range(1, 11))]
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

    get_and_check_solution(problem, answer)

def big_multiplication():
    multiplication(range(2,100), range(2,100))

def zeroes_multiplication(operands):
    operands = [random.choice(operands), random.choice(range(1, 11))]
    operands[0] = operands[0] * (10 ** random.choice(range(0, 3)))
    operands[1] = operands[0] * (10 ** random.choice(range(0, 3)))
    answer = operands[0] * operands[1]
    problem = '%d X %d = ?\t____' % (operands[0], operands[1])
    get_and_check_solution(problem, answer)

def division(operands):
    operands = [random.choice(operands), random.choice(range(1, 11))]
    product = operands[0] * operands[1]
    first = random.choice([0,1])
    second = 0 if first == 1 else 1

    answer = operands[second]
    problem = '%d : %d = ?\t____' % (product, operands[first])
    get_and_check_solution(problem, answer)

def division_remainder(operands):
    operands = [random.choice(operands), random.choice(range(1, 11))]
    product = operands[0] * operands[1]
    first = random.choice([0,1])
    second = 0 if first == 1 else 1
    remainder = random.choice(range(0, operands[first]))
    product += remainder
    problem = '%d : %d = %d\tRemainder: ___' % (product, operands[first], operands[second])
    get_and_check_solution(problem, remainder)

def get_and_check_solution(problem, answer):
    attempt = -1
    while attempt != answer:
        attempt = input(random.choice(bgcolors) + problem + Style.RESET_ALL + '  ')
        try:
            attempt = int(attempt)
        except:
            attempt = -1

        if attempt != answer:
            print('')

def main():
    options = get_options() 
    i = 0
    while i < int(options['count']):
        op = random.choice(options['operations'])
        print(op)

        if op == 'add':
            addition(options['addition_range'])
        elif op == 'sub':
            subtraction(options['addition_range'])
        elif op == 'mul':
            multiplication(options['operands'])
        elif op == 'bigmul':
            big_multiplication()
        elif op == 'zeroesmul':
            zeroes_multiplication(options['operands'])
        elif op == 'div':
            division(options['operands'])
        elif op == 'devrem':
            division_remainder(options['operands'])
        else:
            continue

        print(emoji.emojize(random.choice(emojis), use_aliases=True) +
            ' ' + str(int(options['count']) - i - 1) + ' left')
        i = i + 1

    print('Great job ' + options['name'] + '!!!')

if __name__ == "__main__":
    main()
