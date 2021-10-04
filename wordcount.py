"""Count words in file."""
test_file = open("test.txt")
word_count = {} 
def make_word_count_dict(test_file):
    for line in test_file:
        line = line.rstrip()
        words = line.split()
        for word in words: 
            word_count[word] = word_count.get(word,0) + 1
    return word_count
    
word_count = make_word_count_dict (test_file)
# # print(word_count)
for word, count in word_count.items():
    print(f'{word}: {count}')
