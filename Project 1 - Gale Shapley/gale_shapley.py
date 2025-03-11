def gale_shapley(positions, interns):
    """
    Implements the Gale-Shapley stable matching algorithm using only 2D arrays.

    Instructions:
    - Positions (employers) propose to interns in order of preference.
    - Interns may accept or reject proposals based on their own rankings.
    - The algorithm continues until all positions are matched to an intern.
    - Use the provided variables and hints to complete the missing parts.
    """

    num_positions = len(positions)
    num_interns = len(interns)
    
    # List of unmatched positions
    unmatched_positions = list(range(num_positions))  

    # Tracks which intern each position will propose to next
    next_intern = [0] * num_positions  

    # Stores which position each intern is currently matched with (-1 = unmatched)
    matching = [-1] * num_interns  

    # Stores which intern each position is matched with (-1 = unmatched)
    position_matches = [-1] * num_positions  

    # TODO: Populate the ranking matrix
    # rank[i][p] tells how much intern `i` prefers position `p`
    rank = [[0] * num_positions for _ in range(num_interns)]
    
    # HINT: Loop through interns[][] and fill rank[i][p] such that 
    #       rank[i][p] = k means intern `i` ranks position `p` at preference `k`.
    
    # TODO: Implement the Gale-Shapley matching loop
    while unmatched_positions:
        p = unmatched_positions.pop(0)  # Pick an unmatched position

        # TODO: Ensure position has valid choices left before proceeding
        # HINT: Check if `next_intern[p]` is still within bounds of `positions[p]`
        #       If `next_intern[p] >= len(positions[p])`, the position has no more interns to propose to.

        # TODO: Get the next intern this position wants to propose to
        # HINT: Retrieve `i = int(positions[p][next_intern[p]])` 
        #       and then increment `next_intern[p]` for the next round.

        # TODO: Check if intern is free
        # If free, accept proposal and update the matching
        # HINT: Check if `matching[i] == -1`
        #       If so, set `matching[i] = p` and `position_matches[p] = i`

        # TODO: If intern is already matched, check if they prefer the new position
        # HINT: Use the `rank[][]` array to determine preference.
        #       Compare `rank[i][p]` with `rank[i][current_p]` where `current_p = matching[i]`.
        
        # TODO: If the intern prefers the new position, update the matching and unmatch the old position
        # HINT: Set `matching[i] = p` and `position_matches[p] = i`
        #       Add `current_p` back to `unmatched_positions` since it's now unmatched.

        # TODO: Otherwise, reject the proposal and the position remains unmatched
        # HINT: Add `p` back to `unmatched_positions` to try again in the next iteration.

    return position_matches  # Returns final stable matching