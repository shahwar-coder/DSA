'''
4. Playlist Editor
Task:
Implement a simple playlist editor. You start with an empty playlist (a list of song titles). You receive a sequence of commands of two types:

("add", idx, title) → insert title at position idx (use insert())

("play", idx) → remove and return the song at idx (use pop(idx))

At the end, return a tuple (final_playlist, played_songs) where:

final_playlist is the list after all commands,

played_songs is the list of titles returned by each "play" in the order they were played.

Goal:
Combine insert() and pop(i) to simulate a real‐world editing workflow.

# Example
commands = [
    ("add", 0, "SongA"),
    ("add", 1, "SongB"),
    ("add", 1, "SongC"),
    ("play", 0),
    ("add", 2, "SongD"),
    ("play", 1)
]
# Step-by-step:
#  [] 
#  insert(0,"SongA") → ["SongA"]
#  insert(1,"SongB") → ["SongA","SongB"]
#  insert(1,"SongC") → ["SongA","SongC","SongB"]
#  play pop(0) → "SongA", playlist = ["SongC","SongB"]
#  insert(2,"SongD") → ["SongC","SongB","SongD"]
#  play pop(1) → "SongB", playlist = ["SongC","SongD"]
# Final: (["SongC","SongD"], ["SongA","SongB"])
'''

