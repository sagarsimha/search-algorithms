Exercise 1. Rock Paper Scissors

Task:
• Write a Python 3 script which lets a user play “rock-paper-scissors” against the computer
• It should read the standard input for either “stone”, “paper”, “scissors” and generate a random
response
• The selection of both the user and the script should be displayed on the console
• Additionally, the game should run in a loop, asking for another round
• Count the amount of wins / losses for the user and the computer and print the count after each
round

Exercise 2. Numpy 1
a) import numpy
b) create an array a with values from 1 to 3
c) create an array b with random values between 0 and 100 of length 3
d) multiply a with b
e) calculate the dot product of a and b
f) calculate the cross product of a and b

Exercise 3. Numpy 2
a) create a matrix x with random values from 1 to 100 of shape 10x10
b) calculate the determinant of x

Exercise 4. Numpy 3
a) implement a function that gets a numpy array as argument
b) the function should change every even value to its negative
# input
array
np.array ([1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9])
# output
array
np.array([1, − 2,3, − 4,5, − 6,7, − 8,9])

Exercise 5. Numpy 4
a) write a function that has two numpy arrays as arguments
b) the function should return an numpy array of all elements that are shared between both input
arrays
# input
np.array ([1 ,2 ,3 ,4 ,5 ,6 ,7]) ,
np.array ([23 ,12 ,76 ,23 ,1 ,45 ,5])
#output
np.array ([1 ,5])