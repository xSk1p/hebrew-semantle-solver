import os 
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from semantle import submit_guesses,submit_candidates
from similarity import get_candidates
from model import loadModel

if __name__ == "__main__":
    model = loadModel()

    guesses,initial_similarities = submit_guesses(model, 10)

    candidates = get_candidates(model,guesses,initial_similarities,tolerance=0.1, max_candidates=10) # Hold candidates
    submitCandidates = submit_candidates(candidates) # Submit
    
            



