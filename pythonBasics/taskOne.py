 # Christmas tree using for loop

'''      

********
 ******
  ****
   **
   **
  ****
 ******
********

        
'''


m = 8

for i in range(m, 1, -2):

    for j in range((m - i) // 2):
        print(" ", end="")

    for k in range(i):
        print("*", end="")

    print()

# Lower part
for i in range(2, m + 1, 2):

    for j in range((m - i) // 2):
        print(" ", end="")

    for k in range(i):
        print("*", end="")

    print()

