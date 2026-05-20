class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sd = []
        bd = []
        hd = []
        for i in range(len(prices)) :
            if prices[-1] != prices[i] :
                if prices[i] >= prices[i+1] :
                    sd.append(prices[i])#replace this with actual sell and if nothing bought yet then nothing to sell

                else :
                    if prices[i-1] <= prices[i] <=prices[i+1]:
                        hd.append(prices[i])#just continue
                    else:
                        bd.append(prices[i])#buy 
        if prices[-2] < prices[-1] :
            sd.append(prices[-1])
        else:
            hd.append(prices[-1])
            
        print(sd, bd, hd)