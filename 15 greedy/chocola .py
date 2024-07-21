def chocola(hCost,vCost):
    hCost = sorted(hCost,reverse=True)
    vCost = sorted(vCost,reverse=True)
    
    hPointer , vPointer = 0, 0
    hpiece, vpiece = 1, 1
    Cost = 0
    
    while hPointer < len(hCost) and vPointer < len(vCost):
        
        if hCost[hPointer] <= vCost[vPointer]:
            Cost += (vCost[vPointer] * hpiece)
            vpiece += 1
            vPointer += 1
        else:
            Cost += (hCost[hPointer] * vpiece)
            hpiece += 1
            hPointer += 1
            
    while hPointer < len(hCost):
        Cost += (hCost[hPointer] * vpiece)
        hpiece += 1
        hPointer += 1
        
    while vPointer < len(vCost):
            Cost += (vCost[vPointer] * hpiece)
            vpiece += 1
            vPointer += 1
            
    print(f'Minium cost : {Cost}')        
                 
 
    
hCost = [4,1,2]
vCost = [2,1,3,1,4]

chocola(hCost,vCost)