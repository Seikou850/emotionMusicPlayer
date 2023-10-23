import pygame
import os

class EmotionMusicPlayer:

    def __init__(self, music_folder, student_id):
        self.is_access_granted = False  # Initially, access is denied
        self.student_id = student_id  # Define the student_id attribute
        self.music_folder = music_folder
        self.favorite_songs = []
        self.current_mood = None
        self.current_playlist = {}
        self.song_index = 0
        pygame.mixer.init()


        self.song_info = {
            'a-1.mp3': {'name': 'Menace', 'artist': 'Sione'},
            'a-2.mp3': {'name': 'Es geht mir gut', 'artist': 'LGM'},
            'a-3.mp3': {'name': 'Encode', 'artist': 'Vivid'},
            'h-1.mp3': {'name': 'Indifferent', 'artist': 'The Newmen'},
            'h-2.mp3': {'name': 'Summer Time', 'artist': 'Morning Light Music'},
            'h-3.mp3': {'name': 'Fun Memories', 'artist': 'Morning Light Music'},
            's-1.mp3': {'name': 'Sky Aspens World', 'artist': 'Unknown Artist'},
            's-2.mp3': {'name': 'Sad Emotional Piano', 'artist': 'DS Productions'},
            's-3.mp3': {'name': '4. November', 'artist': 'XrYA'},
            'r-1.mp3': {'name': 'Sunrise Tranquility', 'artist': 'Unipurpose'},
            'r-2.mp3': {'name': 'Sleep Relaxed', 'artist': 'Music Relax'},
            'r-3.mp3': {'name': 'Frostful Night', 'artist': 'Silent Sea'},
            'e-1.mp3': {'name': 'Techno Party', 'artist': 'Tujamo, Vienne, Murotani'},
            'e-2.mp3': {'name': 'Vrah', 'artist': 'Jv Torren'},
            'e-3.mp3': {'name': 'CyberPunk', 'artist': 'BROOKXLYN'},
            # Define the song info for other songs in a similar way.
        }

        self.moods = {
            1: {
                'description': 'Happy',
                'songs': [os.path.join(self.music_folder, 'h-1.mp3'), #Name of the music: Indifferent by The Newmen
                          os.path.join(self.music_folder, 'h-2.mp3'), #Name of the music: Summer Time by Morning Light Music
                          os.path.join(self.music_folder, 'h-3.mp3')] #Name of the music: Fun Memories by Morning Light Music
            },
            2: {
                'description': 'Sad',
                'songs': [os.path.join(self.music_folder, 's-1.mp3'), #Name of the music: Sky Aspens World
                          os.path.join(self.music_folder, 's-2.mp3'), #Name of the music: Sad Emotional Piano by DS Productions
                          os.path.join(self.music_folder, 's-3.mp3')] #Name of the music: 4. November by XrYA
            },
            3: {
                'description': 'Relaxed',
                'songs': [os.path.join(self.music_folder, 'r-1.mp3'), #Name of the music: Sunrise Tranquility By Unipurpose
                          os.path.join(self.music_folder, 'r-2.mp3'), #Name of the music: Sleep Relaxed by Music Relax
                          os.path.join(self.music_folder, 'r-3.mp3')] #Name of the music: Frostful Night by Silent Sea
            },
            4: {
                'description': 'Angry',
                'songs': [os.path.join(self.music_folder, 'a-1.mp3'), #Name of the music: Menace by Sione
                          os.path.join(self.music_folder, 'a-2.mp3'), #Name of the music: Es geht mir gut by LGM
                          os.path.join(self.music_folder, 'a-3.mp3')] #Name of the music: Encode by Vivid
            },
            5: {
                'description': 'Energetic',
                'songs': [os.path.join(self.music_folder, 'e-1.mp3'), #Name of the music: Techno Party bu Tujamo, Vienne, Murotani
                          os.path.join(self.music_folder, 'e-2.mp3'), #Name of the music: Vrah by Jv Torren
                          os.path.join(self.music_folder, 'e-3.mp3')] #Name of the music: CyberPunk by BROOKXLYN
            }
        }

    def check_student_access(self):
        entered_id = input("Enter your student ID to access the Emotion-Based Music Player: ")
        if entered_id == self.student_id:
            return True
        else:
            print("Access denied. The provided student ID does not match.")
            return False

    def check_student_access(self):
        entered_id = input("Enter your student ID to access the Emotion-Based Music Player: ")
        if entered_id == self.student_id:
            return True
        else:
            print("Access denied. The provided student ID does not match.")
            return False
    def stop_music(self):
        pygame.mixer.music.stop()

    def play_music(self, song_path):
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()

    def play_music_from_folder(self, playlist):
        self.current_playlist = playlist
        self.song_index = 0
        self.play_music(self.current_playlist['songs'][self.song_index])
        self.options()

    def change_mood(self):
        mood_number = self.choice_mood()
        new_mood = self.moods.get(mood_number, {'description': 'Unknown Mood', 'songs': []})
        self.play_music_from_folder(new_mood)

    def play_next_song(self):
        self.song_index = (self.song_index + 1) % len(self.current_playlist['songs'])
        self.play_music(self.current_playlist['songs'][self.song_index])

    def play_previous_song(self):
        self.song_index = (self.song_index - 1) % len(self.current_playlist['songs'])
        self.play_music(self.current_playlist['songs'][self.song_index])

    def choice_mood(self):
        print("Choose your mood:")
        for mood_num, mood_data in self.moods.items():  # Corrected: Access self.moods
            print(f"{mood_num}: {mood_data['description']}")
        return int(input("Enter the number for your mood: "))

    def welcome_message(self):
        print("Welcome to the Emotion-Based Music Player!")
        print("Select your mood to start listening to music.")

    def options(self):
        while True:
            print("|----------------------------|")
            print("|Options:                    |")
            print("|----------------------------|")
            print("| 1. Next Song               |")
            print("| 2. Previous Song           |")
            print("| 3. Change Mood             |")
            print("| 4. View Favourites         |")
            print("| 5. Add to Favourites       |")
            print("| 6. Play Favourites         |")
            print("| 7. Stop Music              |")
            print("|----------------------------|")
            # Get the current song's name and artist
            current_song_name = self.song_info.get(os.path.basename(self.current_playlist['songs'][self.song_index]),
                                                   {})
            name = current_song_name.get('name', '')
            artist = current_song_name.get('artist', '')

            # Print the name and artist without the file name
            print(f"Currently Playing: {name} by {artist}")

            choice = input("Enter your choice (1-7):")

            if choice == '1':
                self.play_next_song()
            elif choice == '2':
                self.play_previous_song()
            elif choice == '3':
                self.change_mood()
            elif choice == '4':
                self.view_favorites()
            elif choice == '5':
                self.add_to_favorites(self.current_playlist['songs'][self.song_index])
            elif choice == '6':
                self.play_favorites()
            elif choice == '7':
                self.stop_music()
        else:
            print("Invalid choice. Please select a valid option.")

    def view_favorites(self):
        print("Favorite Songs:")
        for song in self.favorite_songs:
            print(song)

    def add_to_favorites(self, song_path):
        self.favorite_songs.append(song_path)
        print(f"{song_path} added to favorites.")

    def play_favorites(self):
        if not self.favorite_songs:
            print("You don't have any favorite songs yet. Add some to your favorites.")
            return

        favorite_playlist = {'description': 'Favorites',
                             'songs': [os.path.join(self.music_folder, song) for song in self.favorite_songs]}
        self.play_music_from_folder(favorite_playlist)

    def run(self):
        if not self.check_student_access():
            return

        if self.is_access_granted:
            self.start_music_player()

        self.welcome_message()
        mood_number = self.choice_mood()
        initial_mood = self.moods.get(mood_number, {'description': 'Unknown Mood', 'songs': []})
        self.play_music_from_folder(initial_mood)

