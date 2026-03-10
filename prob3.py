#A classroom has N students, each having a different score. 
# The teacher wants to form pairs for a group project with the following rules:
#Every student must be in exactly one pair
#Score difference between students in a pair must not exceed K
#Find if it's possible to pair all students following these rules

def pair(scores, K):
    scores.sort()   #sort the scores in ascending order to pair easily
    n = len(scores)
    if n % 2 != 0: #check if number of students is odd
        return False
    
    for i in range(0, n, 2):
        if scores[i + 1] - scores[i] > K:
            return False
            
    return True
