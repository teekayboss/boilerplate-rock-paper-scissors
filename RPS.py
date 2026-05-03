# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

    def player(prev_play, opponent_history=[], play_order={}):
    # 1. Handle the very first move
    if not prev_play:
        prev_play = 'R'
    opponent_history.append(prev_play)
    
    prediction = 'P' # Default guess

    # 2. Track patterns of 3 moves
    if len(opponent_history) > 3:
        last_three = "".join(opponent_history[-3:])
        play_order[last_three] = play_order.get(last_three, 0) + 1
        
        # 3. Look at the last two moves and predict the third
        potential_next_moves = [
            "".join(opponent_history[-2:]) + "R",
            "".join(opponent_history[-2:]) + "P",
            "".join(opponent_history[-2:]) + "S",
        ]
        
        # Find which of those 3 patterns happened most often in the past
        sub_order = {
            k: play_order[k]
            for k in potential_next_moves if k in play_order
        }

        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1]

    # 4. Counter the prediction (If they play R, you play P)
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]
