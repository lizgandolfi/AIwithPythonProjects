# Homework 5: Comparing Alpha-Beta Pruning and Monte Carlo Tree Search on ConnectFour

## Instructions

Compare alpha-beta pruning and Monte Carlo tree search on the ConnectFour game. Have one agent play using alpha-beta and the other agent using Monte Carlo tree search. Let each player take up to 15 seconds to compute its next move. Base your code on the `games4e.py`, specifically `alpha_beta_cutoff_search`, `monte_carlo_tree_search`, and `ConnectFour`. You will need to adapt the code to cut-off after 15 seconds as opposed to a depth. This is very similar to what you will need to do for the project. Play 30 games and summarize the results.

## Results

Based on the results from my code I noticed the following trends:

- **Which method wins more often?**
    - Monte Carlo Tree Search seems to be winning more often than Alpha-Beta Pruning.

- **Why do you think that is?**
    - That might be because Monte Carlo Tree Search is able to explore more possibilities in the given time frame, which allows it to make better decisions than alpha-beta pruning. 

## Utilized Resources

- `games4e.py`, specifically:
    - `alpha_beta_cutoff_search`
    - `monte_carlo_tree_search`
    - `ConnectFour`

- GitHub Copilot was used to fix bugs in the code and problem solve.

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
