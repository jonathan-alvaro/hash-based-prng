import hashlib
import itertools

hash_algorithms = hashlib.algorithms_available

def run_hash_algorithm(hash_func, seed=b"Default seed", num_iters=100):
    """
    Generates random numbers using 100 instances of the algorithm
    hash_func: One of the hash functions in the hashlib module
    """

    hasher = hash_func(seed)
    current_string = hasher.hexdigest()
    numbers = []
    for _ in range(num_iters):
        for j, character in enumerate(current_string):
            if int(character,base=16) >= 10:
                continue
            numbers.append(int(character, base=16))
        hasher = hash_func(current_string.encode())
        current_string = hasher.hexdigest()
    return numbers