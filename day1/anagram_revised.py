from collections import defaultdict


def anagram_solution(random_word, dictionary):
    sorted_random_word = ''.join(sorted(random_word))
    return dictionary[sorted_random_word]

def create_new_dictionary(dictionary):
    new_dictionary = defaultdict(list)
    for word in dictionary:
        sorted_word = ''.join(sorted(word))
        new_dictionary[sorted_word].append(word)
    return new_dictionary

def main():
    with open("../day1/words.txt") as f:
        dictionary = f.readlines()
        for i in range(len(dictionary)):
            dictionary[i] = dictionary[i].replace('\n', '')
    new_dictionary = create_new_dictionary(dictionary)
    print(anagram_solution("tabob", new_dictionary))
    print(anagram_solution("uabseotl", new_dictionary))
    print(anagram_solution("baccalaureates", new_dictionary))
        
if __name__ == "__main__":
    main()