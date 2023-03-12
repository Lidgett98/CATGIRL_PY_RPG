 def fight(self, enemy_stats):
        # Start fight
        while True:
            # Player turn
            player_attack = player_stats.attack()
            enemy_stats.stats["hp"] -= player_attack
            self.text_box.config(state=tk.NORMAL)
            self.text_box.insert(
                tk.END,
                f"You dealt {player_attack} damage to the {enemy_stats.name}!\n",
            )
            self.text_box.config(state=tk.DISABLED)
            if enemy_stats.stats["hp"] <= 0:
                # Enemy defeated
                self.text_box.config(state=tk.NORMAL)
                self.text_box.insert(
                    tk.END,
                    f"You have defeated the {enemy_stats.name}!\n",
                )
                self.text_box.config(state=tk.DISABLED)
                break

            # Enemy turn
            enemy_attack = enemy_stats.attack()
            player_stats.stats["hp"] -= enemy_attack
            self.text_box.config(state=tk.NORMAL)
            self.text_box.insert(
                tk.END,
                f"The {enemy_stats.name} dealt {enemy_attack} damage to you!\import tkinter as tk
from tkinter import messagebox
from utils import PlayerStats, Room, handle_action, create_scene_template, app
import rooms_code
import scene_code

# Player stats
race_var = ""
player = {
    "name": "",
    "current_room": "room_a",
    "inventory": [],
    "stats": {
        "hp": 10,
        "mp": 5,
        "strength": 3,
        "defense": 3,
        "intelligence": 3,
        "wisdom": 3,
        "dexterity": 3,
        "charisma": 3,
    },
}

player_stats = PlayerStats(player["stats"])


# GUI
class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("PyGirl")

        # Create the main text box
        self.text_box = tk.Text(
            self.window,
            height=20,
            width=70,
            wrap=tk.WORD,
            background="#E6E6FA",
            borderwidth=2,
            relief=tk.SUNKEN,
            font=("Helvetica", 11),
        )
        self.text_box.pack(padx=10, pady=10)

        # Create the user input box
        self.user_input = tk.Entry(self.window, width=70)
        self.user_input.pack(padx=10, pady=10)
        self.user_input.bind("<Return>", self.handle_input)

        # Start the game
        self.display_room()
        self.window.mainloop()

    def handle_input(self, event):
        user_text = self.user_input.get().strip().lower()
        self.text_box.insert(tk.END, f"\n> {user_text}\n")
        self.user_input.delete(0, tk.END)
        handle_action(user_text)
        self.display_room()

    def display_room(self):
        current_room = getattr(rooms_code, player["current_room"])
        self.text_box.insert(tk.END, f"\n\n{current_room.name.upper()}\n")
        self.text_box.insert(tk.END, f"{current_room.description}\n")

        if current_room.items:
            self.text_box.insert(tk.END, "\nYou see:\n")
            for item in current_room.items:
                self.text_box.insert(tk.END, f"{item}\n")

        if current_room.enemies:
            self.text_box.insert(tk.END, "\nEnemy encounter!\n")
            scene = getattr(scene_code, current_room.fight_to)
            enemy = scene["enemy"]
            self.text_box.insert(tk.END, f"\n{enemy['name']} appears\n")

            action_button = tk.Button(
                self.window, text="Fight", command=lambda: self.fight(scene)
            )
            action_button.pack(pady=5)

        if current_room.doors:
            self.text_box.insert(tk.END, "\nDoors:\n")
            for direction, door in current_room.doors.items():
                self.text_box.insert(tk.END, f"{direction.capitalize()}: {door}\n")

    def fight(self, scene):
        # Get enemy and create template
        enemy = scene["enemy"]
        enemy_stats = PlayerStats(enemy["stats"])
        template = create_scene_template(scene)

        # Switch to fight scene
        self.user_input.delete(0, tk.END)
        action_button.destroy()
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert(tk.END, template)

        # Start fight
        while True:
            # Player turn
            player_attack = player_stats.attack()
            enemy_stats.stats["hp"] -= player_attack
            self