def anagram2_solution(random_word, dictionary):
    random_word_multiply = calculate_multiply(random_word)
    for dic in dictionary:
        if random_word_multiply % dic[0] == 0:
            return dic[2]
    return ""
    
def create_new_dictionary(dictionary):
    score = 0
    new_dictionary = []
    for word in dictionary:
        multiply = calculate_multiply(word)
        score = count_score(word)
        new_dictionary.append((multiply, score, word))
    new_dictionary = sorted(new_dictionary, reverse=True, key=lambda new_dictionary_tuple: new_dictionary_tuple[1])
    return new_dictionary

def calculate_multiply(word):
    alphabet_num = {
    'a': 2,   'b': 3,   'c': 5,   'd': 7,   'e': 11,
    'f': 13,  'g': 17,  'h': 19,  'i': 23,  'j': 29,
    'k': 31,  'l': 37,  'm': 41,  'n': 43,  'o': 47,
    'p': 53,  'q': 59,  'r': 61,  's': 67,  't': 71,
    'u': 73,  'v': 79,  'w': 83,  'x': 89,  'y': 97,
    'z': 101
    }
    multiply = 1
    for char in word:
        multiply *= alphabet_num[char]
    return multiply
        
def count_score(word):
    score = 0
    
    point1 = ["a", "e", "h", "i", "n", "o", "r", "s", "t"]
    point2 = ["c", "d", "l", "m", "u"]
    point3 = ["b", "f", "g", "p", "v", "w", "y"]
    point4 = ["j", "k", "q", "x", "z"]

    for char in word:
        if char in point1:
            score += 1
        if char in point2:
            score += 2
        if char in point3:
            score += 3
        if char in point4:
            score += 4
            
    return score  

def main():
    with open("../day1/words.txt") as f:
        dictionary = f.readlines()
        for i in range(len(dictionary)):
            dictionary[i] = dictionary[i].replace('\n', '')
    new_dictionay = create_new_dictionary(dictionary)
    
    # with open("../day1/small.txt") as f:
    #     words = f.readlines()
    #     for i in range(len(words)):
    #         words[i] = words[i].replace('\n', '')
    
    # with open("../day1/medium.txt") as f:
    #     words = f.readlines()
    #     for i in range(len(words)):
    #         words[i] = words[i].replace('\n', '')
    
    with open("../day1/large.txt") as f:
        words = f.readlines()
        for i in range(len(words)):
            words[i] = words[i].replace('\n', '')
    
    # print(new_dictionay[:10])
    # with open("../day1/small_hash_answer.txt", "w") as f:
    #     for word in words:
    #         answer = anagram2_solution(word, new_dictionay)
    #         f.write(answer + "\n")  
    
    # with open("../day1/medium_hash_answer.txt", "w") as f:
    #     for word in words:
    #         answer = anagram2_solution(word, new_dictionay)
    #         f.write(answer + "\n")  
            
    with open("../day1/large_hash_answer.txt", "w") as f:
        for word in words:
            answer = anagram2_solution(word, new_dictionay)
            f.write(answer + "\n")  
            
if __name__ == "__main__":
    main()    