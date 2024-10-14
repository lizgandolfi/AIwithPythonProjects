### Missionaries and Cannibals Problem ###

#CLeft = number of Cannibals on the left side of the river
#MLeft = number of Missionaries on the left side of the river
#boat = the position of the boat
#CRight = number of Cannibals on the right side of the river
#MRight = number of Missionaries on the right side of the river

import math
import random

class State():
	def __init__(self, CLeft, MLeft, boat, CRight, MRight):
		self.CLeft = CLeft
		self.MLeft = MLeft
		self.boat = boat
		self.CRight = CRight
		self.MRight = MRight
		self.parent = None

	def is_goal(self):
		if self.CLeft == 0 and self.MLeft == 0:
			return True
		else:
			return False

	def is_valid(self):
		if self.MLeft >= 0 and self.MRight >= 0 \
                   and self.CLeft >= 0 and self.CRight >= 0 \
                   and (self.MLeft == 0 or self.MLeft >= self.CLeft) \
                   and (self.MRight == 0 or self.MRight >= self.CRight):
			return True
		else:
			return False

	def __eq__(self, other):
		return self.CLeft == other.CLeft and self.MLeft == other.MLeft \
                   and self.boat == other.boat and self.CRight == other.CRight \
                   and self.MRight == other.MRight

	def __hash__(self):
		return hash((self.CLeft, self.MLeft, self.boat, self.CRight, self.MRight))

def successors(cur_state):
    children = []
    
    #Possible movements: (Missionaries, Cannibals)
    movements = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
    
    if cur_state.boat == 'left':
        new_boat_position = 'right'
        for M_move, C_move in movements:
            new_state = State(cur_state.CLeft - C_move, cur_state.MLeft - M_move, new_boat_position,
                              cur_state.CRight + C_move, cur_state.MRight + M_move)
            if new_state.is_valid():
                new_state.parent = cur_state
                children.append(new_state)
    else:
        new_boat_position = 'left'
        for M_move, C_move in movements:
            new_state = State(cur_state.CLeft + C_move, cur_state.MLeft + M_move, new_boat_position,
                              cur_state.CRight - C_move, cur_state.MRight - M_move)
            if new_state.is_valid():
                new_state.parent = cur_state
                children.append(new_state)
    
    return children

def breadth_first_search():
	initial_state = State(3,3,'left',0,0)
	if initial_state.is_goal():
		return initial_state
	frontier = list()
	explored = set()
	frontier.append(initial_state)
	while frontier:
		state = frontier.pop(0)
		if state.is_goal():
			return state
		explored.add(state)
		children = successors(state)
		for child in children:
			if (child not in explored) or (child not in frontier):
				frontier.append(child)
	return None

def print_solution(solution):
		path = []
		path.append(solution)
		parent = solution.parent
		while parent:
			path.append(parent)
			parent = parent.parent

		for t in range(len(path)):
			state = path[len(path) - t - 1]
			print("(" + str(state.CLeft) + "," + str(state.MLeft) \
							  + "," + state.boat + "," + str(state.CRight) + "," + \
							  str(state.MRight) + ")")

def main():
	solution = breadth_first_search()
	print("The Solution for Missionaries and Cannibals is:")
	print ("in order of (Cannibals on the left, Missionaries on the left, Boat position, Cannibals on the right, Missionaries on the right):")
	print_solution(solution)

if __name__ == "__main__":
    main()


