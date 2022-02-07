import sys
from TowerOfHanoi import *

def main():
	n = int(sys.argv[1]) if len(sys.argv) == 2 and sys.argv[1].isnumeric() else 3
	solution = S({"L","C","R"}, {"L"}, {"R"}, n)
	print("solution: ", solution)
	puzzle = TowerOfHanoi(n)
	print(puzzle)
	for operation in solution:
		print("**********************")
		print("operation: ", operation)
		puzzle.execute(operation)
		print("----------------------")
		print(puzzle)
	print("COMPLETE!")
		
	

#HANOI'S FUNCTION
def S(U, F, T, n):
	if n == 1:
		return [list(F) + list(T)]
	return S(U, F, U - (F | T), n - 1) + [list(F) + list(T)] + S(U, U - (F | T), T, n - 1)


main()












"""
HANOI's TOWER

PROBRAM: move the disks (represented by numbers) from the L column to the R column
         without stacking a large disk on a small disk

START             END

1                   1
2                   2
3                   3
L C R           L C R




HANOI TOWER SOLUTIONS PLOT by number of disks (discovered by investigation and program assistance to help keep track of operations)

#DISKS                                                                                                      OPERATIONS

1    														                                                 ['L,R']
2    							                     ['L,C',                                                  'L,R',                                                  'C,R']
3    			         ['L,R',                      'L,C',                      'R,C',                      'L,R',                      'C,L',                      'C,R',                      'L,R']
4    	   ['L,C',        'L,R',        'C,R',        'L,C',        'R,L',        'R,C',        'L,C',        'L,R',        'C,R',        'C,L',        'R,L',        'C,R',        'L,C',        'L,R',        'C,R']
5   ['L,R', 'L,C', 'R,C', 'L,R', 'C,L', 'C,R', 'L,R', 'L,C', 'R,C', 'R,L', 'C,L', 'R,C', 'L,R', 'L,C', 'R,C', 'L,R', 'C,L', 'C,R', 'L,R', 'C,L', 'R,C', 'R,L', 'C,L', 'C,R', 'L,R', 'L,C', 'R,C', 'L,R', 'C,L', 'C,R', 'L,R']

notice the length of the operation sequence for each row

#DISKS
1       1
2       3
3       7
4       15
5       31

BINARY TREES ALSO HAVE SIMILAR property
we also see similaraties accross the rows of the plot of HANOI TOWER SOLUTIONS
this hints of recursion (even when playing the game, we can see recursive)

turns out its a INORDER BINARY TREE TRAVERSAL, we can illustrate this with some of
the trees

recall inorder traversal is: left ROOT right





                                                      1 DISK
                                                       
														 LR


inorder traversal for 1 DISK : LR


                                                      2 DISKS
                                                       
														 LR
														/  \
													   /    \
													  /      \
			                                         /        \
		                                            /          \
		                                           /            \
                                                  /              \
                                                 /                \
												LC                CR



inorder traversal for 2 DISKS: 'L,C',   'L,R',   'C,R'

                                                      3 DISKS
                                                       
														 LR
														/  \
													   /    \
													  /      \
			                                         /        \
		                                            /          \
		                                           /            \
                                                  /              \
                                                 /                \
												LC                CR
											   /  \              /  \
											  /    \            /    \
											 /      \          /      \
											/        \        /        \
										   LR        RC      CL        LR



inorder traversal for 3 DISKS: 'L,R',   'L,C',    'R,C',    'L,R',   'C,L',    'C,R',    'L,R'


                                                      4 DISKS
                                                       
														 LR
														/  \
													   /    \
													  /      \
			                                         /        \
		                                            /          \
		                                           /            \
                                                  /              \
                                                 /                \
												LC                CR
											   /  \              /  \
											  /    \            /    \
											 /      \          /      \
											/        \        /        \
										   LR        RC      CL        LR
										  /  \      /  \    /  \      /  \
								         LC  CR    RL  LC  CR  RL    LC  CR

inorder traversal for 4 DISKS: 'L,C',   'L,R',    'C,R',    'L,C',    'R,L',    'R,C',    'L,C',    'L,R',    'C,R',   'C,L',   'R,L',   'C,R',   'L,C',   'L,R',   'C,R'

so for example the traversal of 4 disks lists the steps to solve the hanoi tower with 4 disks


we can generate the sequence with the following python function (which implements the inorder traversal)

def printSolution(left,right, n):
	if n == 0:
		return
		
	if {left,right} == {"L","R"}:
		printSolution(left, "C", n - 1)
		print(f"{left,right}", end = " ")
		printSolution("C", right, n - 1)
	
	if {left,right} == {"L","C"}:
		printSolution(left, "R", n - 1)
		print(f"{left,right}", end = " ")
		printSolution("R", right, n - 1)
	
	if {left,right} == {"R","C"}:
		printSolution(left, "L", n - 1)
		print(f"{left,right}", end = " ")
		printSolution("L", right, n - 1)

printSolution("L","R", 3) <---- this will print out the solution for 3 disks



we can optimize this function using sets

def printSolution(left,right, n):
	if n == 0:
		return
		
	middle = {"L","R","C"} - (left | right)
	printSolution(left, middle, n - 1)
	print(f"{left,right}", end = " ")
	printSolution(middle, right, n - 1)

print({"L"}, {"R"}, 3)   <---- we pass in sets this time, but doesn't print as nice as before (this can be fixed with  tweaks)

if we keep optimizing we arrive to the following recursive function




def S(U, F, T, n):
	if n == 1:
		return [list(F) + list(T)]
	return S(U, F, U - (F | T), n - 1) + [list(F) + list(T)] + S(U, U - (F | T), T, n - 1)


S({"L","C","R"}, {"L"},{"R"},3)  <----- generalized for any set


rewriting the above in mathematical form

HANOI's FUNCTION
S(U,F,T,1) = [list(F) + list(T)]
S(U,F,T,n) = S(U, F, U - (F | T), n - 1) + [list(F) + list(T)] + S(U, U - (F | T), T, n - 1)

"""





