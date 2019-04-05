

# Array of string representations for numeric "places"
_ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
_teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
_tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
_hundreds = ["hundred", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion"]

# ASCII ordinal letter conversion constant
_ordinal_conv = 97


# Utility method for breaking "triples" into arrays for processing
def get_triple_array(number):
    num_string = str(number)
    # If length is 3, use list comprehension for faster processing
    if len(num_string) == 3:
        return [int(n) for n in list(num_string)]
    else:
        # length is less than three, requires padding elements
        triple = [0, 0, 0]
        sentinel = 0
        for i in range(0, 3):
            if i < 3 - len(num_string):
                triple[i] = 0
            else:
                triple[i] = int(num_string[sentinel])
                sentinel = sentinel + 1
        return triple


# Utility method to "stringify" the triple
def stringify_triple(triple, group_index):
    string_array = ["", "", "", ""]
    for i in range(0, 3):
        if i == 0:
            if triple[0] != 0:
                string_array[0] = f"{_ones[triple[0]]}{_hundreds[0]}"
        if i == 1:
            if triple[1] == 1:
                string_array[1] = f"{_teens[triple[2]]}"
            else:
                string_array[1] = f"{_tens[triple[1]]}"
                string_array[2] = f"{_ones[triple[2]]}"
    # CHECK THIS
    if group_index > 1 and (string_array[0] != "" or string_array[1] != "" or string_array[2] != "" ):
        string_array[3] = _hundreds[group_index - 1]
    return str("".join(string_array))


# Utility method to return the base during integer parsing
def get_base(thousandth):
    return int(100 ** (thousandth - 1) * (10 ** (thousandth - 1)))


# Utility to parse the full integer of arbitrary length
def parse_integer(in_int):
    output_str_array = []
    place_count = len(str(in_int))
    triple_count = int(place_count / 3 if place_count % 3 == 0 else (place_count / 3) + 1)
    while triple_count > 0:
        base = get_base(triple_count)
        triple_num = int(in_int / base)
        output_str_array.append(stringify_triple(get_triple_array(triple_num), triple_count))
        in_int = in_int - (triple_num * base)
        triple_count = triple_count - 1
    return "".join(output_str_array)

# Join the complete word list
def construct_complete_string(lower, upper):
    complete = []
    for i in range(lower, upper + 1):
        complete.append(parse_integer(i))
    return "".join(complete)

# Get the probability of arbitrary letter in the complete string
def get_prob(check, in_str):
    letter_counts = []
    for i in range(0, 26):
        letter_counts.append(0)
    for c in in_str:
        char_curr = ord(c) - _ordinal_conv
        letter_counts[char_curr] = letter_counts[char_curr] + 1
    return letter_counts[ord(check) - _ordinal_conv] / len(in_str)


# Utility to round and beautify percentage
def pretty_percent(percent):
    return f"{round(percent, 4) * 100}%"


# Get the max precision "raw" probability
def get_raw_answer(the_char, the_lownum, the_highnum):
    return get_prob(the_char, construct_complete_string(the_lownum, the_highnum))


# Wrapper to prettify the percentage
def get_answer(the_char, the_lownum, the_highnum):
    return pretty_percent(get_prob(the_char, construct_complete_string(the_lownum, the_highnum)))


#Testing
print(get_answer('q', 999999999999999, 1000000000000001))
print(parse_integer(1000000000000001))
print(parse_integer(1002003004005001))
