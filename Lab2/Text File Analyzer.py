def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

#open and read the txt file
content = read_file('sample.txt')
print(content[:200])  # Print the first 200 words

def count_lines(content):
    return len(content.split('\n'))

#count the number of lines
num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

#count the number of words
def count_words(content):
    return len(content.split())


num_words = count_words(content)
print(f"Number of words: {num_words}")

#finding the most commom words
from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

# how many times it appeared 
common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")

#calculate average word length
def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")

#combine everything into main function
def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")


analyze_text('sample.txt')



#unique words

def count_unique_words(content):
    words = content.split()
    unique_words = set(words)
    unique_word_count = len(unique_words)
    
    return unique_word_count
print("Number of unique words:", count_unique_words(content))

#longest words
def longest_word(content):
    words = content.split()
    longest_word = set(words)
    longest_word_count = len(longest_word)
    return max(words, key=len)
print("longest word:", longest_word(content))

#occurance of a specfic words
def count_specific_word(content):
    words = content.split()
    count_specific_word = set(words)
    count_specific_word_count = len(count_specific_word)
    return count
print("occurance of specific words:", count_specific_word(content))

#Calculate the percentage of words longer than the average length
def percentage_long_words(content):
    words = content.split()
    avg_length = average_word_length(content)
    long_words = [word for word in words if len(word) > avg_length]
    return (len(long_words) / len(words)) * 100
print("percentages:", percentage_long_words(content))





def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    unique_words = count_unique_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    longest = longest_word(content)
    specific_word_count = count_specific_word(content)
    long_words_percentage = percentage_long_words(content)

    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print("Number of unique words:", count_unique_words(content))
    print("longest word:", longest_word(content))
    print("occurance of specific words:", count_specific_word(content))
    print("percentages:", percentage_long_words(content))


   
# Run the analysis
analyze_text('sample.txt')
