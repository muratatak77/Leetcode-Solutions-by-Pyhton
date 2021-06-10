#
# Rate Limiter (for API requests)
#
# def accept_request(String ip, float timestamp)
#   Exceeds: Return false
#   Does not exceed: Return true
#
# Assumptions:
#  - Hardcode rate limit to 5 per second
#  - Every request coming in will be in chronological order
#  - The timestamp being passed is the current time
#  - Failures will count towards the rate
#
# ----> time ---->
#
# -- 1 second--|
#
#        --- 1 second --|
#      ------ 1 sec-|
#|T  T   T T T F    T  F|
#
# accept_request("127.0.0.1", 0.0) = true
# accept_request("127.0.0.1", 0.1) = true

# accept_request("127.0.0.1", 0.2) = true
# accept_request("127.0.0.1", 0.3) = true
# accept_request("127.0.0.1", 0.4) = true

# accept_request("127.0.0.1", 0.5) = false  - global_rate = 6 false

# accept_request("127.0.0.1", 1.15) = true
# accept_request("127.0.0.1", 1.16) = false
# accept_request("127.0.0.1", 1.17) = false
# accept_request("127.0.0.1", 1.18) = false
# 
# hash_map = {ts, count} 0 : T ,  1 : F

# 01 : 0.00 T  
# 02 : 0.10 T   
# 03 : 0.20 T L
# 04 : 0.30 T 
# 05 : 0.40 T L
# 06 : 0.41 F 
# 07 : 0.42 F 
# 08 : 0.43 F
# 09 : 0.44 F
# 10 : 1.44 T R

rate_limit = 0
hash_map = {}
def accept_request(ip_address, timestamp):
    
    
        
    return True


print(accept_request("127.0.0.1", 0.0) == True)
print(accept_request("127.0.0.1", 0.1) == True)
# --> 0.16 -->
print(accept_request("127.0.0.1", 0.2) == True)
print(accept_request("127.0.0.1", 0.3) == True)
print(accept_request("127.0.0.1", 0.4) == True)
print(accept_request("127.0.0.1", 0.5) == False)
print(accept_request("127.0.0.1", 1.15) == True)  # 5 @ this time
print(accept_request("127.0.0.1", 1.16) == False) # 6 @ this time
# <-- 1.16 <--
# [0.16, 1.16] (viewing 1 second in the past)

print(accept_request("127.0.0.1", 1.17) == False) # 7 @ this time
print(accept_request("127.0.0.1", 1.18) == False) # 8 @ this time
print(accept_request("127.0.0.2", 1.19) == True)
