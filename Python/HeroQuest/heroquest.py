import pandas as pd
import random
import matplotlib.pyplot as plt

# = Heroes =========================
# Barbarian = 1
# Dwarf = 2
# Elf = 3
# Wizard = 4

# = Monsters =======================
# Goblin = 1
# Skeleton = 2
# Zombie = 3
# Orc = 4
# Abomination = 5
# Mummy = 6
# Dread Warrior = 7
# Gargoyle = 8

# = Graphs =========================
# Pie Chart = 1
# Bar Chart = 2

def hero_select():
    '''
    Asks the user to enter a hero and type checks it, also prompts to exit the program.
    '''
    # Define the heroes to choose from
    heroes = ["Barbarian", "Dwarf", "Elf", "Wizard"]
    
    print("Select a Hero:")
    print("0) Exit")
    print("1) Barbarian")
    print("2) Dwarf")
    print("3) Elf")
    print("4) Wizard")
    print("==================================")
    while True:
        hero = 0
        hero = input("Select a Hero\n> ")
        if hero == "0":
            print("Goodbye!")
            quit()
        else:
            try:
                hero = heroes[int(hero) - 1]
                return hero
            except (IndexError, TypeError):
                print("!! INVALID HERO !!")

def monster_select():
    '''
    Asks the user to enter a monster and type checks it, also prompts to exit the program.
    '''
    monsters = ["Goblin", "Skeleton", "Zombie", "Orc", "Abomination", "Mummy", "Dread Warrior", "Gargoyle"]
    print("Select a Monster:")
    print("0) Exit")
    print("1) Goblin")
    print("2) Skeleton")
    print("3) Zombie")
    print("4) Orc")
    print("5) Abomination")
    print("6) Mummy")
    print("7) Dread Warrior")
    print("8) Gargoyle")
    print("==================================")
    while True:
        monster = 0
        monster = input("Select a Monster\n> ")
        if monster == "0":
            print("Goodbye!")
            quit()
        else:
            try:
                monster = monsters[int(monster) - 1]
                return monster
            except (IndexError, TypeError):
                print("!! INVALID MONSTER !!")

def num_of_fights_entry():
    '''
    Asks the user to enter a number of fights and type checks it
    '''
    while True:
        num_of_fights = int(input("Number of fights to simulate:\n> "))
        if num_of_fights > 0:
            return num_of_fights
        elif num_of_fights == 0:
            print("No fights occur and everyone lives happily ever after?")
        else:
            print("!! INVALID NUM OF FIGHTS !!")

def graph_type_entry():
    '''
    Asks the user to enter a graph type and type checks the input, also prompts to exit
    '''
    graph_types = ["Pie Chart", "Bar Chart"]
    print("Select a graph type")
    print("0) Exit")
    print("1) Pie Chart")
    print("2) Bar Chart")
    # More coming soon? Probably not
    while True:
        graph_type = input("Select a graph\n> ")
        if graph_type == "0":
            print("Goodbye!")
            quit()
        else:
            try:
                graph_type = graph_types[int(graph_type) - 1]
                return graph_type
            except (IndexError, TypeError):
                print("!! INVALID GRAPH TYPE !!")

def log_append(message) -> str:
    '''
    Append argument given to log.txt
    '''
    with open("log.txt","a") as log:
        log.write(f"{message}\n")

def skull_roll(char_stats, character):
    '''
    Roll for skulls with a 1/3 chance of getting one
    Rolls the number of times that the characters attack stat is
    '''
    hits = 0
    for x in range(0,int(char_stats.loc['Attack', character])):
        roll = random.randint(0,2)
        if roll == 0:
            hits += 1
    print(f"{character} rolled {str(hits)} skulls!")
    log_append(f"{character} rolled {str(hits)} skulls")
    return hits

def shield_roll(char_stats, character):
    '''
    Roll for skulls with a 1/3 chance of getting one
    Rolls the number of times that the characters defend stat is
    '''
    hits = 0
    for x in range(0,int(char_stats.loc['Defend', character])):
        roll = random.randint(0,2)
        if roll == 0:
            hits += 1
    print(f"{character} rolled {str(hits)} useful shields!")
    log_append(f"{character} rolled {str(hits)} useful shields")
    return hits


# MAIN =============================
# Some prep stuff before actually getting started
char_stats = pd.read_csv('HeroQuestStats.csv', index_col=0)
wins = 0
losses = 0
hero_win_turns = []
monster_win_turns = []

# Actually getting started
# Ask user for number of fights, hero and monster
while True:
    hero = hero_select()
    monster = monster_select()
    num_of_fights = num_of_fights_entry()
    okay_check = input(f"{hero} will fight {monster} {str(num_of_fights)} times. Is this OK? [Y/n]\n> ")
    if okay_check.lower() != "n":
        break

log_append(f"= {hero} VS {monster} x{num_of_fights} =============================")

for fight_num in range(1, num_of_fights+1):
    log_append(f"# Fight {str(fight_num)} #################")
    # Set hero stats for the next fight
    hero_body = char_stats.loc['Body', hero]
    hero_attack = char_stats.loc['Attack', hero]
    hero_defense = char_stats.loc['Defend', hero]
    
    # Same for the monster
    monster_body = char_stats.loc['Body', monster]
    monster_attack = char_stats.loc['Attack', monster]
    monster_defense = char_stats.loc['Defend', monster]

    # And non-character-specific variables
    turns = 0

    # Fight to the death...
    while True:
        turns += 1
        # Hero rolls for attack
        hero_skulls = skull_roll(char_stats, hero)
        
        # Monster rolls for defense
        monster_shields = shield_roll(char_stats, monster)
        
        # Monster takes damage if it should
        if (hero_skulls - monster_shields) > 0:
            monster_body -= (hero_skulls - monster_shields)
            print(f"{monster} took {(hero_skulls - monster_shields)} damage and now has {monster_body}HP")
            log_append(f"{monster} took {(hero_skulls - monster_shields)} damage and now has {monster_body}HP")
    
        # Check if the monster is dead, if so then end the fight
        if monster_body <= 0:
            print(f"{hero} killed {monster} in {str(turns)} turns")
            log_append(f"{hero} killed {monster} in {str(turns)} turns")
            hero_win_turns.append(turns)
            wins += 1
            break
        
        # Monster attacks back if it's not already dead
        # Monster rolls for attack
        monster_skulls = skull_roll(char_stats, monster)
        
        # Hero rolls for defense
        hero_shields = shield_roll(char_stats, hero)

        # Monster takes damage if it should
        if (monster_skulls - hero_shields) > 0:
            hero_body -= (monster_skulls - hero_shields)
            print(f"{hero} took {(monster_skulls - hero_shields)} damage and now has {hero_body}HP")
            log_append(f"{hero} took {(monster_skulls - hero_shields)} damage and now has {hero_body}HP")

        # Check if the hero is dead, if so then end the fight
        if hero_body <= 0:
            print(f"{monster} killed {hero} in {str(turns)} turns")
            log_append(f"{monster} killed {hero} in {str(turns)} turns")
            monster_win_turns.append(turns)
            losses += 1
            break

# Summary
if len(hero_win_turns) > 0: # If the hero won at all
    win_percentage = 100 * (wins / num_of_fights)
    hero_avg_turns = sum(hero_win_turns) / len(hero_win_turns)
else:
    win_percentage = 0
    hero_avg_turns = 0
if len(monster_win_turns) > 0: # If the monster won at all
    monster_win_turns = sum(monster_win_turns) / len(monster_win_turns)
else:
    monster_win_turns = 0

print("= SUMMARY ========================")
# Print to output
print(f"{hero} won {win_percentage}% of fights with {wins} wins and {losses} losses!")
print(f"{hero} won in an average of {hero_avg_turns} turns")
print(f"{monster} won in an average of {monster_win_turns} turns")
print("Log can be found in log.txt")
print("==================================")

# Append to log
log_append("= RESULTS ===========================")
log_append(f"{hero} won {win_percentage}% of fights with {wins} wins and {losses} losses!")

# Graphs
another_graph_check = "y"
graph_check = input("Generate a graph with these results? [y/N]\n> ")
while graph_check.lower() == "y" and another_graph_check.lower() == "y":
    graph_type = graph_type_entry()
    if graph_type == "Pie Chart":
        # Generate a pie chart
        plt.pie([wins, losses], labels=[hero, monster], autopct='%1.1f%%')

        # Add title
        plt.title(f"{hero} VS {monster} x{num_of_fights}")
        
        # Display the chart
        plt.show()
    
    elif graph_type == "Bar Chart":
        # Generate a bar chart
        plt.bar([hero, monster], [wins, losses])

        # Add title and labels
        plt.xlabel("Character")
        plt.ylabel("Wins")
        plt.title(f"{hero} VS {monster} x{num_of_fights}")

        # Display the plot
        plt.show()
    another_graph_check = input("Generate another graph? [y/N]\n> ")
