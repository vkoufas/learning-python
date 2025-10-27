"""
Sentence Dictionary

The dictionary contains the unique words of sentence stored as keys and the
number of times they appear in sentence stored as values. 
Use this dictionary to answer the following questions.

1. How many unique words are in sentence_dict?
2. Is the key "sister" in sentence_dict?
3. What is the first element in the list created when sentence_dict is sorted by keys?
Hint: Use the appropriate dictionary method to get a list of its keys, and then
sort that list. 
4. What is the last element in the list created when sentence_dict is sorted by keys?
5. What is the highest value in this dictionary?
"""

sentence_dict = {'as': 2,
                 'he': 2,
                 'crossed': 1,
                 'toward': 1,
                 'the': 4,
                 'pharmacy': 1,
                 'at': 1,
                 'corner': 1,
                 'involuntarily': 1,
                 'turned': 1,
                 'his': 2,
                 'head': 1,
                 'because': 1,
                 'of': 5,
                 'a': 7,
                 'burst': 1,
                 'light': 1,
                 'that': 2,
                 'had': 1,
                 'ricocheted': 1,
                 'from': 2,
                 'temple': 1,
                 'and': 2,
                 'saw': 1,
                 'with': 4,
                 'quick': 1,
                 'smile': 1,
                 'which': 2,
                 'we': 1,
                 'greet': 1,
                 'rainbow': 1,
                 'or': 1,
                 'rose': 1,
                 'blindingly': 1,
                 'white': 1,
                 'parallelogram': 1,
                 'sky': 2,
                 'being': 1,
                 'unloaded': 1,
                 'van—a': 1,
                 'dresser': 1,
                 'mirrors': 1,
                 'across': 2,
                 'cinema': 1,
                 'screen': 1,
                 'passed': 1,
                 'flawlessly': 1,
                 'clear': 1,
                 'reflection': 1,
                 'boughs': 2,
                 'sliding': 1,
                 'swaying': 1,
                 'not': 1,
                 'arboreally': 1,
                 'but': 1,
                 'human': 1,
                 'vacillation': 1,
                 'produced': 1,
                 'by': 1,
                 'nature': 1,
                 'those': 1,
                 'who': 1,
                 'were': 1,
                 'carrying': 1,
                 'this': 2,
                 'these': 1,
                 'gliding': 1,
                 'facade': 1}
print(sentence_dict)

# find number of unique keys in the dictionary
num_keys = len(sentence_dict.keys())
print(num_keys)

# find whether 'sister' is a key in the dictionary
contains_sister = "sister" in sentence_dict
print(contains_sister)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(sentence_dict.keys())

# get the first element in the sorted list of keys
print(min(sorted_keys))

# get the last element in the sorted list of keys
print((max(sorted_keys)))

# find the highest value
print(max(sentence_dict.values()))