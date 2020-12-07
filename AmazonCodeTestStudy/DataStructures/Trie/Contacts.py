"""
We're going to make our own Contacts application! The application must perform two types of operations:

add name, where  is a string denoting a contact name. This must store  as a new contact in the application.
find partial, where  is a string denoting a partial name to search the application for. It must count the number of contacts starting with  and print the count on a new line.
Given  sequential add and find operations, perform each operation in order.

Input Format

The first line contains a single integer, , denoting the number of operations to perform.
Each line  of the  subsequent lines contains an operation in one of the two forms defined above.

Constraints

It is guaranteed that  and  contain lowercase English letters only.
The input doesn't have any duplicate  for the  operation.
Output Format

For each find partial operation, print the number of contact names starting with  on a new line.

Sample Input

4
add hack
add hackerrank
find hac
find hak
Sample Output

2
0
Explanation

We perform the following sequence of operations:

Add a contact named hack.
Add a contact named hackerrank.
Find and print the number of contact names beginning with hac. There are currently two contact names in the application and both of them start with hac, so we print  on a new line.
Find and print the number of contact names beginning with hak. There are currently two contact names in the application but neither of them start with hak, so we print  on a new line.
"""

#standard answer
# def contacts(queries):
#     contactList = []
#     counts = []
#     for item in queries:
#         task = item[0]
#         name = item[1]
#         if task == 'add':
#             contactList.append(name)
#         elif task == 'find':
#             count = 0
#             for contact in contactList:
#                 if name in contact:
#                     count += 1
                
#             counts.append(count)
#     return counts





# #Solve using trie
# import fileinput

class Node:
    def __init__(self, children=None, isLeaf=False, count=0):
        if children is None:
            self.children = {}
        else:
            self.children = children
        self.isLeaf = isLeaf
        self.count = count


def add(node, name):
    node.count += 1
    for key in node.children:
        common, extraName1, extraName2 = getPrefix(key, name)
        if extraName1 == '':
            child = node.children[key]
            return add(child, extraName2)
        if common != '':
            child = node.children[key]
            newNode = Node(
                children={extraName1: child},
                count=child.count
            )
            del node.children[key]
            node.children[common] = newNode
            return add(newNode, extraName2)
    node.children[name] = Node(isLeaf=True, count=1)


def find(node, name):
    for key in node.children:
        common, extraName1, extraName2 = getPrefix(key, name)
        if extraName2 == '':
            return node.children[key].count

        if extraName1 == '':
            return find(node.children[key], extraName2)
    return 0


def getPrefix(name1, name2):
    n = 0
    for letter1, letter2 in zip(name1, name2):
        if letter1 != letter2:
            break
        n += 1
    return name1[:n], name1[n:], name2[n:]

def contacts(queries):
    root = Node()
    counts = []
    for item in queries:
        func, name = item
        if func == 'add':
            add(root, name)
        elif func == 'find':
            counts.append(find(root, name))
    return counts


queries = [['add', 'hack'], ['add', 'hackerrank'], ['find', 'hac'], ['find', 'hak']]

print(contacts(queries))
stop = True