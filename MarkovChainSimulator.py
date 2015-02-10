import scipy as sp     

def discSamp(events,probs):
    """
    This function samples from a list of discrete events provided in the events
    argument, using the event probabilities provided in the probs argument. 
    These lists must:
        - Be the same length
        - Be in corresponding orders
    Also, the probabilities in probs must sum to 1.
    """
    ranNum = sp.random.random()
    cumulProbs = []
    cumulProbs.extend([probs[0]])
    for i in range(1,len(probs)):
        cumulProbs.extend([probs[i]+cumulProbs[-1]])
    for i in range(0,len(probs)):
        if ranNum < cumulProbs[i]:
           return events[i]
    return None

def dmcSim(n,st=("a","b"),allProbs=[[0.5,0.5],[0.5,0.5]]):
    """
    This function simulates the progression of a discrete-time, discrete-state
    Markov chain. It takes 3 arguments: (1) The number of steps (n), (2) the 
    state space, and (3) the transition matrix. It returns a list containing 
    the progression of states through time. This list should have length n.
    
    The chain will be initiated with a randomly drawn state.
    """
    
    # Define list to hold chain's states
    chain = []    

    # Draw a state to initiate the chain
    currState = discSamp(st,[1.0/len(st) for x in st])
    chain.extend(currState)

    # Simulate the chain over n-1 steps following the initial state
    for step in range(1,n):
        probs = allProbs[st.index(currState)] # Grabbing row associated with currState
        currState = discSamp(st,probs) # Sample new state
        chain.extend(currState)        
        
    return chain

