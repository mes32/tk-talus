#!/usr/bin/env python3
'''
Random number generator application
'''

import random

# 1. Set range of random integers
min_randint = 1
max_randint = 20

# 2. Generate a random integer
rolled_number = random.randint(min_randint, max_randint)

# 3. Print the number
print(rolled_number)