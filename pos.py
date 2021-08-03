def lol9(intervals):    
        
    intervals.sort()
    ans = [intervals[0]]
    x = len(intervals)
    

    for i in range(1,x):
        

        if ans[-1][0] <= intervals[i][0] <= ans[-1][1] <= intervals[i][1] :

            ans[-1]=[ans[-1][0],intervals[i][1]]
            print(str(ans)+"  one  "+ str(i) )
            continue


        
        if ans[-1][0] <= intervals[i][0] <= intervals[i][1] <= ans[-1][1] :

            ans[-1]=[ans[-1][0],ans[-1][1]]
            print(str(ans)+"  two  "+ str(i) )
            continue


        if intervals[i][0] <=  ans[-1][0] <= intervals[i][1] <= ans[-1][1] :

            ans[-1]=[intervals[i][0],ans[-1][1]]
            print(str(ans)+"  three  "+ str(i) )
            continue


        if intervals[i][0] <=  ans[-1][0] <= ans[-1][1] <= intervals[i][1] :

            ans[-1]=[intervals[i][0],intervals[i][1]]
            print(str(ans)+"  four  "+ str(i) )
            continue
        
        
        
        if ans[-1][0] <=  ans[-1][1] == intervals[i][0] <= intervals[i][1] :
        
            ans[-1]=[ans[-1][0],intervals[i][1]]
            print(str(ans)+"  five  "+ str(i) )

            continue
        
        
        else:
            ans += [intervals[i]]



     
    return ans




print(lol9([[1,4],[4,5]]))