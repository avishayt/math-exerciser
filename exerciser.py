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
               'operations': ['mul', 'div'],
               'bigmulmaxop1': 999,
               'bigmulmaxop2': 9}

    if args.config:
        with open(args.config, 'r') as ymlfile:
            cfg = yaml.safe_load(ymlfile)

        if 'name' in cfg:
            options['name'] = cfg['name']
        if 'count' in cfg:
            options['count'] = int(cfg['count'])
        if 'operands' in cfg:
            options['operands'] = cfg['operands']
        if 'bigmulmaxop1' in cfg:
            options['bigmulmaxop1'] = int(cfg['bigmulmaxop1'])
        if 'bigmulmaxop2' in cfg:
            options['bigmulmaxop2'] = int(cfg['bigmulmaxop2'])
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
    problem = '%s\n- %s\n  ___' % (str(bigger).rjust(5), str(smaller).rjust(3))
    get_and_check_solution(problem, answer)

def multiplication(operands1, operands2):
    operands = [random.choice(operands1), random.choice(operands1)]
    product = operands[0] * operands[1]
    first = random.choice([0,1])
    second = 0 if first == 1 else 1

    variable = random.choice([0,4])
    if variable == 0:
        answer = operands[first]
        problem = '? X %d = %d' % (operands[second], product)
    elif variable == 1:
        answer = operands[second]
        problem = '%d X ? = %d' % (operands[first], product)
    else:
        answer = product
        problem = '%d X %d = ?' % (operands[first], operands[second])

    get_and_check_solution(problem, answer)

def big_multiplication(operands1, operands2):
    operands = [random.choice(operands1), random.choice(operands2)]
    answer = operands[0] * operands[1]
    problem = '%s\nX %s\n  ___' % (str(operands[0]).rjust(5), str(operands[1]).rjust(3))
    get_and_check_solution(problem, answer)

def zeroes_multiplication(operands):
    operands = [random.choice(operands), random.choice(range(1, 11))]
    operands[0] = operands[0] * (10 ** random.choice(range(0, 3)))
    operands[1] = operands[1] * (10 ** random.choice(range(0, 3)))
    answer = operands[0] * operands[1]
    problem = '%d X %d = ?' % (operands[0], operands[1])
    get_and_check_solution(problem, answer)

def division(operands):
    operands = [random.choice(operands), random.choice(range(1, 11))]
    product = operands[0] * operands[1]
    first = random.choice([0,1])
    second = 0 if first == 1 else 1

    answer = operands[second]
    problem = '%d : %d = ?\t' % (product, operands[first])
    get_and_check_solution(problem, answer)

def division_remainder(operands):
    operands = [random.choice(operands), random.choice(range(1, 11))]
    product = operands[0] * operands[1]
    first = random.choice([0,1])
    second = 0 if first == 1 else 1
    remainder = random.choice(range(0, operands[first]))
    product += remainder
    problem = '%d : %d = %d\tRemainder: ?' % (product, operands[first], operands[second])
    get_and_check_solution(problem, remainder)

def fraction_string(whole_number, numerator, denominator):
    filled = u'\u25AE'
    unfilled = u'\u25AF'

    s = ""
    for i in range(0, whole_number):
        for j in range(0, denominator):
            s = s + filled
        s = s + '  '

    for i in range(0, numerator):
        s = s + filled
    for i in range(0, denominator - numerator):
        s = s + unfilled

    return s

def fraction_identify():
    whole_number = random.choice(range(1, 5))
    denominator = random.choice(range(2, 10))
    numerator = random.choice(range(1, denominator))
    filled = u'\u25AE'
    unfilled = u'\u25AF'

    problem = fraction_string(whole_number, numerator, denominator)

    get_and_check_solution(problem, '%s %s/%s' % (whole_number, numerator, denominator), answer_type=str)

def fraction_conversion():
    whole_number = random.choice(range(1, 5))
    denominator = random.choice(range(2, 10))
    numerator = random.choice(range(1, denominator))
    improper_numerator = (whole_number * denominator) + numerator
    to_improper = random.choice([0, 1])

    print(fraction_string(whole_number, numerator, denominator))

    if to_improper == 1:
        get_and_check_solution('%d %d/%d = ?' % (whole_number, numerator, denominator), '%s/%s' % (improper_numerator, denominator), answer_type=str)
    else:
        get_and_check_solution('%d/%d = ?' % (improper_numerator, denominator), '%s %s/%s' % (whole_number, numerator, denominator), answer_type=str)

def get_and_check_solution(problem, answer, answer_type=int):
    attempt = -1
    while attempt != answer:
        attempt = input(random.choice(bgcolors) + problem + Style.RESET_ALL + '\n')
        try:
            attempt = answer_type(attempt)
        except:
            attempt = -1

        if attempt != answer:
            print('')

def main():
    options = get_options() 
    i = 0
    while i < int(options['count']):
        op = random.choice(options['operations'])

        if op == 'add':
            addition(options['addition_range'])
        elif op == 'sub':
            subtraction(options['addition_range'])
        elif op == 'mul':
            multiplication(options['operands'], range(1, 11))
        elif op == 'bigmul':
            big_multiplication(range(2,options['bigmulmaxop1']), range(2,options['bigmulmaxop2']))
        elif op == 'zeroesmul':
            zeroes_multiplication(options['operands'])
        elif op == 'div':
            division(options['operands'])
        elif op == 'devrem':
            division_remainder(options['operands'])
        elif op == 'fracident':
            fraction_identify()
        elif op == 'fracconv':
            fraction_conversion()
        else:
            continue

        print(emoji.emojize(random.choice(emojis), use_aliases=True) +
            ' ' + str(int(options['count']) - i - 1) + ' left\n')
        i = i + 1

    print('Great job ' + options['name'] + '!!!')

if __name__ == "__main__":
    main()
