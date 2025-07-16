def candy(self, ratings):
    # initilize
    n = len(ratings)
    i = 1
    sum = 1

    while i < n:
        # flat lands
        if ratings[i] == ratings[i-1]:
            sum += 1
            i += 1
            continue


        # increasing slope
        peak = 1
        while i < n and ratings[i] > ratings[i-1]:
            peak += 1
            sum += peak
            i += 1

        # decreasing slope
        foot = 1
        while i < n and ratings[i] < ratings[i-1]:
            sum += foot
            foot += 1
            i += 1

        # if foot number was more than peak, add the difference
        if foot > peak :
            sum += (foot - peak)

    return sum
