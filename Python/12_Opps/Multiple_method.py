
# Creating a Playlist class with methods to add and display songs with multiple methods
class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Sneha-Favorites")
my_playlist.add_song("Butterfly Song")
my_playlist.add_song("Titlli udii")
my_playlist.show_songs()
