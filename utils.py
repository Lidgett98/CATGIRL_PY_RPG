import random

class PlayerStats:
    def __init__(self):
        self.stats = {
            "strength": 1,
            "endurance": 1,
            "intelligence": 1,
            "luck": 1,
            "health": 10,
            "max_health": 10,
            "gold": 0,
            "level": 1,
            "experience": 0,
            "exp_to_next_level": 10
        }

    def level_up(self):
        self.stats["experience"] += 1
        if self.stats["experience"] >= self.stats["exp_to_next_level"]:
            self.stats["level"] += 1
            self.stats["experience"] = 0
            self.stats["exp_to_next_level"] += 5
            for stat in self.stats:
                if stat != "health" and stat != "max_health" and stat != "gold":
                    self.stats[stat] += random.randint(1, 3)

class Room:
    def __init__(self, name, description, actions, interact=None):
        self.name = name
        self.description = description
        self.actions = actions
        self.interact = interact

def handle_action(room, action):
    if action in room.actions:
        if action == "fight":
            print("You fight the enemy and win!")
            player_stats.stats["gold"] += room.interact
            player_stats.level_up()
            setattr(rooms_code, room.name + ".actions", ["explore"])
            setattr(rooms_code, room.name + ".description", f"{room.description}\n\nYou have defeated the enemy and earned {room.interact} gold!")
        elif action == "explore":
            print(f"{room.description}\n\nActions: {room.actions}")
        elif action == "interact":
            if room.interact:
                player_stats.stats["gold"] += room.interact
                setattr(rooms_code, room.name + ".interact", None)
                print(f"{room.description}\n\nYou found {room.interact} gold!")
            else:
                print("There's nothing to interact with here.")
    else:
        print("That's not an action you can take here.")

def create_scene_template(name, description, choices):
    def scene():
        print(description)
        for index, choice in enumerate(choices, start=1):
            print(f"{index}. {choice[0]}")
        choice = input("Enter choice: ")
        while not choice.isnumeric() or int(choice) not in range(1, len(choices) + 1):
            choice = input("Invalid choice. Enter a valid number: ")
        choice = int(choice)
        return choices[choice - 1][1]
    setattr(scene_code, name, scene)
