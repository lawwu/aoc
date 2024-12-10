def split_game_string(game_string):
    # game_string = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

    # split game_id from the rest of the string
    game_string, cube_sets_one_str = game_string.split(":")

    # split cube sets
    cube_sets = cube_sets_one_str.split(";")
    # strip each one
    cubesets = [cube_set.strip() for cube_set in cube_sets]

    # get game id
    _, game_id = game_string.split(" ")
    game_int = int(game_id)

    # get cube set dictionary
    # [' 3 blue, 4 red', ' 1 red, 2 green, 6 blue', ' 2 green'])
    color_dict_list = []
    for s in cubesets:
        color_dict = {}
        num_color_string_list = s.split(",")
        for num_color in num_color_string_list:
            num_color = num_color.strip()
            num, color = num_color.split(" ")
            # add to dictionary
            color_dict[color] = int(num)
            color_dict_list.append(color_dict)

    return game_string, game_int, cube_sets, color_dict_list

def is_game_possible(color_dict, max_red=12, max_green=13, max_blue=14):
    # Check if any color exceeds its maximum
    red = color_dict.get('red', 0)
    green = color_dict.get('green', 0)
    blue = color_dict.get('blue', 0)
    
    return red <= max_red and green <= max_green and blue <= max_blue

# Part 2
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
# Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
# Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
# Game 4 required at least 14 red, 3 green, and 15 blue cubes.
# Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.

def find_minimum_cubes(color_dict_list):
    # Initialize maximums for each color
    max_red = 0
    max_green = 0
    max_blue = 0
    
    # Find the maximum number needed for each color across all sets
    for color_dict in color_dict_list:
        max_red = max(max_red, color_dict.get('red', 0))
        max_green = max(max_green, color_dict.get('green', 0))
        max_blue = max(max_blue, color_dict.get('blue', 0))
    
    # Return the power (product of the minimums needed)
    return max_red * max_green * max_blue


def main():
    # game_string = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    # #game_string, game_int, cube_sets, color_dict_list = split_game_string(game_string)
    # # print(game_string, game_int, cube_sets, color_dict_list)

    # game_int,color_dict_list = split_game_string(game_string)

    total = 0
    total_power = 0
    with open('input.txt', 'r') as file:
        for line in file:
            _, game_id, _, color_dict_list = split_game_string(line.strip())
            # print(color_dict_list)

            power = find_minimum_cubes(color_dict_list)
            total_power += power

            
            # Check if all sets in this game are possible
            game_possible = True
            for color_dict in color_dict_list:
                if not is_game_possible(color_dict):
                    game_possible = False
                    break
            
            # If game is possible, add its ID to total
            if game_possible:
                total += game_id
    
    print(f"Sum of possible game IDs: {total}")
    print(f"Part two: total power is {total_power}")


if __name__ == "__main__":
    main()