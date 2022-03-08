from TowerOfHanoi import *
import sys
def main():
	height = int(sys.argv[0]) if len(sys.argv) == 1 and sys.argv[0].isnumeric() else 3
	puzzle = TowerOfHanoi(height)
	print(puzzle)
	while not puzzle.solved():
		operation = input("Enter your next operation: ")
		puzzle.execute(operation)
		print(puzzle)
	print("COMPLETE!")


main()#hmmmm
