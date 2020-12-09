"""
8-Reverse-words-in-a-sentence
Reverse the order of words in a given sentence (an array of characters). 
Click here to view the solution in C++, Java, JavaScript, and Ruby.
"Hello World" -> "World Hello"
"""


def str_rev(str, start, end):
  if str == None or len(str) < 2:
    return

  while start < end:
    temp = str[start]
    str[start] = str[end]
    str[end] = temp

    start += 1
    end -= 1


def reverse_words(sentence):

  # Here sentence is a null-terminated string ending with char '\0'.

  if sentence == None or len(sentence) == 0:
    return

  #  To reverse all words in the string, we will first reverse
  #  the string. Now all the words are in the desired location, but
  #  in reverse order: "Hello World" -> "dlroW olleH".

  str_len = len(sentence)
  str_rev(sentence, 0, str_len - 2)

  # Now, let's iterate the sentence and reverse each word in place.
  # "dlroW olleH" -> "World Hello"

  start = 0
  end = 0

  while True:

  # find the  start index of a word while skipping spaces.
    while start < len(sentence) and sentence[start] == ' ':
      start += 1

    if start == str_len:
      break

  # find the end index of the word.
    end = start + 1
    while end < str_len and sentence[end] != ' ':
      end += 1

  # let's reverse the word in-place.
    str_rev(sentence, start, end - 1)
    start = end


def get_array(t):
  # s = array('u', t)
  s = t.split()
  return s


def print_array(s):
  i = 0
  while i != len(s):
    print(s[i])
    i += 1
  print ()


s = get_array('Hello World!')
print_array(s)
reverse_words(s)
print_array(s)

stop = True