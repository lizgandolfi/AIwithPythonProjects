# LisaGandolfi_COSC5600HW4
This .zip file contains the code for the M&C problem.
    
Three M and three C are on one side of a river, along with a boat that can hold one or two people. Find a way to get everyone to the other side without ever leaving a group of M in one place outnumbered by the C in that place.

The problem can be solved using breadth-first search. The state space is represented by the number of M and C on the left side of the river, the number of M and C on the right side of the river, and the position of the boat. The initial state is (3,3,'left',0,0), and the goal state is (0,0,'right',3,3). The successors of a state are the states that can be reached by moving one or two people from one side of the river to the other. The search terminates when everyone is on the right side of the river. 

The solution is:
(3,3,right,0,0)

CLeft = number of C on the left side of the river
MLeft = number of M on the left side of the river
boat = the position of the boat
CRight = number of C on the right side of the river
MRight = number of M on the right side of the river

## Prerequisites

Before running the code, ensure you have the following installed:

- Python 3.x
- Required Python packages (listed in `requirements.txt`)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/aimacode/aima-python.git
    ```

2. Install the required packages: (also included in the .zip file)

    ```sh
    pip install -r requirements.txt
    ```