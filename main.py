import time

from Notes import Notes, Scales
from PianoKey import PianoKey
from build_scale import get_scale
from MathFunctions import calculate_pi, calculate_fibonacci, calculate_primes, calculate_golden_ratio, calculate_collatz

Notes = Notes


def play_sequence(label, digits, scale):
    """Print the sequence, then play a chord for each digit (skipping anything else, like the '.')."""
    print(f"{label}: {digits}")
    for char in digits:
        if not char.isdigit():
            continue

        PianoKey.play_chord(scale, char)

    # End the line of printed notes.
    print()


"""Load stuff into memory"""
scale_to_play = get_scale(Scales.CMajor)

pi = calculate_pi(10)
fibonacci = calculate_fibonacci(12)
primes = calculate_primes(10)
golden_ratio = calculate_golden_ratio(15)
collatz = calculate_collatz(7)


"""play the notes"""
play_sequence("Pi", pi, scale_to_play)
time.sleep(3)
play_sequence("Fibonacci", fibonacci, scale_to_play)
time.sleep(3)
play_sequence("Primes", primes, scale_to_play)
time.sleep(3)
play_sequence("Golden ratio", golden_ratio, scale_to_play)
time.sleep(3)
play_sequence("Collatz from 7", collatz, scale_to_play)
