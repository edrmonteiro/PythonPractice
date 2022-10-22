from numpy import True_


def palindromeIndex(s):
	rev = s[::-1]
	lst = list(s)
	revlst = list(rev)
	if (rev == s):
		return -1
	else:
		for c,v in enumerate(s):
			if v != rev[c]:
				lst.pop(c)
				revlst.pop(c)
				if (lst != lst[::-1]):
					return (len(s)-c-1)
				if (revlst != revlst[::-1]):
					return (c)
		return -1

s =  'hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh'
print(palindromeIndex(s))
s = 'baa'
print(palindromeIndex(s))
s = 'aaa'
print(palindromeIndex(s))


