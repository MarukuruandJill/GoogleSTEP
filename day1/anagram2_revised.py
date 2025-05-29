from collections import defaultdict

def anagram2_solution(random_word, dictionary):
    print(random_word)
    random_word_map = {}
    for char in random_word:
        if char in random_word_map.keys():
            random_word_map[char] += 1
        else:
            random_word_map[char] = 1
        
    for dic in dictionary:
        is_valid = True
        for key in dic[0].keys():
            # print("dic[0][key]", dic[0][key])
            # print("random_word_map.get(key, 0)", random_word_map.get(key, 0))
            if int(dic[0][key]) > random_word_map.get(key, 0):
                is_valid = False
                break
        if is_valid:
            return dic[2]  
    return ""

def create_new_dictionary(dictionary):
    score = 0
    new_dictionary = []
    for word in dictionary:
        word_in_dictionary_map = {}
        for char in word:
            if char in word_in_dictionary_map.keys():
                word_in_dictionary_map[char] += 1
            else:
                word_in_dictionary_map[char] = 1
        score = count_score(word)
        new_dictionary.append((word_in_dictionary_map, score, word))
    new_dictionary = sorted(new_dictionary, reverse=True, key=lambda new_dictionary_tuple: new_dictionary_tuple[1])
    return new_dictionary

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
    # with open("../day1/small_revised_answer.txt", "w") as f:
    #     for word in words:
    #         answer = anagram2_solution(word, new_dictionay)
    #         f.write(answer + "\n")  
    
    # with open("../day1/medium_revised_answer.txt", "w") as f:
    #     for word in words:
    #         answer = anagram2_solution(word, new_dictionay)
    #         f.write(answer + "\n")  
            
    new_dictionay = create_new_dictionary(dictionary)
    with open("../day1/large_revised_answer.txt", "w") as f:
        for word in words:
            answer = anagram2_solution(word, new_dictionay)
            f.write(answer + "\n")  
            
if __name__ == "__main__":
    main()