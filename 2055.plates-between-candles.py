def platesBetweenCandles(s, queries):
        n = len(s)
        prefixSum = [0]*n
        prefixSum[0] = 1 if s[0] == '*' else 0
        left_candle = [-1]*n
        left_candle[0] = 0 if s[0] == '|' else -1

        for i in range(1, n):
            if s[i]=='*':
                prefixSum[i] = prefixSum[i-1] + 1
                left_candle[i] = left_candle[i-1]
            else:
                prefixSum[i] = prefixSum[i-1]
                left_candle[i] = i


        right_candle = [-1]*n
        right_candle[n-1] = n-1 if s[n-1] == "|" else -1
        for i in range(n-2, -1, -1):
            if s[i] == '*':
                right_candle[i] = right_candle[i+1]
            else:
                right_candle[i] = i

        result = []
        for l,r in queries:
            startCandle = right_candle[l]
            endCandle = left_candle[r]
            # onyl add res when start<end
            if startCandle < endCandle:
                result.append(prefixSum[endCandle] - prefixSum[startCandle])
            else:
                result.append(0)
        print(result)

platesBetweenCandles("||*",[[2,2]])
