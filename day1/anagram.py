def anagram_solution(random_word, dictionary):
    sorted_random_word = ''.join(sorted(random_word))
    
    new_dictionary = []
    for word in dictionary:
        new_dictionary.append((''.join(sorted(word)), word))
    new_dictionary = sorted(new_dictionary, key=lambda word_tuple: word_tuple[0])
    anagram = binary_search(sorted_random_word, new_dictionary)
    return anagram

def binary_search(word, dictionary):
    anagrams = []
    left, right = 0, len(dictionary)-1
    while left <= right:
        mid = (left + right) // 2
        mid_word_tuple = dictionary[mid]
        mid_word_sorted = mid_word_tuple[0]
        if mid_word_sorted < word:
            left = mid + 1
        elif word < mid_word_sorted:
            right = mid - 1
        else:
            anagrams.append(mid_word_tuple[1])
            #周辺を探索
            upper = mid + 1
            lower = mid - 1
            while upper < len(dictionary) and word == dictionary[upper][0]:
                anagrams.append(dictionary[upper][1])
                upper += 1
        
            while lower < len(dictionary) and word == dictionary[lower][0]:
                anagrams.append(dictionary[lower][1])
                lower -= 1
            break

    return anagrams

def main():
    with open("../day1/words.txt") as f:
        dictionary = f.readlines()
        for i in range(len(dictionary)):
            dictionary[i] = dictionary[i].replace('\n', '')
        print(anagram_solution("tabob", dictionary))
        print(anagram_solution("uabseotl", dictionary))
        print(anagram_solution("baccalaureates", dictionary))
        
if __name__ == "__main__":
    main()
    
    