#def bracket_check(section):
#    stringed = [x for x in section]
#    bracket_level = 0
#    for x in range(len(stringed)):
#        if stringed[x] == "(":
#            bracket_level += 1
#            if bracket_level == 1:
#                p_one = x
#        if stringed[x] == ")":
#            bracket_level -= 1
#            if bracket_level == 0:
#                p_two = x
#                segment = [x for x in stringed[p_one+1:p_two]]
#                if "(" or ")" in segment:
#                    bracket_check(segment)

#def evaluate_value(stringed_sum):
#    #division
#    for x in range(len(stringed_sum)):
#        if stringed_sum[x] == "/":
#            if stringed_sum[x] == stringed_sum[x+1]:
#                behind = ""
#                ahead = ""
#                string_chunk = stringed_sum[:x]
#                string_chunk = string_chunk[::-1]
#                for char in string_chunk:
#                    if char.isnumeric() == True:
#                        behind += char
#                    else:
#                        break
#                string_chunk = stringed_sum[x+2:]
#                for char in string_chunk:
#                    if char.isnumeric() == True:
#                        ahead += char
#                    else:
#                        break
#                behind = behind[::-1]
#                total = int(behind) // int(ahead)
#                return (total)

#            else:
#                behind = ""
#                ahead = ""
#                string_chunk = stringed_sum[:x]
#                string_chunk = string_chunk[::-1]
#                for char in string_chunk:
#                    if char.isnumeric() == True:
#                        behind += char
#                    else:
#                        break
#                string_chunk = stringed_sum[x+1:]
#                for char in string_chunk:
#                    if char.isnumeric() == True:
#                        ahead += char
#                    else:
#                        break
#                behind = behind[::-1]
#                total = int(behind) / int(ahead)
#                return(total)

#spa = "50//2"
#spa = [x for x in spa]
#print(evaluate_value(spa))

def sum_splitter(current):
    chunks = {}
    stringed = [x for x in current]
    location = 0
    prev_char = "num"
    for x in stringed:
        if len(chunks) != 0:
            if chunks[location].isnumeric():
                prev_char = "num"
            else:
                prev_char = "str"
        if x.isnumeric() != True and prev_char == "num":
            location += 1
            chunks[location] = x
            pass
        if x.isnumeric() != True and prev_char == "str":
            chunks[location] = chunks[location] + x
            pass
        if x.isnumeric() == True and prev_char != "num":
            location += 1
            chunks[location] = x
            pass
        if x.isnumeric() == True and prev_char == "num":
            if location in chunks.keys():
                chunks[location] = chunks[location] + x
                pass
            else:
                chunks[location] = x
    split = []
    for x in chunks.keys():
        split.append(chunks[x])
    return(split)

def sign_sorter(current):
    split = []
    for x in current:
        if x.isnumeric():
            split.append(x)
        else:
            stringed = [p for p in x]
            temp_list = []
            for z in range(len(stringed)):
                if len(temp_list) != 0:
                    if stringed[z] == "/" and stringed[z] == temp_list[-1]:
                        temp_list[-1] = "//"
                    else:
                        temp_list.append(stringed[z])
                else:
                    if stringed[z] == "x":
                        temp_list.append("*")
                    else:
                        temp_list.append(stringed[z])
            for q in temp_list:
                split.append(q)
    return split

def bracket_valuation(current):
    bracket_level_var = 0
    temp_list = []
    for x in current:
        if x != "(" and x != ")":
            temp_list.append(x)
        else:
            if x == "(":
                bracket_level_var += 1
                temp_list.append({"(" : bracket_level_var})
            if x == ")":
                temp_list.append({")" : bracket_level_var})
                bracket_level_var -= 1
    return temp_list

def plus_minus_sort(current):
    temp_list = []
    for x in current:
        change = False
        if x.isnumeric() == True and change == False:
            temp_list.append(x)
            change = True
        else:
            if x == "-":
                if len(temp_list) == 0 and change == False:
                    temp_list.append(0)
                    temp_list.append(x)
                    change = True
                else:
                    if temp_list[-1] == "-" and change == False:
                        temp_list[-1] = "+"
                        change = True
                    elif temp_list[-1] == "+" and change == False:
                        temp_list[-1] = "-"
                        change = True
            elif x == "+":
                if temp_list[-1] == "-" and change == False:
                    temp_list[-1] = "-"
                    change = True
                if temp_list[-1] == "+" and change == False:
                    temp_list[-1] = "+"
                    change = True
            elif x == "(":
                if temp_list[-1].isnumeric() == True and change == False:
                    temp_list.append("*")
                    temp_list.append(x)
                    change = True
            if change == False:
                temp_list.append(x)
                change = True
    return temp_list


def negative_app(current):
    next_num_neg = False
    new_list = []
    for x in current:
        if x == "-" and new_list[-1].isnumeric() == False and new_list[-1] != "(" and new_list[-1] != ")":
            next_num_neg = True
        else:
            if next_num_neg == True:
                if x.isnumeric() == False:
                    new_list.append("-")
                    new_list.append(x)
                    next_num_neg = False
                else:
                    new_list.append("-" + x)
                    next_num_neg = False
            else:
                new_list.append(x)
    return new_list


#Probably needs rewriting
def bracket_calc(cur_sum):
    temp_list = []
    in_bracket = False
    bracket_level = 0
    range = []
    for x in cur_sum:
        if type(x) == dict:
            if x[")"] == 1:
                in_bracket = False
                temp_list.append(bracket_missile(range, bracket_level+1))
                range = []
                continue
            if x["("] == 1:
                in_bracket = True
                continue
            if in_bracket == True:
                range.append(x)
            else:



    temp_list = []
    in_bracket = False
    bracket = 0
    range = []
    for x in sum:
        if type(x) is dict and x[")"] == 1:
            in_bracket = False
            temp_list.append(bracket_missile(range))
            range = []
        if type(x) is dict and x["("] == 1:
            in_bracket = True
            range[bracket] = x
        else:
            if in_bracket == False:
                temp_list.append(x)
            if in_bracket == True:
                range.append()
    return(temp_list)


def bracket_missile(cur_sum, bracket_leve):


    in_bracket = False
    range = []
    sum_purged = []
    if sum[0].isnumeric() != True:
        sum_purged.append("0")
    for x in cur_sum:
        if x == "(":
            in_bracket = True
            pass
        if x == ")":
            in_bracket = False
            sum_purged.append(bracket_missile(range))
            range = []
            pass
        if in_bracket == True:
            range.append(x)
        if in_bracket == False:
            sum_purged.append(x)
    value = calculation(sum_purged)
    return value


def calculation(sum_purged):
    divide_list = []
    num_used = False
    for x in range(len(sum_purged)):
        if num_used == False:
            if sum_purged[x] == "/" or sum_purged[x] == "//":
                int_one = divide_list[-1]
                int_two = sum_purged[x+1]
                if sum_purged[x] == "/":
                    divide_list[-1] = str(float(int_one) / float(int_two))
                if sum_purged[x] == "//":
                    divide_list[-1] = str(float(int_one) / float(int_two))
                num_used = True
            else:
                divide_list.append(sum_purged[x])
        else:
            num_used = False
    multiply_list = []
    num_used = False
    for x in range(len(divide_list)):
        if num_used == False:
            if divide_list[x] == "*" or divide_list[x] == "x":
                int_one = multiply_list[-1]
                int_two = divide_list[x+1]
                multiply_list[-1] = str(float(int_one) * float(int_two))
                num_used = True
            else:
                multiply_list.append(divide_list[x])
        else:
            num_used = False
    addition_list = []
    num_used = False
    for x in range(len(multiply_list)):
        if num_used == False:
            if multiply_list[x] == "+":
                int_one = addition_list[-1]
                int_two = multiply_list[x+1]
                num_used = True
                addition_list[-1] = str(float(int_one) + float(int_two))
            else:
                addition_list.append(multiply_list[x])
        else:
            num_used = False
    subtraction_list = []
    num_used = False
    for x in range(len(addition_list)):
        if num_used == False:
            if addition_list[x] == "-":
                int_one = subtraction_list[-1]
                int_two = addition_list[x+1]
                subtraction_list[-1] = str(float(int_one) - float(int_two))
                num_used = True
            else:
                subtraction_list.append(addition_list[x])
        else:
            num_used = False
    return subtraction_list

def Calculator(sum):
    sum = bracket_valuation(negative_app(plus_minus_sort(sign_sorter(sum_splitter(sum)))))
    return sum
#print(calculation(["5", "/", "2", "/", "5", "+", "2", "*", "5", "*", "4", "*", "3", "-", "10"]))
print(Calculator("5((20//5)-10)+(1--2)+10x-5"))