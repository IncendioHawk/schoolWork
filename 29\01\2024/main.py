import json
import random

def getPieces():
  with open("data/music.json", 'r') as file:
    data = file.read() 
    data = json.loads(data) 
    return data
  
def getPiece(name):
  data = getPieces()
  for piece in data:
    if piece["name"] == name:
      return piece
    
def writePieces(data):
  with open("data/music.json", 'w') as file:
    file.write(json.dumps(data))
    
def randomPiece():
  data = getPieces()
  return random.choice(data)

def addPiece(name, composer):
  data = getPieces()
  data.append({"name": name, "composer": composer})
  writePieces(data)

def removePiece(name):
  data = getPieces()
  for piece in data:
    if piece["name"] == name:
      data.remove(piece)
  writePieces(data)

def countPieces():
  data = getPieces()
  return len(data)

def shufflePieces():
  data = getPieces()
  random.shuffle(data)
  writePieces(data)

def newPlaylist(length):
  playlist = []
  for i in range:
    playlist.append({"name": input("Enter the name of the piece: "), "composer": input("Enter the name of the composer: ")})
  writePieces(playlist)

def main():
  print("Welcome to the music database!")
  while True:
    print("What would you like to do?")
    print("1. Add a piece\n2. Remove a piece\n3. Count the pieces\n4. Shuffle the pieces\n5. Create a new playlist\n6. Exit")
    choice = int(input("Enter your choice: "))
    match(choice):
      case 1:
        name = input("Enter the name of the piece: ")
        composer = input("Enter the name of the composer: ")
        addPiece(name, composer)
      case 2:
        name = input("Enter the name of the piece: ")
        removePiece(name)
      case 3:
        print("There are", countPieces(), "pieces")
      case 4:
        shufflePieces()
      case 5:
        length = int(input("Enter the length of the playlist: "))
        newPlaylist(length)
      case 6:
        print("Goodbye!")
        break
      case _:
        print("Invalid choice")
main()