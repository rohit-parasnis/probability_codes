import itertools
import random

import matplotlib.pyplot as plt
import numpy as np

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets


# Range of number of people
PEOPLE = np.arange(1, 26)

# Days in year
DAYS = 365


def prob_unique_birthdays(num_people):
    '''
    Returns the probability that all birthdays are unique, among a given
    number of people with uniformly-distributed birthdays.
    '''
    return (np.arange(DAYS, DAYS - num_people, -1) / DAYS).prod()


def sample_unique_birthdays(num_people):
    '''
    Selects a sample of people with uniformly-distributed birthdays, and
    returns True if all birthdays are unique (or False otherwise).
    '''
    bdays = np.random.randint(0, DAYS, size=num_people)
    unique_bdays = np.unique(bdays)
    return len(bdays) == len(unique_bdays)


def plot_probs(iterations):
    '''
    Plots a comparison of the probability of a group of people all having
    unique birthdays, between the theoretical and empirical probabilities.
    '''
    sample_prob = []  # Empirical prob. of unique-birthday sample 
    prob = []         # Theoretical prob. of unique-birthday sample
    
    # Compute data points to plot
    np.random.seed(1)
    for num_people in PEOPLE:
        unique_count = sum(sample_unique_birthdays(num_people)
                          for i in range(iterations))
        sample_prob.append(unique_count / iterations)
        prob.append(prob_unique_birthdays(num_people))
    
    # Plot results
    plt.plot(PEOPLE, prob, 'k-', label='Theoretical prob.')
    plt.plot(PEOPLE, sample_prob, 'bo-', label='Empirical prob.')
    plt.axhline(0.5, color='red', label='0.5 threshold')
    plt.xlabel('Number of people')
    plt.ylabel('Probability of unique birthdays')
    plt.grid()
    plt.xticks()
    plt.legend()
    plt.show()

    
interact(plot_probs,
         iterations=widgets.IntSlider(min=50, max=5050, step=200),
         continuous_update=False, layout='bottom');
