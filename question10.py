songs = [
    "Song A",
    "Song B",
    "Song C",
    "Song D",
    "Song E",
    "Song F",
    "Song G",
    "Song H"
]

print("Complete Playlist")
print(songs)

print("First 3 Songs")
print(songs[0:3])

print("Last 3 Songs")
print(songs[-3:])

print("Songs from Position 3 to 6")
print(songs[3:6])

print("Every Alternate Song")
print(songs[::2])

print("Playlist in Reverse Order")
print(songs[::-1])

print("Playlist Without First and Last Song")
print(songs[1:-1])

short_playlist = songs[2:6]

short_playlist[0] = "Song X"

print("Original Playlist")
print(songs)

print("Short Playlist")
print(short_playlist)