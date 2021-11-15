class Song:
    # default constructor
    def __init__(self):
        self.name = ""
        self.duration = 0
        self.fullAudio = "/"
        self.genre = ""
        self.vocalAudio = "/"
        self.timeSignature = 0
        self.tempo = 0
        self.mode = True
        self.key = 0
        self.instrumentalness = 0.0
        self.instrumentalAudio = "/"

    # constructor
    def __int__(self, name, duration, fullAudio, genre, vocalAudio, timeSignature, tempo, mode, key, instrumentalness, instrumentalAudio):
        self.name = name
        self.duration = duration
        self.fullAudio = fullAudio
        self.genre = genre
        self.vocalAudio = vocalAudio
        self.timeSignature = timeSignature
        self.tempo = tempo
        self.mode = mode
        self.key = key
        self.instrumentalness = instrumentalness
        self.instrumentalAudio = instrumentalAudio

    # getter/setter methods
    def set_name(self, n):
        self.name = n

    def get_name(self):
        return self.name

    def set_duration(self, d):
        self.duration = d

    def get_duration(self):
        return self.duration

    def set_fullAudio(self, fA):
        self.fullAudio = fA

    def get_fullAudio(self):
        return self.fullAudio

    def set_genre(self, g):
        self.genre = g

    def get_genre(self):
        return self.genre

    def set_vocalAudio(self, vA):
        self.vocalAudio = vA

    def get_vocalAudio(self):
        return self.vocalAudio

    def set_timeSignature(self, tS):
        self.timeSignature = tS

    def get_timeSignature(self):
        return self.timeSignature

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

    def set_instrumentalAudio(self, iA):
        self.instrumentalAudio = iA

    def get_instrumentalAudio(self):
        return self.instrumentalAudio
