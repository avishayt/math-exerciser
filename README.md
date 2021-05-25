# Math Exerciser

This is a simple command-line program written in Python for kids that are learning math.  It has a few flavors of addition, subtraction, multiplication, and division.

It can be run with:
```
python exerciser.py --config config.yaml
```

## Config file format
The config file is a series of key-value pairs in yaml format, and a sample is included in this repository.  The supported keys are:
- name: The name of your child
- count: The number of questions to ask [default 20]
- operands: A comma-separated list of numbers to use as one operand in multiplication questions (the other operand is between 1 and 10) [default 2-9]
- operations: A python-style list (see example), where supported operations are listed below.  Note that an operation may be listed more than once to make it asked more often. [default mul, div]

## Operations
The exerciser currently supports:
- add: Add two 3-digit numbers
- sub: Subtract a number from a 3-digit number
- mul: A multiplication problem with an operand from the list supplied in the config file by a number from 1 to 10. The problem may have the product or one of the operands missing.
- div: A division problem where the operands are as in 'mul'
- bigmul: A multiplication problem where the operands range from 2 to 99
- zeroesmul: A multiplication problem similar to 'mul', but some number of zeroes are appended to the operands
- devrem: A solved division problem is shown and the remainder must be found
