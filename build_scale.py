from Notes import Notes as Notes, Scales


def get_scale(name):
    """
    Each scale holds 14 notes: one per digit (0-9) plus 4 more on top so chords
    built on the highest digits still have their upper notes.
    :type name: Scales
    """
    scale = []
    if name == Scales.CMajor:
        scale =  [Notes.LowB, Notes.MiddleC, Notes.D, Notes.E, Notes.F, Notes.G, Notes.A, Notes.B, Notes.HighC, Notes.HighD,
                  Notes.HighE, Notes.HighF, Notes.HighG, Notes.HighA]
    elif name == Scales.CMinor:
        scale = [Notes.LowASharp, Notes.MiddleC, Notes.D, Notes.DSharp, Notes.F, Notes.G, Notes.GSharp, Notes.ASharp, Notes.HighC, Notes.HighD,
                 Notes.HighDSharp, Notes.HighF, Notes.HighG, Notes.HighGSharp]
    elif name == Scales.DMajor:
        scale = [Notes.CSharp, Notes.D, Notes.E, Notes.FSharp, Notes.G, Notes.A, Notes.B, Notes.HighCSharp, Notes.HighD, Notes.HighE,
                 Notes.HighFSharp, Notes.HighG, Notes.HighA, Notes.HighB]
    elif name == Scales.EMajor:
        scale = [Notes.DSharp, Notes.E, Notes.FSharp, Notes.GSharp, Notes.A, Notes.B, Notes.HighCSharp, Notes.HighDSharp,Notes.HighE, Notes.HighFSharp,
                 Notes.HighGSharp, Notes.HighA, Notes.HighB, Notes.TopCSharp]
    elif name == Scales.AMinor:
        scale = [Notes.LowG, Notes.LowA, Notes.LowB, Notes.MiddleC, Notes.D, Notes.E, Notes.F, Notes.G, Notes.A, Notes.B,
                 Notes.HighC, Notes.HighD, Notes.HighE, Notes.HighF]
    elif name == Scales.FMajor:
        scale = [Notes.LowE, Notes.LowF, Notes.LowG, Notes.LowA, Notes.LowASharp, Notes.MiddleC, Notes.D, Notes.E,Notes.F, Notes.G,
                 Notes.A, Notes.ASharp, Notes.HighC, Notes.HighD]
    elif name == Scales.GMajor:
        scale = [Notes.LowFSharp, Notes.LowG, Notes.LowA, Notes.LowB, Notes.MiddleC, Notes.D, Notes.E, Notes.FSharp, Notes.G, Notes.A,
                 Notes.B, Notes.HighC, Notes.HighD, Notes.HighE]
    elif name == Scales.HarmonicAMinor:
        scale = [Notes.LowGSharp, Notes.LowA, Notes.LowB, Notes.MiddleC, Notes.D, Notes.E, Notes.F, Notes.GSharp,Notes.A, Notes.B,
                 Notes.HighC, Notes.HighD, Notes.HighE, Notes.HighF]

    return scale
