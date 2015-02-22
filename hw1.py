# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random
def name_to_number(name):
    if(name == "rock"):
        number = 0
    elif(name == "Spock"):
        number = 1
    elif(name == "paper"):
        number = 2
    elif(name == "lizard"):
        number = 3
    elif(name == "scissors"):
        number = 4
    else:
        return name + " does not match any of the five correct input strings."

    return number


def number_to_name(number):
    if(number == 0):
        name = "rock"
    elif(number == 1):
        name = "Spock"
    elif(number == 2):
        name = "paper"
    elif(number == 3):
        name = "lizard"
    elif(number == 4):
        name = "scissors"
    else:
        return str(number) + " does not match any of the five correct input numbers."

    return name
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below    
    print

    print "Player chooses " + player_choice
    
    player_number = name_to_number(player_choice)

    comp_number = random.randrange(0, 5, 1)

    comp_choice = number_to_name(comp_number)
    
    print "Computer chooses " + comp_choice
    
    difference = (player_number - comp_number) % 5
    
    if(difference >= 3):
        print 'Computer wins!'
    elif(difference == 0):
        print "Player and computer tie!"
    else:
        print "Player wins!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
