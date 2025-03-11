## Problem Statement  
The **Stable Matching Problem** involves pairing two groups in a way that ensures **stability**. A pairing is considered **stable** if no two entities prefer each other over their assigned match.  

The **Gale-Shapley algorithm** (Deferred Acceptance Algorithm) is a well-known solution to this problem. In class, we introduced it using a **dating example** and **general n × n pairings**.  

For this assignment, we will apply the algorithm to match **interns** with **positions** (companies). Each **intern** has a ranked preference list of **positions**, and each **position** has a ranked preference list of **interns**. The goal is to ensure that no unmatched **intern-position** pair prefers each other over their current assignments.

---

## Gale-Shapley Algorithm (Pseudocode)  
The algorithm proceeds in rounds, where each **position** proposes to **interns** in order of its preference list.

1. Start with **all positions unmatched**.  
2. Each **unmatched position** proposes to its most preferred **intern** who has not yet rejected it.  
3. The **intern** considers the proposal:
   - If the intern is **unmatched**, they accept the proposal.  
   - If the intern is **already matched**:
     - If they prefer the **new position** over their current match, they switch.
     - Otherwise, they reject the proposal.  
4. The algorithm **repeats** until all positions are matched.  

This algorithm **always** produces a stable matching in **O(n²) time complexity**.

---

## Files Provided  
Your project folder contains the following files:

Project Folder  
│── data  
│   ├── positions.txt    # Preference list for positions (companies)  
│   ├── interns.txt      # Preference list for interns (candidates)  
│  
│── preferences.py       # Loads the preference data (DO NOT MODIFY)  
│── gale_shapley.py      # Implements the Gale-Shapley algorithm (YOU WILL COMPLETE THIS)  
│── main.py              # Runs the program (DO NOT MODIFY)  

---

## Input File Format  
Both `positions.txt` and `interns.txt` follow this format:  
Each line represents the ranked preferences of an entity.

### Example: `positions.txt`  
0 1 2  
1 2 0  
2 0 1  

Interpretation:  
- Position 0 prefers intern **0 > 1 > 2**  
- Position 1 prefers intern **1 > 2 > 0**  
- Position 2 prefers intern **2 > 0 > 1**  

### Example: `interns.txt`  
0 1 2  
1 2 0  
2 0 1  

Interpretation:  
- Intern 0 prefers position **0 > 1 > 2**  
- Intern 1 prefers position **1 > 2 > 0**  
- Intern 2 prefers position **2 > 0 > 1**  

---

## Your Task  
You will **only modify** `gale_shapley.py`. The other files are **pre-implemented** to provide structure.

Hints are provided in `gale_shapley.py` to guide your implementation.

---

## Running the Program  
Once you have implemented `gale_shapley.py`, run:  
python main.py  

Expected output:  
Final Stable Matching:  
Position 1 is matched with Intern 1  
Position 2 is matched with Intern 2  
Position 3 is matched with Intern 3  

---

## Grading Criteria  
| **Category**                  | **Points** |  
|-------------------------------|------------|  
| Code correctness & logic      | 30 pts     |  
| Proper use of data structures | 20 pts     |  
| Readability & comments        | 15 pts     |  
| Proper handling of input data | 15 pts     |  
| Successful execution & output | 20 pts     |  
| **Total**                     | **100 pts**|  

**Bonus (10 pts)** may be awarded for exceptional creativity, efficiency, or optimizations.

---

## Notes  
- **Do not modify `preferences.py` or `main.py`.**  
- Your solution should work for **any valid input**, not just the example provided.  
- Ensure your code is well-commented for readability.  
- If you have any questions, contact the instructor.  
