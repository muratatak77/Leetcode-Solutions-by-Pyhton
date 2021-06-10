
# Your previous Plain Text content is preserved below:
# 
# This is just a simple shared plaintext pad, with no execution capabilities.
# 
# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.
# 
# You can also change the default language your pads are created with
# in your account settings: https://app.coderpad.io/settings
# 
# Enjoy your interview!
# 
# ==============================================================================
# 
# Given a list of Card objects, find all the cards in the list that are duplicates.
# 
# Duplicates are defined as two cards with the same rank and color.
# 
# Cards are similar to, but not exactly like, common playing cards. 
# 
# 
# final class Card {
#     int rank;  // any integer
#     Color color; // RED, GREEN, BLUE, YELLOW, etc.
#     String cardId; // uniquely identifies a card object
# }
# 
# 
# List<Card> findDuplicates(List<Card> cards);
# 
# 
# Example:
# (Each card is listed as [rank, color, id])
# 
#    Input        ||   Output
# ==================================
#                 ||
# [5, YELLOW, aa] || [5, YELLOW, aa]
#                 ||
# [2, BLUE, bb]   || [2, BLUE, bb]
#                 ||
# [3, YELLOW, cc] || 
#                 ||
# [5, YELLOW, dd] || [5, YELLOW, dd]
#                 ||
# [3, GREEN, ee]  || 
#                 ||
# [2, BLUE, ff]   || [2, BLUE, ff]
#                 ||
# [5, YELLOW, gg] || [5, YELLOW, gg]
#                 ||


# [5, YELLOW, aa] || [5, YELLOW, aa]


def findDuplicate(cards):
    result = []
    hash_map = {}
    hash_map_repeating = {}

    for i in range(len(cards)):
        key = cards[i][0],cards[i][1]
        if key in hash_map:

            result.append(hash_map[key])
            hash_map[key] = cards[i]

            # result.append(hash_map[key])


        else:
            hash_map[key] = cards[i]
        

        print("                     hash_map : ", hash_map)
        print("                     hash_map_repeating : ", hash_map_repeating)
        print("======================================================")
        
        # result.append(hash_map[key] > 0)
        
    return result
    
# {[5,YELLOW]: [5, YELLOW, dd] }
# {[2,BLUE]: [2, BLUE, bb]}
# {[3,YELLOW]:  [3, YELLOW, cc]}

# def findDuplicate(cards):
#     result = []
    
#     for i in range(len(cards))
#         key = [cards[i].rank , cards[i].color]
#         if hash_map[key] > 0         
#             result.append(cards[i])
    
#     return result
            
input = [
[5, "YELLOW", "aa"],
[2, "BLUE", "bb"] , 
[3, "YELLOW", "cc"], 
[5, "YELLOW", "dd"], 
[3, "GREEN", "ee"], 
[2, "BLUE", "ff"], 
[5, "YELLOW", "gg"]]
res = findDuplicate(input)
print("res : ", res)
