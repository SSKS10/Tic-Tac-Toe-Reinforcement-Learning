# Tic-Tac-Toe-Reinforcement-Learning
Q Learning

1.Initialize all state with 0

  I have created 3^9 state (not all legal) for variables (" ","X","O") and initialize every state with all 9 actions with 0

  I started my indexing with 1 so for 0 you can give any value since that value will not matter much

2.Training Phase

  a)For Agent:-
    v(s,a) = (1-alpha) * v(s,a) + alpha * (reward + gamma * max v(s',a'))
    
  b)For Player(Skilled):-
    v(s,a) = (1-alpha) * v(s,a) + alpha * (-1 * reward + gamma * max v(s',a'))

    where,
    v(s,a) is current state value
    v(s',a') is state value after action a
    alpha is learning rate (I have taken it 0.5)
    reward (for winning 1; for lossing -1; for draw 0.5; else 0.0)
    gamma is adjustment factor
    
  for more details go to this link below:
  
     https://towardsdatascience.com/lessons-learned-from-tic-tac-toe-practical-reinforcement-learning-tips-5cac654a45a8 
     
3.Playing with real environment
 Since while training some of states will not occur so that can be done by playing with real player
 
4.Table Value
This is used to track all value of every state
