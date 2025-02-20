import random

def gamble(stake, goal, num_trials):
    wins = 0
    total_bets = 0
    
    for _ in range(num_trials):
        current_stake = stake
        bets = 0
        
        while 0 < current_stake < goal:
            bets += 1
            if random.random() < 0.5:  # 50% chance to win
                current_stake += 1
            else:
                current_stake -= 1
        
        if current_stake == goal:
            wins += 1
        
        total_bets += bets
    
    win_percentage = (wins / num_trials) * 100
    loss_percentage = 100 - win_percentage
    
    print(f"Number of Wins: {wins}")
    print(f"Win Percentage: {win_percentage:.2f}%")
    print(f"Loss Percentage: {loss_percentage:.2f}%")
    print(f"Average Bets per Game: {total_bets / num_trials:.2f}")

# Get user input
stake = int(input("Enter initial stake: "))
goal = int(input("Enter goal amount: "))
num_trials = int(input("Enter number of trials: "))

gamble(stake, goal, num_trials)
