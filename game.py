import tkinter as tk
from tkinter import messagebox

from stats import PlayerStats
from rooms import *
from utils import handle_action, create_scene_template, app


# Player starts with 0 gold and is in "room_1"
player = {
    "current_room": "room_1",
    "stats": PlayerStats(),
    "gold": 0,
    "inventory": []
}

# Create dictionary to keep track of visited rooms
visited_rooms = {}

# Create dictionary to keep track of unlocked doors
unlocked_doors = {}

# Create dictionary to keep track of which scenes have been generated
generated_scenes = {}

# Generate scene templates for each room
for room in Room.__subclasses__():
    if room.name not in generated_scenes:
        generated_scenes[room.name] = {}
    for scene_type in room.scenes:
        if scene_type not in generated_scenes[room.name]:
            generated_scenes[room.name][scene_type] = create_scene_template(scene_type)

# Run tkinter Gui
def start_game():
    # Reset player's stats and gold
    player["stats"] = PlayerStats()
    player["gold"] = 0
    
    # Reset dictionaries for visited rooms and unlocked doors
    visited_rooms.clear()
    unlocked_doors.clear()

    # Reset generated scenes dictionary
    for room in generated_scenes:
        for scene_type in generated_scenes[room]:
            generated_scenes[room][scene_type]["generated"] = False
    
    # Update player's race
    player["stats"].race = race_var.get()

    # Initialize current room
    current_room = getattr(rooms_code, player["current_room"])(visited_rooms, unlocked_doors, generated_scenes)

    # Display current room's description
    text_box.delete("1.0", "end")
    text_box.insert("end", current_room.description)
    
    # Enable action button
    action_button.config(state="normal")

def handle_player_input():
    # Get player's input and clear entry field
    player_input = entry_field.get()
    entry_field.delete(0, "end")

    # Handle player's action and update current room
    current_room, player_output = handle_action(player_input, current_room, player)
    
    # Display player output in text box
    text_box.insert("end", "\n\n" + player_output)

    # Check if game over
    if current_room.game_over:
        messagebox.showinfo("Game Over", current_room.game_over)
        start_game()
    else:
        # Update visited rooms and unlocked doors
        visited_rooms[current_room.name] = True
        for door in current_room.doors:
            if door.is_locked() and door.room_b.name in visited_rooms:
                unlocked_doors[door.name] = True

        # Disable action button if current room is a treasure room
        if current_room.is_treasure_room():
            action_button.config(state="disabled")
        else:
            action_button.config(state="normal")
        
        # Display current room's description
        text_box.insert("end", "\n\n" + current_room.description)


# Create tkinter GUI
root = tk.Tk()
root.title("Text-Based Adventure RPG")

# Add main text box to display game output
text_box = tk.Text(root, height=20, width=50)
text_box.pack(pady=10)

# Add input field for player's actions
entry_field = tk.Entry(root, width=50)
entry_field.pack()

# Add start scene button
start_scene_button = tk.Button(root, text="Start Game", command=start_game)
start_scene_button.pack(pady=10)

# Add
