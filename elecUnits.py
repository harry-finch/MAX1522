# Library 

import math
import re

# Converts a very large or very small number into a more readable prefix notation (string).
# unitPrefix(1000)      => returns 10.0K
# unitPrefix(0.000001)  => returns 1.0µ

def unitPrefix(num):
    sciNotation = format(num, "10.2E")
    splitSciNotation = sciNotation.split('E')

    value = float(splitSciNotation[0])
    multiplier = int(splitSciNotation[1])

    prefixes = {
        8: "M",
        7: "M",
        6: "M",
        5: "K",
        4: "K",
        3: "K",
        2: "",
        1: "",
        -1: "m",
        -2: "m",
        -3: "m",
        -4: "µ",
        -5: "µ",
        -6: "µ",
        -7: "n",
        -8: "n",
        -9: "n",
        -10: "p",
        -11: "p",
        -12: "p"
    }

    remainder = multiplier%3
    if remainder>0: value = round(value * pow(10,remainder))

    return str(value)+prefixes[multiplier]    

# Converts a prefix notation to a float.
# prefixToValue("10K") => returns 1000
# prefixToValue("1µ")  => returns 0.000001
# Returns None if string is empty

def prefixToValue(numStr):
    try: return float(numStr)
    except ValueError: 
        prefix = numStr[-1:]
        numStr = numStr[:-1]

        try: value = float(re.findall('\d+', numStr)[0])
        except IndexError: return None

        prefixValues = {
            "M": 1000000,
            "K": 1000,
            "m": 0.001,
            "µ": 0.000001,
            "n": 0.000000001,
            "p": 0.000000000001
        }

        return value * prefixValues[prefix]

# Converts a prefix notation (string) - including the unit - to a float.
# prefixAndUnitToValue("10KV") => returns 1000
# prefixAndUnitToValue("1µA")  => returns 0.000001
# Returns None if string is empty

def prefixAndUnitToValue(numStr):
        numStr = numStr[:-1]
        return prefixToValue(numStr)

