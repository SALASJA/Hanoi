from turtle import *
from TowerOfHanoi import TowerOfHanoi
from hanois_formula import S
import sys
import time

class TowerView:
	def __init__(self):
		setup(1280, 500)
		tracer(0,0)
		hideturtle()
		bgcolor("black")
		self.colors = ["red", "orange", "yellow","green", "cyan","blue", "purple"]
		self.tower_positions = {"L": -400, "C":0, "R":400}
		self.MAX_WIDTH = 50
		self.MAX_HEIGHT = 30
		self.STARTING_HEIGHT = -100
		self.WIDTH_DELTA = 50
		
		
	
	def render(self, tower_data):
		reset()
		hideturtle()
		for key in tower_data:
			x_pos = self.tower_positions[key]
			disks = tower_data[key]
			for disk_position in range(len(disks)):
				y_pos = self.MAX_HEIGHT * disk_position + self.STARTING_HEIGHT
				disk_width =  self.MAX_WIDTH + self.WIDTH_DELTA * disks[disk_position]
				disk_height = self.MAX_HEIGHT
				current_disk = disks[disk_position]
				disk_color = self.colors[current_disk - 1]
				self.rectangle(x_pos,y_pos, disk_width, disk_height, disk_color)
		update()
		

	def rectangle(self,x,y, width,height, color_string):
		penup()
		goto(x  - width/2,y)
		pendown()
		color(color_string)
		begin_fill()
		forward(width)
		left(90)
		forward(height)
		left(90)
		forward(width)
		left(90)
		forward(height)
		left(90)
		end_fill()


def main():
	height = int(sys.argv[1]) if len(sys.argv) == 2 and sys.argv[1].isnumeric() else 3
	view = TowerView()
	puzzle = TowerOfHanoi(height)
	solution = S({"L","C","R"}, {"L"}, {"R"}, height)
	view.render(puzzle.state)
	time.sleep(1)
	for operation in solution:
		puzzle.execute(operation)
		view.render(puzzle.state)
		time.sleep(0.50)
	time.sleep(2)

main()


"""
def main():
	tracer(0,0)
	disks = [5,8,1,2,9,7]
	i = 0
	while i < len(disks):
		rectangle(-250, 30 * i - 100, 200 - 20 * disks[i])
		rectangle(0, 30 * i - 100, 200 - 20 * disks[i])
		rectangle(250, 30 * i - 100, 200 - 20 * disks[i])
		i = i + 1
	update()
	done()

def rectangle(x,y, width,height = 30):
	penup()
	goto(x  - width/2,y)
	pendown()
	forward(width)
	left(90)
	forward(height)
	left(90)
	forward(width)
	left(90)
	forward(height)
	left(90)


main()
"""