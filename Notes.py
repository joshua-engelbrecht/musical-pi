from enum import Enum, auto


class Notes(Enum):
    LowASharp = 0
    LowB = 1
    MiddleC = 2
    CSharp = 3
    D = 4
    DSharp = 5
    E = 6
    ESharp = 7
    F = 8
    FSharp = 9
    G = 10
    GSharp = 11
    A = 12
    ASharp = 13
    B = 14
    BSharp = 15
    HighC = 16
    HighCSharp = 17
    HighD = 18
    HighE = 19
    HighFSharp = 20
    HighDSharp = 21
    LowA = 22
    LowG = 23
    LowE = 24
    LowF = 25
    LowGSharp = 26
    LowFSharp = 27
    HighF = 28
    HighG = 29
    HighGSharp = 30
    HighA = 31
    HighB = 32
    TopCSharp = 33

class Scales(Enum):
    CMajor = auto()
    CMinor = auto()
    DMajor = auto()
    EMajor = auto()
    AMinor = auto()
    FMajor = auto()
    GMajor = auto()
    HarmonicAMinor = auto()
