# RL-exercise
A Q-Learning problem example


Consider a bidimensional space of 4 x 4 cells, with the following rewards for being in each cell:

0,   0,   0,  0 </br>
0,   0,   0,  0 </br>
0,   0, -.04, 0 </br>
0,   0,   1,-.1 </br>



There is a goal point, position [3,2], with high reward for being on it, and no reward or negative reward for leaving it. Our actions are king movements in a chess game, plus the No Operation movement. Adding the NOP movement allows us to remain in the best position when found, then exhaust the convergence steps until loop breaks, finishing the game. The NOP has as drawback that we could get stuck in a local sub-optimal, while forcing us to always move could let us escape from them.



Problem Details: 

Space has dimensions 4 x 4
Goal is to reach [3,2] (We don't tell which is the goal, but rather we reward it better)
Start point is at Random
Reward depends only on the current position


## Solution Proposal

We propose to use Q- Learning as the way to asses the problem
Points to take in consideration

- We don´t know where the goal cell is so we need to explore the solutions to try to find it

- We don`t know how many step we have to reach the solution ( we can only suppose there are enough)

- We supose the agent doesn't know the dimensions of the world and the distribution of the rewards

- We need to consider the Exploration / Exploitation balance: </br> The ε-greedy policy balances trying new moves (exploration) and following the best-known move (exploitation)

So we need to give our agent a feasible policy to follow to get it to maximize the reward  

To warranty a reward near to maximum ( can not warranty in general because the unknowns mentioned before) we propose the use of Q - Learning with the following formula

## Q-value Function in Q-learning

The **Q-value function** represents the expected cumulative reward for taking an action `a` in a given state `s`, following the best learned policy thereafter.

### **Formula:**
\[
Q(s, a) = Q(s, a) + α [ R(s) + γ \max <sub>_a' </sub> Q(s', a') - Q(s, a) ]
\]
Where:
- \( Q(s, a) \) → Current Q-value for state \( s \) and action \( a \).
- \( α \) → Learning rate (how much new information overrides old).
- \( R(s) \) → Reward received for reaching state \( s \).
- \( γ \) → Discount factor (how much future rewards matter).
- \( \max <sub>_a' </sub> Q(s', a') \) → Highest Q-value of the next state \( s' \).
- \( s' \) → New state reached after taking action \( a \).

### Actions available (King Movements + NOP):**

 0: (-1, -1) → Up-Left  </br>
 1: (-1,  0) → Up  </br>
 2: (-1,  1) → Up-Right  </br>
 3: ( 0, -1) → Left  </br>
 4: ( 0,  0) → No Operation (NOP)  </br>
 5: ( 0,  1) → Right  </br>
 6: ( 1, -1) → Down-Left  </br>
 7: ( 1,  0) → Down  </br>
 8: ( 1,  1) → Down-Right  </br>

## Description of the solution

1. **Initialize** \( Q(s, a) \) 
2. **Execute N Episodes **:
   - Choose action \( a \) using an **exploration strategy** (e.g., ε-greedy).
   - Take action \( a \), observe **reward** \( R(s) \) and new state \( s' \).
   - Update \( Q(s, a) \) using the formula.
3. **Derive the optimal policy** by selecting actions with the highest Q-values:
   \[
   \pi(s) = \arg\max_{a} Q(s, a)
   \]

### **Key Insights:**
- **Exploration vs. Exploitation**: The ε-greedy policy balances trying new moves (exploration) and following the best-known move (exploitation).
- **Convergence**: As episodes progress, Q-values stabilize, leading to an optimal policy.
- **Handling Local Optima**: Adjusting \( \alpha \), \( \gamma \), or using **random restarts** can help escape poor strategies.

