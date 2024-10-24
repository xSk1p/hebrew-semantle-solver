# hebrew-semantle-solver

After countless sleepless nights, and seeing our entire group of friends' lives tearing apart because of the so-called [Hebrew Semantle](https://semantle.ishefi.com/) "game". I knew I had to do something. So, I built this Python project to process the possible secret words based on guesses' similarity, using a pre-trained Word2Vec model created by [Iddo Yadlin](https://github.com/Iddoyadlin/hebrew-w2v) (similar model to the one used in the Semantle game).

## Overview


The hebrew-semantle-solver project automates the word-guessing process using a similarity-based approach:

- **Initial Guesses**: The script starts by making 10 guesses.
- **Similarity Filtering**: It then finds words with close similarities to these initial guesses.
- **Narrowing Down**: If there are too many candidates, the script guesses 5 additional words to refine the candidate list.
- **Submission**: Once the number of candidates is small enough (defined by max_candidates), the script submits each word to the Semantle API to check if the secret word is found.

    #### Demo
    ![Watch the hebrew-semantle-solver Demo](./semantle.gif)


### Installation
 - Clone the repository: `git clone https://github.com/xSk1p/hebrew-semantle-solver.git`
 - Navigate to the project directory: `cd Semantle-Solver`
 - Install the required dependencies: `pip install -r requirements.txt`
 - Ensure the pre-trained model is placed in the project `model` directory.
 - Run the script `python main.py`

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more information.

### Model License
The pre-trained Word2Vec model by [Iddo Yadlin](https://github.com/Iddoyadlin/hebrew-w2v) is also licensed under the Apache License 2.0. The usage of this model in the Semantle-Solver project complies with the terms of the Apache 2.0 license.
