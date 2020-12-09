"""
9-How-many-ways can-you-make change-with-coins-and-a-total-amount

Suppose we have coin denominations of [1, 2, 5] and the total amount is 7. 
We can make changes in the following six ways. Click here to view the solution in C++, Java, JavaScript, and Ruby.
"""
def solve_coin_change(denominations, amount):
  solution = [0] * (amount + 1)
  solution[0] = 1
  for den in denominations:
    for i in range(den, amount + 1):
      solution[i] += solution[i - den] 

  return solution[len(solution) - 1]
    
denominations = [1, 2, 5]
amount = 7
result = solve_coin_change(denominations, amount)
# printing the answer
print("solve_coin_change(" + str(denominations) + ', ' + str(amount) + ') = ', end = '' )
print(result)

stop = True

"""
Runtime Complexity: Quadratic, O(m∗n)
Memory Complexity: Linear, O(n)
To solve this problem, we’ll keep an array of size amount + 1. One additional space is reserved because we also want to store the solution for the 0 amount. 
There is only one way you can make a change of 0, i.e., select no coin, so we’ll initialize solution[0] = 1. 
We’ll solve the problem for each amount, denomination to amount, using coins up to a denomination, den. 
The results of different denominations should be stored in the array solution. The solution for amount x using a denomination den will then be:
solution[x] = solution[x] + solution[x - den]
We’ll repeat this process for all the denominations, and at the last element of the solution array, we will have the solution.
"""