from tqdm import tqdm
from semantle import submit_guesses

# Function to calculate similarity between a guess and the secret word
def check_similarity(model,guess, secret_word):
    if guess in model.wv.index_to_key and secret_word in model.wv.index_to_key:
        return model.wv.similarity(guess, secret_word)
    else:
        return None
    
# Function to compare similarity of a word to a list of guesses
def compare_similarities(model, word, guesses, guess_similarities, tolerance=0.3):
    for guess in guesses:
        try:
            sim = model.wv.similarity(word, guess)
            if abs(sim - guess_similarities[guess]) > tolerance:  
                return False
        except KeyError:
            return False
    return True

# Function to filter possible candidates by guessing another 5 words
def filter_candidates(model, candidates, guesses, similarities, tolerance, max_candidates):
    while len(candidates) > max_candidates:
        filtered_candidates = []
        guesses,similarities = submit_guesses(model, 5)
        for word in tqdm(candidates, desc="Narrowing Down Options"):
            if compare_similarities(model, word, guesses, similarities, tolerance):
                filtered_candidates.append(word)
        candidates = filtered_candidates
    return candidates

# Function to get possible candidates by checking similarties to the initial X guesses 
def get_candidates(model, guesses, similarities, tolerance, max_candidates):
    candidates = []
    for word in tqdm(model.wv.index_to_key, desc="Searching for possible secret words"):
        if compare_similarities(model,word, guesses, similarities, tolerance):
            candidates.append(word)
    candidates = filter_candidates(model, candidates, guesses, similarities, tolerance, max_candidates)
    return candidates
