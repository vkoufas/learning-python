"""
Count Unique Words

Find the number of unique words in the text.
Complete these three steps to get your answer:
1. Split sentence into a list of words. 
Hint: You can use a string method you learned in the previous lesson.
2. Convert the list into a data structure that would keep only the unique
elements from the list.
3. Print the length of the container.
"""

sentence = 'as he crossed toward the pharmacy at the corner he involuntarily turned his head because of a burst of light that had ricocheted from his temple and saw with that quick smile with which we greet a rainbow or a rose a blindingly white parallelogram of sky being unloaded from the van—a dresser with mirrors across which as across a cinema screen passed a flawlessly clear reflection of boughs sliding and swaying not arboreally but with a human vacillation produced by the nature of those who were carrying this sky these boughs this gliding facade'
print(sentence)

# split sentence into list of words
sentence_list = sentence.split()
print(sentence_list)

# convert list to set to get unique words
sentence_set = set(sentence_list)
print(sentence_set)

# print the number of unique words
num_unique = len(sentence_set)
print(num_unique)