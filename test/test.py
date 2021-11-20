import pytest

# test song class
from src.song import Song


def test_song_class_default_constructor():
    song = Song()
    assert song.name == ""
    assert song.duration == 0
    assert song.fullAudio == "/"
    assert song.genre == ""
    assert song.vocalAudio == "/"
    assert song.timeSignature == 0
    assert song.tempo == 0
    assert song.mode
    assert song.key == 0
    assert song.instrumentalness == 0.0
    assert song.instrumentalAudio == "/"


def test_song_class_constructor():
    song = Song("song name", 3, "/c/Users/lfang/Music", "EDM", "/c/Users/lfang/Music", 3, 160, True, 1, 5.0,
                "/c/Users/lfang/Music")
    assert song.name == "song name"
    assert song.duration == 3
    assert song.fullAudio == "/c/Users/lfang/Music"
    assert song.genre == "EDM"
    assert song.vocalAudio == "/c/Users/lfang/Music"
    assert song.timeSignature == 3
    assert song.tempo == 160
    assert song.mode
    assert song.key == 1
    assert song.instrumentalness == 5.0
    assert song.instrumentalAudio == "/c/Users/lfang/Music"


def test_song_class_set_method():
    song = Song()
    song.set_name("new name")
    assert song.name == "new name"


def test_song_class_get_method():
    song = Song()
    assert song.get_duration() == 0
