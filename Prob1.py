#In a music festival,
#N participants are playing different musical instruments. 
# For security reasons, participants need to be divided into groups based on their entry ID 
# numbers. 
# A participant with an ID number should be placed in 'Rock' band if their ID 
# is divisible by 3, 
# 'Jazz' band if divisible by 5, 
# and 'Pop' band if divisible by both 3 and 5. 
# All others go to 'Blues' band. Help the organizer count participants in each band.

def count_participants(Ids):
    rock = 0
    jazz = 0
    pop = 0
    blues = 0
    
    for Id in Ids:
        if Id % 3 == 0 and Id % 5 == 0:
            pop += 1
        elif Id % 3 == 0:
            rock += 1
        elif Id % 5 == 0:
            jazz += 1
        else:
            blues += 1
            
    return rock, jazz, pop, blues
