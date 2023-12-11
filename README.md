# Hidden Markov Model (HMM) - Viterbi Algorithm

This Python script implements the Viterbi algorithm for Hidden Markov Models (HMMs). The algorithm is used to find the most likely sequence of hidden states given a sequence of observed events. This is a final project for MATH 4581: Statistics and Stochastic Processes.

## Usage

### Prerequisites

- Python 3.8+

### Getting Started

1. Clone the repository or download the script.

    ```bash
    git clone git@github.com:RishikeshNK/hidden-markov-model.git
    ```

2. Navigate to the project directory.

    ```bash
    cd hidden-markov-model
    ```

3. Run the script.

    ```bash
    python main.py
    ```

### Input

The script is designed to work with the following input parameters:

- `obs`: A tuple representing the sequence of observed events.
- `states`: A tuple of possible hidden states.
- `start_p`: A dictionary containing the initial probabilities of each state.
- `trans_p`: A dictionary of dictionaries representing transition probabilities between states.
- `emit_p`: A dictionary of dictionaries representing emission probabilities of observed events given each state.

### Output

The script returns a tuple containing:
- `path`: A list representing the most likely sequence of hidden states.
- `max_prob`: A float representing the probability of the most likely path.

## Example

```python
obs = ("Flat", "Upward", "Downward", "Downward", "Flat", "Flat", "Flat")
states = ("Bullish", "Bearish", "Neutral")
start_p = {"Bullish": 0.4, "Bearish": 0.3, "Neutral": 0.3}
trans_p = {
    "Bullish": {"Bullish": 0.5, "Bearish": 0.2, "Neutral": 0.3},
    "Bearish": {"Bullish": 0.2, "Bearish": 0.5, "Neutral": 0.3},
    "Neutral": {"Bullish": 0.3, "Bearish": 0.2, "Neutral": 0.5},
}
emit_p = {
    "Bullish": {"Upward": 0.5, "Downward": 0.2, "Flat": 0.3},
    "Bearish": {"Upward": 0.3, "Downward": 0.5, "Flat": 0.2},
    "Neutral": {"Upward": 0.3, "Downward": 0.2, "Flat": 0.5},
}

path, prob = viterbi(obs, states, start_p, trans_p, emit_p)

print(f"Highest Probable Path: {' → '.join(path)}")
print(f"Probability: {prob}")
```