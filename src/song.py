class Song:

    def __init__(self, name=None, duration=None, full_audio=None, genre=None, vocal_audio=None, time_signature=None,
                 tempo=None, mode=None, key=None, instrumentalness=None, instrumental_audio=None):
        # overloaded constructor
        if name:
            self.name = name
            self.duration = duration
            self.full_audioudio = full_audio
            self.genre = genre
            self.vocal_audio = vocal_audio
            self.time_signature = time_signature
            self.tempo = tempo
            self.mode = mode
            self.key = key
            self.instrumentalness = instrumentalness
            self.instrumental_audio = instrumental_audio

        # default constructor
        else:
            self.name = ""
            self.duration = 0
            self.full_audio = "/"
            self.genre = ""
            self.vocal_audio = "/"
            self.time_signature = 0
            self.tempo = 0
            self.mode = True
            self.key = 0
            self.instrumentalness = 0.0
            self.instrumental_audio = "/"

    # getter/setter methods
    def set_name(self, n):
        self.name = n

    def get_name(self):
        return self.name

    def set_duration(self, d):
        self.duration = d

    def get_duration(self):
        return self.duration

    def set_full_audio(self, fa):
        self.full_audio = fa

    def get_full_audio(self):
        return self.full_audio

    def set_genre(self, g):
        self.genre = g

    def get_genre(self):
        return self.genre

    def set_vocal_audio(self, va):
        self.vocal_audio = va

    def get_vocal_audio(self):
        return self.vocal_audio

    def set_time_signature(self, ts):
        self.time_signature = ts

    def get_time_signature(self):
        return self.time_signature

    def set_tempo(self, t):
        self.tempo = t

    def get_tempo(self):
        return self.tempo

    def set_mode(self, m):
        self.mode = m

    def get_mode(self):
        return self.mode

    def set_key(self, k):
        self.key = k

    def get_key(self):
        return self.key

    def set_instrumentalness(self, i):
        self.instrumentalness = i

    def get_instrumentalness(self):
        return self.instrumentalness

    def set_instrumental_audio(self, ia):
        self.instrumental_audio = ia

    def get_instrumental_audio(self):
        return self.instrumental_audio
