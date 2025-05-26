from collections import defaultdict

def anagram2_solution(random_word, dictionary):
    random_word_map = defaultdict(int)
    for char in random_word:
        random_word_map[char] += 1
        
    # res = []
    res = ""
    max_score = 0
    for word in dictionary:
        word_in_dictionary_map = defaultdict(int)
        for char in word:
            word_in_dictionary_map[char] += 1
        
        is_valid = True
        for key in word_in_dictionary_map.keys():
            if word_in_dictionary_map[key] > random_word_map.get(key, 0):
                is_valid = False
                break
        
        if is_valid and max_score <  count_score(word):
            max_score = count_score(word)
            res = word

    return res

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
    
    
    # with open("../day1/small_answer.txt", "w") as f:
    #     for word in words:
    #         answer = anagram2_solution(word, dictionary)
    #         f.write(answer + "\n")  
    
    # with open("../day1/medium_answer.txt", "w") as f:
    #     for word in words:
    #         answer = anagram2_solution(word, dictionary)
    #         f.write(answer + "\n")  
            
    with open("../day1/large_answer.txt", "w") as f:
        for word in words:
            answer = anagram2_solution(word, dictionary)
            f.write(answer + "\n")  
            
if __name__ == "__main__":
    main()