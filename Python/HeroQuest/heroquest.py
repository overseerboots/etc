import pandas as pd
import random

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

def hero_select():
    print("Select a Hero:")
    print("0) Exit")
    print("1) Barbarian")
    print("2) Dwarf")
    print("3) Elf")
    print("4) Wizard")
    print("==================================")
    hero = input("Select a Hero\n> ")
    while True:
        if hero == "0":
            print("Goodbye!")
            quit()
        else:
            try:
                hero = heroes[int(hero) - 1]
                return hero
            except:
                print("Invalid Hero")

def monster_select():
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
    monster = input("Select a Monster\n> ")
    while True:
        if monster == "0":
            print("Goodbye!")
            quit()
        else:
            try:
                monster = monsters[int(monster) - 1]
                return monster
            except:
                print("Invalid Monster")

def log_append(message):
    with open("log.md","a") as log:
        log.write(f"{message}\n")

def skull_roll(char_stats, character):
    hits = 0
    for x in range(0,int(char_stats.loc['Attack', character])):
        roll = random.randint(0,2)
        if roll == 0:
            hits += 1
    print(f"{character} rolled {str(hits)} skulls!")
    log_append(f"{character} rolled {str(hits)} skulls")
    return hits

def shield_roll(char_stats, character):
    hits = 0
    for x in range(0,int(char_stats.loc['Defend', character])):
        roll = random.randint(0,2)
        if roll == 0:
            hits += 1
    print(f"{character} rolled {str(hits)} useful shields!")
    log_append(f"{character} rolled {str(hits)} useful shields")
    return hits

# VARIABLES ========================
monsters = ["Goblin", "Skeleton", "Zombie", "Orc", "Abomination", "Mummy", "Dread Warrior", "Gargoyle"]
heroes = ["Barbarian", "Dwarf", "Elf", "Wizard"]

# MAIN =============================
# Some prep stuff before actually getting started
char_stats = pd.read_csv('HeroQuestStats.csv', index_col=0)
wins = 0
losses = 0

# Actually getting started

# Ask user for number of fights, hero and monster
hero = hero_select()
monster = monster_select()
num_of_fights = int(input("Number of fights to simulate:\n> "))
okay_check = input(f"{hero} will fight {monster} {str(num_of_fights)} times. Is this OK? [Y/n]\n> ")
log_append(f"# {hero} VS {monster} x{str(num_of_fights)}")

for fight_num in range(1, num_of_fights+1):
    log_append(f"## Fight {str(fight_num)}")
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
            losses += 1
            break

# Summary
print("= SUMMARY ========================")
print(f"{hero} won {wins} fights and lost {losses}!")
