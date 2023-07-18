import random
from itertools import permutations
import matplotlib.pyplot as plt

# Generate Random Number
def generate_random_number():
    return str(random.randint(0, 999)).zfill(3)


#Counters
straight_wins = 0
rambolito_wins = 0
straight_total_bet_cost = 0
rambolito_total_bet_cost = 0
straight_total_winnings = 0
rambolito_total_winnings = 0
# Initialize Parameters
bet_cost = 12
result_winnings = 4500
iterations = 1000

straight_plot = []
rambolito_plot = []
straight_roi_plot = []
rambolito_roi_plot = []

for i in range(iterations):
    # Generate the winning number
    winning_number = generate_random_number()
    #winning_number = "100"
    # Generate random numbers for straight and rambolito
    straight = generate_random_number()
    rambolito = generate_random_number()
    #straight = "321"
    #rambolito = "456"
    print("Straight 3-digit number:", straight)
    print("Rambolito 3-digit number:", rambolito)

    # Calculate bet cost for each bet type
    straight_bet_cost = bet_cost
    straight_total_bet_cost += straight_bet_cost

    rambolito_combinations = set(permutations((rambolito), 3))
    rambolito_bet_cost = len(rambolito_combinations) * bet_cost
    rambolito_total_bet_cost += rambolito_bet_cost


    print("Rambolito combinations:", ", ".join(["".join(combination) for combination in rambolito_combinations]))
    print("Straight bet cost:", straight_bet_cost)
    print("Rambolito bet cost:", rambolito_bet_cost)
    

    def winner(numbers, win_number):
        straight_number = numbers[0]
        rambolito_number = numbers[1]
        rambolito_permutations = set(permutations(rambolito_number, 3))
        rambolito_numbers = [int("".join(combination)) for combination in rambolito_permutations]

        if win_number == straight_number and int(straight_number) in rambolito_numbers:
            print("Straight and Rambolito winner:", win_number)
            return 'both'
        elif win_number == straight_number:
            print("Straight winner:", win_number)
            return 'straight'
        else:
            if int(win_number) in rambolito_numbers:
                print("Rambolito winner:", win_number)
                return 'rambolito'
            else:
                print("No winner, Result:", win_number, rambolito_numbers)
                return 'no_winner'




    result = winner([straight, rambolito], winning_number)

    # Update the counters 
    if result == 'both':
        straight_wins += 1
        rambolito_wins += 1
        straight_winnings = result_winnings - straight_bet_cost
        straight_total_winnings += straight_winnings
        if len(rambolito_combinations) == 3:
            rambolito_winnings = (result_winnings / 3) - rambolito_bet_cost
        else:
            rambolito_winnings = (result_winnings / 6) - rambolito_bet_cost
        rambolito_total_winnings += rambolito_winnings
    elif result == 'straight':
        straight_wins += 1
        straight_winnings = result_winnings - straight_bet_cost
        straight_total_winnings += straight_winnings
        
    elif result == 'rambolito':
        rambolito_wins += 1
        if len(rambolito_combinations) == 3:
            rambolito_winnings = (result_winnings / 3) - rambolito_bet_cost
        else:
            rambolito_winnings = (result_winnings / 6) - rambolito_bet_cost
        rambolito_total_winnings += rambolito_winnings
        
    straight_prob = straight_wins / (i + 1) * 100
    rambolito_prob = rambolito_wins / (i + 1) * 100

    straight_plot.append(straight_prob)
    rambolito_plot.append(rambolito_prob)

    straight_roi = (straight_total_winnings - straight_total_bet_cost) / straight_total_bet_cost * 100
    straight_roi_plot.append(straight_roi)

    rambolito_roi = (rambolito_total_winnings - rambolito_total_bet_cost) / rambolito_total_bet_cost * 100
    rambolito_roi_plot.append(rambolito_roi)

    print()


print("Straight wins:", straight_wins)
print("Rambolito wins:", rambolito_wins)


print("Straight total bet cost:", straight_total_bet_cost)
print("Rambolito total bet cost:", rambolito_total_bet_cost)


print("Straight total winnings:", straight_total_winnings - straight_total_bet_cost)
print("Straight Return of Investment: ", straight_roi, "%")
print("Rambolito total winnings:", rambolito_total_winnings - rambolito_total_bet_cost)
print("Rambolito Return of Investment: ", rambolito_roi, "%")


straight_probability = straight_wins / iterations * 100
rambolito_probability = rambolito_wins / iterations * 100

if rambolito_probability != 0:
    probability_ratio = straight_probability / rambolito_probability
else:
    probability_ratio = 0

print("Straight probability:", straight_probability, "%")
print("Rambolito probability:", rambolito_probability, "%")
print("Probability ratio (Straight / Rambolito):", probability_ratio)

iterations_list = list(range(1, iterations + 1))

# Plotting the probabilities
plt.plot(iterations_list, straight_plot, label='Straight Bet')
plt.plot(iterations_list, rambolito_plot, label='Rambolito Bet')

plt.xlabel('Iterations')
plt.ylabel('Probability (%)')
plt.title('Probability of Straight Bet vs. Rambolito Bet')
plt.legend()
plt.show()

# Plotting the ROI
plt.plot(iterations_list, straight_roi_plot, label='Straight Bet ROI')
plt.plot(iterations_list, rambolito_roi_plot, label='Rambolito Bet ROI')

plt.xlabel('Iterations')
plt.ylabel('ROI (%)')
plt.title('ROI of Straight Bet vs. Rambolito Bet')
plt.legend()
plt.show()

