def guess_number(number:int=1, range_min=1, range_max=100) -> int:
    """Guessing a number in a given range by sequentially checking and halving the possible range boundaries

    Args:
        number (int, optional): the hidden number. Defaults to 1.
        range_min (int, optional): start range of guessed numbers. Defaults to 1.
        range_max (int, optional): end range of guessed numbers. Defaults to 100.

    Returns:
        int: number of attempts
    """
    
    count = 0

    while True:
        count += 1
        predict_number = (range_max + range_min) // 2 # guessing the number in the middle of the possible range
        if number < predict_number:
            range_max = predict_number - 1
        elif number > predict_number:
            range_min = predict_number + 1
        else:
            break # exit the loop if the number is guessed
        
    return count


import numpy as np


def score_game(guess_number) -> int:
    """For how many attempts, on average, for 1000 passes, our algorithm will guess the number
    
    Args:
        guess_number(int): guessing function

    Returns:
        int: average number of attempts
    """
    
    count_ls = []
    np.random.seed(1)  # we fix the seed for reproducibility
    random_array = np.random.randint(1, 101, size=(1000))  # generated list of numbers

    for number in random_array:
        count_ls.append(guess_number(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number in an average of {score} attempts")
    return score


if __name__ == "__main__":
    # RUN
    score_game(guess_number)