"""
In-Class Markov Chain Exercise
2.10.15
@author: jembrown
"""

"""
Recall from your reading that any irreducible and aperiodic Markov chain has a 
stationary distribution. To convince ourselves that things will converge for 
such a chain with arbitrary transition probabilities, let's give it a try.

Work in pairs for this. It's more fun to be social.
"""

# Paste your Markov chain simulation function below, where the starting state
# is drawn with uniform probability from all possible states. Remember to also
# copy any import statements or other functions on which your simulator is
# dependent.


# Define a 2x2 transition matrix. For fun, don't make all the probabilities
# equal. Also, don't use any 0s or 1s (to make sure the chain is irreducible
# and aperiodic).




# Simulate a single chain for three time steps and print the states




# Analytically calculate the progression of states for this chain.




# Calculate the probability of observing the state in step 3, given the initial
# state in step 1 (i.e., as if you didn't know the state in step 2).





# Now think of the chain progressing in the opposite direction. What is the
# probability of the progression through all 3 states in this direction? How
# does this compare to the original direction?






# Try the same "forward" and "reverse" calculations as above, but with this
# transition matrix:
# revMat = [[0.77,0.23],
#           [0.39,0.61]]
# and these starting frequencies for "a" and "b"
# freq(a) = 0.63   freq(b) = 0.37




# What is (roughly) true about these probabilities?





# Simulate 1,000 replicates  (or 10K if your computer is fast enough) of 25 
# steps. What are the frequencies of the 2 states across replicates through time?

# NOTE: Here is a function that reports the frequencies of a state through time 
# for replicate simulations. You'll need to do this several times during this exercise.

def mcStateFreqSum(sims,state="a"):
    """
    Pass this function a list of lists. Each individual list should be the
    states of a discrete-state Markov chain through time (and all the same 
    length). It will return a list containing the frequency of one state 
    ("a" by default) across all simulations through time.
    """
    freqs = []
    for i in range(len(sims[0])):  # Iterate across time steps
        stateCount = 0
        for j in range(len(sims)): # Iterate across simulations
            if sims[j][i] == state:
                stateCount += 1
        freqs.extend([float(stateCount)/float(len(sims))])
    return freqs

# Run replicate simulations 



    
# Summarize the frequency of one state through time




# What do you notice about the state frequencies through time? Try another round
# of simulations with a different transition matrix. How do the state freq.
# values change?






# Now, calculate a vector of probabilities for the focal state (e.g., 'a')
# based on the transition matrix directly (not by simulation). How do these
# values compare to the simulated frequencies?










