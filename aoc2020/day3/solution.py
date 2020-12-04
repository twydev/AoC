with open('input.txt', 'r') as f:
    horizontal_tracks = f.read().splitlines()

class CircularTrack:
    def __init__(self, track_map):
        self.track_map = track_map
    
    def is_tree_at_position(self, pos):
        index = pos % len(self.track_map)
        return self.track_map[index] == '#'

class Position:
    def __init__(self):
        self.position = [0, 0]
    
    def x(self):
        return self.position[0]
    
    def y(self):
        return self.position[1]
    
    def next_step(self, increment):
        self.position = [self.x() + increment[0], self.y() + increment[1]]
    
    def get_coordinates(self):
        return self.position

circular_tracks = [CircularTrack(track_map) for track_map in horizontal_tracks]

movement_options = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

running_product = 1
for option in movement_options:
    current_position = Position()
    trees_encountered = 0
    while current_position.y() < len(circular_tracks) - 1:
        current_position.next_step(option)
        current_track = circular_tracks[current_position.y()]
        if current_track.is_tree_at_position(current_position.x()):
            trees_encountered += 1
    print(trees_encountered)
    running_product *= trees_encountered

print(running_product)
