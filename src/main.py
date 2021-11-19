def main():
    start_screen = OptionsScreen("StartScreen", ["Mash up two songs", "Randomly mash up two songs"])
    song_fields_list = [
        "Song name: ",
        "Song genre: ",
        "Song tempo/BPM: ",
        "Song key: "
    ]
    pick_song_screen_1 = QuestionsScreen("PickSongScreen1", song_fields_list)
    pick_song_screen_2 = QuestionsScreen("PickSongScreen2", song_fields_list)
    mashing_progress_screen = Screen("MashingProgressScreen")
    playback_fields_list = [
        "Playback the mashup!",
        "Save the mashup",
        "Create a new mashup",
        "Exit the program"
    ]
    playback_screen = OptionsScreen("PlaybackScreen", playback_fields_list)
    all_screens = [start_screen, pick_song_screen_1, pick_song_screen_2, mashing_progress_screen, playback_screen]
    controller = Controller(all_screens)
    controller.start()

if "__init__" == "__main__":
    main()
