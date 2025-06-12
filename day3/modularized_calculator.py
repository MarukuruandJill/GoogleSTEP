
#! /usr/bin/python3

def read_number(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        decimal = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * decimal
            decimal /= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def read_plus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1

def read_minus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def read_multiply(line, index):
    token = {'type': 'MULTIPLY'}
    return token, index + 1

def read_divide(line, index):
    token = {'type': 'DIVIDE'}
    return token, index + 1

def read_opening_parentheses(line, index):
    token = {'type': 'OPENING_PARENTHESES'}
    return token, index + 1

def read_closing_parentheses(line, index):
    token = {'type': 'CLOSING_PARENTHESES'}
    return token, index + 1

def read_abs(line, index):
    token = {'type': 'ABS'}
    return token, index + 3

def read_int(line, index):
    token = {'type': 'INT'}
    return token, index + 3

def read_round(line, index):
    token = {'type': 'ROUND'}
    return token, index + 5

def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = read_number(line, index)
        elif line[index] == '+':
            (token, index) = read_plus(line, index)
        elif line[index] == '-':
            (token, index) = read_minus(line, index)
        elif line[index] == '*':
            (token, index) = read_multiply(line, index)
        elif line[index] == '/':
            (token, index) = read_divide(line, index)
        elif line[index] == '(':
            (token, index) = read_opening_parentheses(line, index)
        elif line[index] == ')':
            (token, index) = read_closing_parentheses(line, index)
        elif line[index:index+3] == 'abs':
            (token, index) = read_abs(line, index)
        elif line[index:index+3] == 'int':
            (token, index) = read_int(line, index)
        elif line[index:index+5] == 'round':
            (token, index) = read_round(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens

# evaluate only multiply and divide
def evaluate_multiply_and_divide(tokens):
    index = 0
    while index < len(tokens):
        if index + 2 < len(tokens) and tokens[index]['type'] == 'NUMBER':
            if tokens[index + 1]['type'] == 'MULTIPLY' or tokens[index + 1]['type'] == 'DIVIDE':
                if tokens[index + 1]['type'] == 'MULTIPLY':
                    result = tokens[index]['number'] * tokens[index + 2]['number']
                else:
                    result = tokens[index]['number'] / tokens[index + 2]['number']
                tokens[index:index + 3] = [{'type': 'NUMBER', 'number': result}]
                continue
        index += 1
    return tokens

# evaluate only plus and minus
def evaluate_plus_and_minus(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index-1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            if tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
        index += 1
    return answer

# evaluate inside the parentheses
def evaluate_parentheses(tokens):
    index = 0
    inside_parentheses = []
    start_indexes = []
    while index < len(tokens):
        if tokens[index]['type'] == 'OPENING_PARENTHESES':
            start_indexes.append(index)
            index += 1
            while tokens[index]['type'] != 'OPENING_PARENTHESES' and tokens[index]['type'] != 'CLOSING_PARENTHESES':
                inside_parentheses.append(tokens[index])
                index += 1
            if tokens[index]['type'] == 'CLOSING_PARENTHESES':
                inside_result = evaluate(inside_parentheses)
                popped_index = start_indexes.pop()
                tokens[popped_index:index + 1] = [{'type': 'NUMBER', 'number': inside_result}]
                if start_indexes:
                    index = start_indexes.pop()
                else:
                    index = popped_index + 1
            inside_parentheses = []
        else:
            index += 1   
    return tokens

# evaluate inside the parentheses
def evaluate_parentheses2(tokens):
    index = 0
    tmp_tokens = []
    while index < len(tokens):
        if tokens[index]['type'] == 'CLOSING_PARENTHESES':
            closing_index = index
            index -= 1
            while tokens[index]['type'] != 'OPENING_PARENTHESES':
                tmp_tokens.insert(0, tokens[index])
                index -= 1
            if tokens[index]['type'] == 'OPENING_PARENTHESES':
                result = evaluate(tmp_tokens)
                tokens[index:closing_index+1] = [{'type': 'NUMBER', 'number': result}]
                tmp_tokens = []
        index += 1          
    return tokens

# evaluate abs, int, and round function
def evaluate_abs_int_round(tokens):
    index = 0
    while index < len(tokens):
        if tokens[index]['type'] == 'ABS':
            result = abs(tokens[index+1]['number'])
            tokens[index:index+2] = [{'type': 'NUMBER', 'number': result}]
        if tokens[index]['type'] == 'INT':
            result = int(tokens[index+1]['number'])
            tokens[index:index+2] = [{'type': 'NUMBER', 'number': result}]
        if tokens[index]['type'] == 'ROUND':
            result = round(tokens[index+1]['number'])
            tokens[index:index+2] = [{'type': 'NUMBER', 'number': result}]
        index += 1
    return tokens


def evaluate(tokens):
    tmp_tokens = evaluate_parentheses(tokens)
    tmp_tokens = evaluate_abs_int_round(tmp_tokens)
    tmp_tokens = evaluate_multiply_and_divide(tmp_tokens)
    answer = evaluate_plus_and_minus(tmp_tokens)        
    return answer


def test(line):
    tokens = tokenize(line)
    actual_answer = evaluate(tokens)
    expected_answer = eval(line)
    if abs(actual_answer - expected_answer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expected_answer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expected_answer, actual_answer))


# Add more tests to this function :)
def run_test():
    print("==== Test started! ====")
    test("1+2")
    test("1.0+2.1-3")
    test("2-1")
    test("2.3*5.4")
    test("2/4")
    test("3.0+4*2-1/5")
    test("4/2/2+5+6*3/2")
    test("3+6/3*2-4")
    test("5.6*3.2*5+46-67+56/4/4")
    test("(3.0+4*(2-1))/5")
    test("12+abs(int(round(-1.55)+abs(int(-2.3+4))))")
    test("(3*4/2)+5*6+8/4")
    test("(2-1+3)+(8-2)")
    test("(2-1)+(8-2)")
    test("(2-1)+(7-8/2)-7")
    test("-1+4")
    test("abs(234*54-67-78/3)*int(67/8*2)+round(34/5*4-3)")
    print("==== Test finished! ====\n")

run_test()

while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)
