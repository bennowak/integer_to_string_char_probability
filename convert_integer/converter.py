ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = ["hundred", "thousand", "million", "trillion"]


def get_num_string(numarr, num):
    return numarr[num]


def get_triple_array(number):
    num_string = str(number)
    triple = [0, 0, 0]
    sentinel = 0
    for i in range(0, 3):
        if i < 3 - len(num_string):
            triple[i] = 0
        else:
            triple[i] = int(num_string[sentinel])
            sentinel = sentinel + 1
    return triple


def stringify_triple(triple, group_index):
    string_array = ["", "", "", ""]
    for i in range(0, 3):
        if i == 0:
            if triple[0] != 0:
                string_array[0] = f"{ones[triple[0]]}{hundreds[0]}"
        if i == 1:
            if triple[1] == 1:
                string_array[1] = f"{teens[triple[2]]}"
            else:
                string_array[1] = f"{tens[triple[1]]}"
                string_array[2] = f"{ones[triple[2]]}"
    if group_index > 1 and (string_array[0] != "" or string_array[1] != "" or string_array[2] != "" ):
        string_array[3] = hundreds[group_index - 1]
    return str("".join(string_array))


def get_base(thousandth):
    return int(100 ** (thousandth - 1) * (10 ** (thousandth - 1)))


def parse_integer(in_int):
    output_str_array = []
    place_count = len(str(in_int))
    triple_count = int(place_count / 3 if place_count % 3 == 0 else (place_count / 3) + 1)

    while triple_count > 0:
        base = get_base(triple_count)
        triple_num = int(in_int / base)
        output_str_array.append(stringify_triple(get_triple_array(triple_num), triple_count))
        # print("-------------------------")
        # print(f"in_int = {in_int}")
        # print(f"base = {base}")
        # print(f"triple_num = {triple_num}")
        in_int = in_int - (triple_num * base)
        triple_count = triple_count - 1
    return "".join(output_str_array)


def construct_complete_string(lower, upper):
    complete = []
    for i in range(lower, upper + 1):
        complete.append(parse_integer(i))
    return "".join(complete)
