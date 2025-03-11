import os

def load_preferences():
    """
    Reads the preference lists from text files and returns them as lists.

    - `positions.txt`: Each line contains space-separated intern preferences for a position.
    - `interns.txt`: Each line contains space-separated position preferences for an intern.
    
    Returns:
    - `positions`: A 2D list where `positions[p]` contains the preference list of position `p`.
    - `interns`: A 2D list where `interns[i]` contains the preference list of intern `i`.
    """
    try:
        # Check if files exist
        if not os.path.exists("data/positions.txt"):
            print("Error: positions.txt not found!")
            return [], []
        if not os.path.exists("data/interns.txt"):
            print("Error: interns.txt not found!")
            return [], []

        # Read positions
        with open("data/positions.txt", "r") as f:
            positions = [line.strip().split() for line in f.readlines() if line.strip()]

        # Read interns
        with open("data/interns.txt", "r") as f:
            interns = [line.strip().split() for line in f.readlines() if line.strip()]

        return positions, interns

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return [], []
