#In a secret communication system, two messages are considered equivalent if they can be rearranged to form each other.
#  Given two encrypted messages, determine if they represent the same secret message. 
#The comparison should be case-insensitive, and any spaces or special characters should be ignored.

def are_equivalent(msg1, msg2):
    # Normalize messages by removing spaces and special characters, and converting to lowercase
    normalized_msg1 = ''.join(filter(str.isalnum, msg1)).lower() #alphanumeric check to ignore special characters and spaces    
    normalized_msg2 = ''.join(filter(str.isalnum, msg2)).lower()
    
    # Sort the characters in both messages and compare
    return sorted(normalized_msg1) == sorted(normalized_msg2)

# Example usage:
message1 = "Listen!"                
message2 = "Silent"
print(are_equivalent(message1, message2))  # Output: True   
message3 = "Hello, World!"
message4 = "World Hello"
print(are_equivalent(message3, message4))  # Output: True