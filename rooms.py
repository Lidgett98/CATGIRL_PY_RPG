from utils import Room

# Define rooms
entrance = Room("Entrance")
entrance.description = "You are at the entrance. The door behind you is locked. In front of you there are two paths: one leading to the left and one leading to the right."
entrance.add_exit("left", "path_left")
entrance.add_exit("right", "path_right")
entrance.add_item("key", "A small key")

path_left = Room("Left path")
path_left.description = "You are on a path that leads to the left. It looks like it hasn't been used in a long time. You can hear some rustling in the bushes nearby."
path_left.add_exit("back", "entrance")
path_left.add_exit("forward", "treasure_room")

treasure_room = Room("Treasure Room")
treasure_room.description = "You are in a treasure room! You see a pile of gold and jewels in front of you. There is also a strange object with a button on it."
treasure_room.add_exit("back", "path_left")
treasure_room.add_item("gold", "A pile of gold")
treasure_room.add_item("jewels", "A pile of jewels")
treasure_room.add_item("strange_object", "A strange object with a button on it")

path_right = Room("Right path")
path_right.description = "You are on a path that leads to the right. You can hear the sound of water in the distance."
path_right.add_exit("back", "entrance")
path_right.add_exit("forward", "waterfall")

waterfall = Room("Waterfall")
waterfall.description = "You are at a beautiful waterfall. The water is crystal clear and you can see some fish swimming in the water."
waterfall.add_exit("back", "path_right")
waterfall.add_exit("forward", "cave")

cave = Room("Cave")
cave.description = "You are in a dark cave. You can hear the sound of bats in the distance."
cave.add_exit("back", "waterfall")
cave.add_exit("forward", "dragon_room")

dragon_room = Room("Dragon Room")
dragon_room.description = "You are in a room with a dragon! The dragon looks at you and starts to breathe fire."
dragon_room.add_exit("back", "cave")
dragon_room.add_item("sword", "A sword")

# Define starting room
starting_room = entrance
