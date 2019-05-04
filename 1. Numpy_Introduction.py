import numpy as np

positions = ['GK', 'M', 'A', 'D']
heights = [191, 184, 185, 180]

# Convert positions and heights to numpy arrays: np_positions, np_heights
np_heights = np.array(heights)
np_positions = np.array(positions)

# Heights of the goalkeepers: gk_heights
gk_heights = np_heights[np_positions  == 'GK']

# Heights of the other players: other_heights
other_heights = np_heights[np_positions != 'GK']

# Median height of goalkeepers
print("Median height of goalkeepers: " + str(np.median(gk_heights)))

# Median height of other players
print("Median height of other players: " + str(np.median(other_heights)))