def get_position(increment, position, start, end):
    length = end - start + 1
    relative = increment + position - end
    idx = relative % length
    if idx == 0:
        return end  
    return idx + start -1

def get_number(letter, k):
    number = ord(letter)
    if number >= 97 and number <= 122:
        return get_position(k, number, 97, 122)
    if number >= 65 and number <= 90:
        return get_position(k, number, 65, 90)
    return number
    
def caesarCipher(s, k):
    # Write your code here
    s1 = ""
    for letter in s:
        s1 += chr(get_number(letter, k))
    return s1

s = "middle-Outz"
s = "w"
s = "159357lcfd"
#s = "f"
k = 98

# s = "z"
# k = 2
print(caesarCipher(s, k))

print("end")

# ord('a')
# ord('z')


# ord('A')
# ord('Z')


# alfabet1 = [chr(x) for  x in range(97,123)]
# alfabet2 = [chr(x) for  x in range(65,90)]

# (121 + 3)

# 124

# 122-65


increment = 5
position = 121
start = 97
end = 123
print(get_position(increment, position, start, end))
print("end")