import List
words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k = 4
class Solution:
    def topKFrequent(words , k) -> List[str]:

        fre = {}
        res = []
        for word in words:
            fre[word] = fre.get(word,0)+1
        
        # sorted(fre.values(), key= lambda x:x[1])
        fre = dict(sorted(fre.items(), key=lambda item: (item[1], item[0]))) # lexicographical order sorted
        fre = dict(sorted(fre.items(), key=lambda item: item[1],reverse=True)) #sorted according frequency

        i = 0
        for value in fre:
            if i == k:
                break
            res.append(value)  
            i +=1 
            
        return res    