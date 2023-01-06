#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
even = n % 2 == 0
valid_range = 2<=n<=5
not_valid_range = 6 <= n <= 20
if not even:
    print("Weird")
elif even and valid_range:
    print("Not Weird")
elif even and not_valid_range:
    print("Weird")
else:
    print("Not Weird")
