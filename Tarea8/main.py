import os
GAME_FIELDS = ["title", "genre", "platform", "year"]

def add_game(games):
    game = ask_game_data()
    games.append(game)

def ask_game_data():
    game = []
    for field in GAME_FIELDS:
        while True:
            data = input(f"Enter {field}'s game.")
            if field == "year":
                if data.isdigit():
                    game.append(data)
                    break
            elif data.strip():
                game.append(data)
                break

    return game

def prepare_data(games):
    games_data = ""
    for game in games:
        games_data += ",".join(game)
        if not game[len(game) - 1].__contains__("\n"):
            games_data += "\n"

    return games_data

def load_games(games, game_file):
    game_list = game_file.readlines()
    for game in game_list:
        games.append(list(game.split(",")))

    return games

def show_games(games):
    if games:
        counter = 1
        for game in games:
            print(f"{counter})")
            show_game(game)
            counter += 1
    else:
        print("There are no videogames to show.")

def show_game(game):
    for field in range(len(game)):
        print(f"{GAME_FIELDS[field]}: {game[field]}")

def update_game(games):
    if not games:
        print("Empty collection.")
        return
    
    show_games(games)
    print("¿Which game do you want to update?")

    game_number = select_option(games) - 1
    updated_game = ask_game_data()
    games[game_number] = updated_game

def delete_game(games):
    if not games:
        print("Empty collection.")
        return
    
    show_games(games)
    print("¿Which game do you want to delete?")

    game_number = select_option(games) - 1
    games.pop(game_number)

def search_game(games):
    if not games:
        print("Empty collection.")
        return
    
    show_fields()
    print("Select a field to search by.")
    field_number = select_option(GAME_FIELDS) - 1

    user_search = input(f"Enter the game's {GAME_FIELDS[field_number]} you want to search. ")
    coincidences = []
    for game in games:
        if game[field_number] == user_search:
            coincidences.append(game)
    
    if coincidences:
        print(f"Found {len(coincidences)} coincidences:")
        show_games(coincidences)
    else:
        print("There are 0 coincidences.")

def show_fields():
    counter = 1
    for field in GAME_FIELDS:
        print(f"{counter}) {field}")
        counter += 1

def select_option(option_list):
    while True:
        try:
            option = int(input("Select an option. "))
        except:
            print("You must select a number")
            continue
        
        if option <= len(option_list) and option > 0:
            return option
        print(f"You must select a number between 1 and {len(option_list)}.")

def menu():
    games = []
    if os.path.exists("games_file.txt"):
        with open("games_file.txt", "r+") as games_file:
            games = load_games(games, games_file)

    while True:
        print("1) Add videogame.\n2) Show videogames.\n3) Update videogame.\n4) Delete videogame.\n5) Search videogame.\n6) Exit.\n")
        option = input("Enter an option.")

        if option == "1":
            add_game(games)
        elif option == "2":
            show_games(games)
        elif option == "3":
            update_game(games)
        elif option == "4":
            delete_game(games)
        elif option == "5":
            search_game(games)
        elif option == "6":
            break
        else:
            print("You must select a number between 1 and 6.")
    
    with open("games_file.txt", "w") as games_file:
        games_file.write(prepare_data(games))

menu()