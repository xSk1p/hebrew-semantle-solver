import requests
from random import choice

# API endpoint for similarity check
API_URL = "https://semantle.ishefi.com/api/distance?word="

# Function to check if a word is in hebrew
def is_hebrew(word):
    return all('\u0590' <= char <= '\u05FF' for char in word)

# Function to get similarity from the Semantle API
def get_similarity_from_api(word):
    try:
        response = requests.get(API_URL + word)
        if response.status_code == 200:
            data = response.json()
            print(f"API response for '{word}': {data}")  # Debugging: print the response
            
            # Check if the response is a list and has the expected structure
            if isinstance(data, list) and len(data) > 0 and 'similarity' in data[0]:
                # Extract the similarity value and divide by 100 to normalize it
                similarity = data[0]['similarity'] / 100
                return similarity
            else:
                print(f"Unexpected data format for word '{word}': {data}")
                return None
        else:
            print(f"Error: Received status code {response.status_code} for word '{word}'")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to request similarity for word '{word}': {e}")
        return None
    
# Function to submit initial guesses and get similarities
def submit_guesses(model, num_guesses=10):
    guesses = []
    similarities = {}

    while len(guesses) < num_guesses:
        word = choice(model.wv.index_to_key)  # Pick a random word
        if is_hebrew(word):  # Only append the word if it's Hebrew
            similarity = get_similarity_from_api(word)
            if similarity is not None:
                guesses.append(word)
                similarities[word] = similarity
                print(f"Similarity for '{word}': {similarity:.4f}")
            else:
                print(f"Failed to retrieve similarity for '{word}'")

    print(f"Trying Guesses: {guesses}")
    print(f"Similarities: {similarities}")
    return guesses, similarities

# Function to submit 10 initial guesses and get similarities
def submit_candidates(candidates):
    if candidates:
        print(f"Found {len(candidates)} possible words")
        print(f"\nPossible secret words based on similarities to the guesses: \n{candidates}")
        for candidate in candidates:
            print(f"Trying Candidate: {candidate}")
            candidate_similarity = get_similarity_from_api(candidate)
            if candidate_similarity > 0.95:
                print(f"======================================")
                print(f"  Secret Word Found! -- {candidate}")
                print(f"======================================")
                break
    else:
        print("No candidates found with similar similarity profiles.")
