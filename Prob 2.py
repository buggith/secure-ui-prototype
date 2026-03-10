#At a carnival, there are N game tokens.
#Each token has a unique lucky number printed on it.
#The carnival organizer needs to sort these tokens into two boxes:
# one for tokens with lucky numbers having magical properties (divisible by 2)
#and another for tokens with mystical properties (not divisible by 2).
#Help count how many tokens belong in each box.

def count_tokens(uniqueNo):
	magical = 0
	mystical = 0
	if (uniqueNo) %2 == 0:
		magical += 1
	else:
		mystical +=1
	return count_tokens(uniqueNo)

