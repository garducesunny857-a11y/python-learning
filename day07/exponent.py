squares = [] #empty list with a label of squares
for value in range(1, 11): #value is a variable that will take on each value in the range of 1 to 10
    square = value ** 3 #square is a variable that will take on the value of value raised to the power of 3
    squares.append(square) #put the value of square into the label squares

print(squares) #printing the value of squares
for square in squares: #square is a variable that will take on each value in the list of squares
    print(square) #printing the value of square