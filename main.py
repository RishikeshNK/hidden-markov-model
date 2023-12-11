def viterbi(
    obs: tuple[str, ...],
    states: tuple[str, ...],
    start_p: dict[str, float],
    trans_p: dict[str, dict[str, float]],
    emit_p: dict[str, dict[str, float]],
) -> tuple[list[str], float]:
    """
    Viterbi algorithm for Hidden Markov Models (HMMs)

    Parameters:
    - obs: list, sequence of observed events
    - states: list, possible hidden states
    - start_p: dict, initial probabilities of each state
    - trans_p: dict of dicts, transition probabilities between states
    - emit_p: dict of dicts, emission probabilities of observed events given each state

    Returns:
    - path: list, the most likely sequence of hidden states
    - max_prob: float, the probability of the most likely path
    """
    V: list[dict[str, float]] = [{}]
    path = {}

    # Initialize base cases (t == 0)
    for state in states:
        V[0][state] = start_p[state] * emit_p[state][obs[0]]
        path[state] = [state]

    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        V.append({})
        new_path = {}

        for current_state in states:
            (prob, state) = max(
                (
                    V[t - 1][prev_state]
                    * trans_p[prev_state][current_state]
                    * emit_p[current_state][obs[t]],
                    prev_state,
                )
                for prev_state in states
            )
            V[t][current_state] = prob
            new_path[current_state] = path[state] + [current_state]

        # Update the best path
        path = new_path

    # Find the maximum probability and corresponding best path
    (max_prob, last_state) = max((V[len(obs) - 1][state], state) for state in states)

    return path[last_state], max_prob


def main() -> None:
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


if __name__ == "__main__":
    main()
