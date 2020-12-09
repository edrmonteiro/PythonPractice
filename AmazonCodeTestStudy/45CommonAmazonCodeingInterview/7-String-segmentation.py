"""
7. String segmentation
You are given a dictionary of words and a large input string. 
You have to find out whether the input string can be completely segmented into the words of a given dictionary. 
The following two examples elaborate on the problem further. Click here to view the solution in C++, Java, JavaScript, and Ruby.

Given a dictionary of words
Apple apple pear pie

input string of "applepie" an be segmented into dictionary words (apple and pie)
apple pie 

input string of "applepeer" cannot be segmented into dictionary words.
apple peer 
"""
def can_segment_string(s, dictionary):
  for i in range(1, len(s) + 1):
    first = s[0:i]
    if first in dictionary:
      second = s[i:]
      if not second or second in dictionary or can_segment_string(second, dictionary):
        return True
  return False
  
s = "hellonow"
dictionary= set(["hello","hell","on","now"])
if can_segment_string(s, dictionary):
  print("String Can be Segmented")
else:
  print("String Can NOT be Segmented")

stop = True


"""
Runtime Complexity: Exponential, O(2^n)
Memory Complexity: Polynomial, O(n^2)
You can solve this problem by segmenting the large string at each possible position to see if the string can be completely segmented to words in the dictionary. 
If you write the algorithm in steps, it will be as follows:
n = length of input string
for i = 0 to n - 1
  first_word = substring (input string from index [0, i] )
  second_word = substring (input string from index [i + 1, n - 1] )
  if dictionary has first_word
    if second_word is in dictionary OR second_word is of zero length, then return true
    recursively call this method with second_word as input and return true if it can be segmented
The algorithm will compute two strings from scratch in each iteration of the loop. Worst case scenario, 
there would be a recursive call of the second_word each time. This shoots the time complexity up to 2^n. 
You can see that you may be computing the same substring multiple times, even if it doesn’t exist in the dictionary. 
This redundancy can be fixed by memoization, where you remember which substrings have already been solved. 
To achieve memoization, you can store the second string in a new set each time. This will reduce both time and memory complexities.
"""

