import array
import math
import numpy as np

import pygame

from Notes import Notes

# Replaces the C# switch: each note maps to its display name and frequency (Hz).
NOTE_INFO: dict[Notes, tuple[str, float]] = {
    Notes.LowE:       ("Low E",       164.814),
    Notes.LowF:       ("Low F",       174.614),
    Notes.LowFSharp:  ("Low F #",     184.997),
    Notes.LowG:       ("Low G",       195.998),
    Notes.LowGSharp:  ("Low G #",     207.652),
    Notes.LowA:       ("Low A",       220.000),
    Notes.LowASharp:  ("Low A #",     233.082),  # original C# had 223.082 (typo)
    Notes.LowB:       ("Low B",       246.942),
    Notes.MiddleC:    ("Middle C",    261.626),
    Notes.CSharp:     ("C #",         277.183),
    Notes.D:          ("D",           293.665),
    Notes.DSharp:     ("D #",         311.127),
    Notes.E:          ("E",           329.628),
    Notes.F:          ("F",           349.228),
    Notes.FSharp:     ("F #",         369.994),
    Notes.G:          ("G",           391.995),
    Notes.GSharp:     ("G #",         415.305),
    Notes.A:          ("A",           440.000),
    Notes.ASharp:     ("A #",         466.164),
    Notes.B:          ("B",           493.883),
    Notes.HighC:      ("High C",      523.251),
    Notes.HighCSharp: ("High C #",    554.365),
    Notes.HighD:      ("High D",      587.330),
    Notes.HighDSharp: ("High D #",    622.254),
    Notes.HighE:      ("High E",      659.255),
    Notes.HighF:      ("High F",      698.456),
    Notes.HighFSharp: ("High F #",    739.989),
    Notes.HighG:      ("High G",      783.991),
    Notes.HighGSharp: ("High G #",    830.609),
    Notes.HighA:      ("High A",      880.000),
    Notes.HighB:      ("High B",      987.767),
    Notes.TopCSharp:  ("Top C #",    1108.731),
}


SAMPLE_RATE = 44100

# The mixer must be initialised before any Sound is created (Sounds is built at import time).
pygame.mixer.init(frequency=SAMPLE_RATE, size=-16, channels=2)


def make_sound(frequency, duration=0.5, volume=0.5):
    sample_rate = SAMPLE_RATE

    t = np.arange(int(sample_rate * duration)) / sample_rate
    wave = (volume * 32767 * np.sin(2 * np.pi * frequency * t)).astype(np.int16)
    stereo = np.column_stack((wave, wave))  # same signal in left and right
    return pygame.sndarray.make_sound(stereo)


class PianoKey:
    """A Simple Class for Piano Keys"""
    Sounds = {note: make_sound(freq) for note, (name, freq) in NOTE_INFO.items()}

    def __init__(self, name, frequency, sort_order, note):
        self.Name = name
        self.Frequency = frequency
        self.SortOrder = sort_order
        self.Note = note

    @classmethod
    def play_note(cls, scale, char):
        """
        :type scale: list[]
        :type char: str
        """
        # The first 10 notes of each scale line up with the digits 0-9.
        note = scale[int(char)]
        # Print before playing, all on one line; flush so it shows before the wait.
        print(NOTE_INFO[note][0], end="  ", flush=True)
        sound = cls.Sounds[note]
        sound.play()
        # Block until the note finishes so notes play in sequence.
        pygame.time.wait(int(sound.get_length() * 1000))

    @classmethod
    def play_chord(cls, scale, char):
        """
        Play a triad built on the digit's note: the root plus the notes 2 and 4 steps above it.
        :type scale: list[]
        :type char: str
        """
        root = int(char)
        notes = [scale[root + step] for step in (0, 2, 4)]
        # Print before playing, all on one line; flush so it shows before the wait.
        print("[" + " ".join(NOTE_INFO[n][0] for n in notes) + "]", end="  ", flush=True)
        sounds = [cls.Sounds[n] for n in notes]
        for sound in sounds:
            channel = sound.play()
            # Split the volume between the notes so the mix doesn't clip.
            # play() resets channel volume, so single notes stay at full volume.
            if channel is not None:
                channel.set_volume(1 / len(sounds))
        pygame.time.wait(int(max(s.get_length() for s in sounds) * 1000))
