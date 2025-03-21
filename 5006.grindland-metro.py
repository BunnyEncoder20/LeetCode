'''
The city of Gridland is represented as ann x m matrix where the rows are numbered from 1 to n and the columns are numbered from 1 to m.
Gridland has a network of train tracks that always run in straight horizontal lines along a row. In other words, the start and end points of a train track are (r, cl) and (r, c2), where r represents the row number, cl represents the starting column, and c2 represents the ending column of the train track.
The mayor of Gridland is surveying the city to determine the number of locations where lampposts can be placed. A lamppost can be placed in any cell that is not occupied by a train track.
Given a map of Gridland and its k train tracks, find and print the number of cells where the mayor can
place lampposts.
Note: A train track may overlap other train tracks within the same row.
'''

def gridlandMetro(n, m, k, track):
    # map the tracks
    mpp = {}
    for row,c1,c2 in track:
        if row not in mpp:
            mpp[row] = []
        mpp[row].append((c1,c2))
    
    # merge the overlapping intervls & count occuppied cells
    occupied = 0
    for row in mpp:
        intervals = sorted(mpp[row])
        merged = []
        start,end = intervals[0]
        for c1,c2 in intervals[1:]:
            # overlapping / side by side interval
            if c1 <= end+1:
                end = max(end, c2)
            else:
                merged.append((start,end))
                start,end = c1,c2
        # add last interval
        merged.append((start,end))
        
        # sum up covered cells
        occupied += sum(end-start+1 for start,end in merged)
    
    totalCells = n * m
    return totalCells - occupied