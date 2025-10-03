import sys
sys.path.insert(0, "../") 
from _parameters import SEED
import numpy as np

# credit: https://stackoverflow.com/questions/36200913/generate-n-random-numbers-from-a-skew-normal-distribution-using-numpy
def randn_skew_fast(N, alpha=0.0, loc=0.0, scale=1.0):
    np.random.seed(SEED)
    sigma = alpha / np.sqrt(1.0 + alpha**2) 
    u0 = np.random.randn(N)
    v = np.random.randn(N)
    u1 = (sigma*u0 + np.sqrt(1.0 - sigma**2)*v) * scale
    u1[u0 < 0] *= -1
    u1 = u1 + loc
    return u1

def elo_expected_score(player_rating, opponent_rating, scale_factor):
    expected_score = 1 / (1 + pow(10, (opponent_rating - player_rating) / scale_factor))
    return expected_score

def delta_rating(score, expected_score, k_factor):
    delta_rating = k_factor * (score - expected_score)
    delta_rating = round(delta_rating)
    if (score == 1) and (delta_rating == 0):
        delta_rating = 1
    return delta_rating

