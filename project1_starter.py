"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Amya Ratcliff Prince]
Date: [October 20, 2025]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

from os import write


def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation

     #starting amount of gold for a new character
    character_gold = 0 
    #starting level for all new characters 
    character_level = 1
    #Use calculate_stats() to get strength, magic, and health based on class and level
    # stores all character information inside a dictionary 
    #makes it easy to save, load , or update later
    character_strength, character_magic, character_health = calculate_stats(character_class,character_level)
    character_dictionary = {"name": name,
                       "class": character_class,
                       "level": character_level,
                       "strength": character_strength,
                       "magic": character_magic,
                       "health": character_health,
                       "gold": character_gold}
    return character_dictionary# returns completed character dictionary into the main program


    pass

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    #starting point for each player 
    base_stat = 5 
    #Each stat will be multiplyed by the level 
    #points * level will then be used for calculations in condotional statements 
    strength_point = 5 * level #fix calculations
    magic_point = 10 * level 
    health_point = 8 * level 
    # if character class is "Warriors", run this block
    if character_class == "Warriors":  
        strength = strength_point * 3 + base_stat 
        magic = magic_point // 2 + base_stat   
        health = health_point * 2 + base_stat
    #if character class is "Mange", run this block
    elif character_class == "Mages":   
        strength = strength_point // 2 + base_stat
        magic = magic_point * 3 + base_stat
        health = health_point + base_stat 
    #if character class is "Rogues", run this block 
    elif character_class == "Rogues":
        strength = strength_point * 2 + base_stat
        magic = magic_point * 2 + base_stat
        health = health_point // 2 + base_stat
         #if the class is none of the ones above, run this block for "Clerics"
    else:#Clerics                    
        strength = strength_point * 2 + base_stat
        magic = magic_point * 3 + base_stat
        health = health_point * 2 + base_stat
     #stores all stats toghter in a tuple 
    return (strength, magic, health)
    pass
#takes in your character and a filename
def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    #opens the given file name in write mode 
    with open(filename, "w") as file_object:
        #writes each piecce of character information on it own line
        #the f-string inserts the value from the character dictionary
        file_object.write(f"Character Name: {character['name']}\n")#ask teacher about importing write
        file_object.write(f"Class: {character['class']}\n")
        file_object.write(f"Level: {character['level']}\n")
        file_object.write(f"Strength: {character['strength']}\n")
        file_object.write(f"Magic: {character['magic']}\n")
        file_object.write(f"Health: {character['health']}\n")
        file_object.write(f"Gold: {character['gold']}\n")
    return True 


    pass
import os #used to check if file exists 
def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    #can we use try and exeception
    #checks if file exist before trying to open it 

    if not os.path.exists(filename):
         print("File not found")
         return None
        #opens file in read mode 
    with open(filename, "r") as file_object:
            character_lines = file_object.readlines()#reads lines into a list
            print(character_lines)

    character_data = {} #an empty dictionary to store character data 
    #loops through each line in the file 
    for line in character_lines:
        line = line.strip() #remove newline and extra spaces 
        key, value = line.split(":") #splits the line into key and value with (:)
        #removes any spaces arounbd the key and value 
        key = key.strip() 
        value = value.strip()
        #adds the key/value pair to the dictionary 
        character_data[key] = value
    return character_data


    pass

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    #Print each key and value from the character dictionary in a readable format
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class:{character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")

    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    #increases character level by 1
    character['level'] +=1
    #boost stats when leveling up 
    character['strength'] += 2
    character['magic'] += 3
    character['health'] += 5 
     #add gold as a reward for leveling up 
    character['gold'] = 10 + character['gold']# gold is increases with each level
    
    #print statements to show player there progress 
    print(f"You leveled up! Your current level is {character['level']}\n")
    print(f"Yay! your strength has levled up {character['strength']}\n")
    print(f"Yay! your magic has levled up {character['magic']}\n")
    print(f"Yay! your health has levled up {character['health']}\n")
    print(f"You earned {character['gold']} gold!")
    #Function modifies the dictionary directly, so no return value is needed
    return None 
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    char = create_character("TestHero", "Warrior")
    display_character(char)
    save_character(char, "my_character.txt")
    level_up(char)
    display_character(char)
    loaded_character = load_character("my_character.txt")
    if loaded_character is not None:
        print("Character loaded successfully!")
        print(loaded_character)
    else:
        print("Failed to load character.")
    #print(char)
