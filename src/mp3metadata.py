from mutagen.easyid3 import EasyID3
import os

def main():
    songs_folder = "Songs/"
    for song in os.listdir(songs_folder):
        print(song)
        if ".mp3" in song:
            audio = EasyID3(f"{songs_folder}{song}")
            audio['title'] = song.replace(".mp3", "")
            audio.save()
            print("Metadata updated!")
            print("="*50)

        else:
            print("Skipped!")
        

if __name__ == "__main__":
    main()
 