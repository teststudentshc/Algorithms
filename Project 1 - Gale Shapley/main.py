import preferences
import gale_shapley

def main():
    """Loads preferences and runs the Gale-Shapley algorithm."""
    positions, interns = preferences.load_preferences()

    # Ensure preferences were loaded correctly
    if not positions or not interns:
        print("Error: Preference files could not be loaded correctly.")
        return

    # Run the Gale-Shapley algorithm
    matching = gale_shapley.gale_shapley(positions, interns)

    # Display the results
    print("\nFinal Stable Matching:")
    for p, i in enumerate(matching):
        print(f"Position {p+1} is matched with Intern {i+1}")

if __name__ == "__main__":
    main()
