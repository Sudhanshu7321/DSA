def rankTeams(votes):
    voteCount = {}
    
    if len(votes) == 1:
        return votes[0]
    
    for vote in votes:
        for i in range(len(vote)):
            if vote[i] not in votes:
                voteCount[vote[i]] = []
            voteCount[vote[i]].append(i)
            
    for d in voteCount:
        voteCount[d] = sum(voteCount[d])    
    
    return ''.join(sorted(voteCount, key= lambda x:voteCount[x]))   
votes =["WXYZ","XYZW"]
print(rankTeams(votes))  
                
    