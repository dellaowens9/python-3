import csv 


def create_files(file):
    word_list = [] 
    word_count = 0
    with open(file) as words:
        rows = csv.reader(words, delimiter=" ")
        for row in rows:
            for x in row:
                if x != "" and x not in word_list:
                    word_count += 1
                    word_list.append(x)
                    
    

    with open("large_word.txt", "w") as large_word_file:
        for word in word_list:
            if len(word) > 3:
                large_word_file.writelines(word + '\n') 
    
    with open("small_word.txt", "w") as small_word_file:
        for word in word_list:
            if len(word) < 3:
                small_word_file.writelines(word + '\n')
                
    return word_count

def ex3():
    total_words = create_files("words.txt")
    print(f"Total words: {total_words}.")

ex3()