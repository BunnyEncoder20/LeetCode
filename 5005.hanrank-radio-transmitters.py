'''
Hackerland is a one-dimensional city with houses aligned at integral locations along a road. The Mayor
wants to install radio transmitters on the roofs of the city's houses. Each transmitter has a fixed range
meaning it can transmit a signal to all houses within that number of units distance away.
Given a map of Hackerland and the transmission range, determine the minimum number of transmitters so that every house is within range of at least one transmitter. Each transmitter must be installed on top of an
existing house.
Example
x = |1,2, 3, 5, 9]
k = 1
3 antennae at houses 2 and 5 and 9 provide complete coverage. There is no house at location 7 to cover both 5 and 9. Ranges of coverage, are [1, 2, 3], [5], and [9].
'''

def hackerlandRadioTransmitters(x, k):
    x.sort()
    transmitters = 0
    i = 0 
    n = len(x)
    
    while i < n:
        # installing a new trans
        transmitters += 1
        
        rangeStart = x[i]
        while i < n and x[i] <= rangeStart+k:
            i += 1
        
        # place transmitter at last possible house
        transPosition = x[i-1]
        while i < n and x[i] <= transPosition+k:
            i += 1
            
    return transmitters
