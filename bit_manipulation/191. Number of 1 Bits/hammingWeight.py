class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while(n):

            bit = n & 1
            print(" bit : ", bit)

            if(bit):
                count += 1

            n = n >> 1
            print(" 		n : ", n)
        
        return count


# public int hammingWeight(int n) {
#     int bits = 0;
#     int mask = 1;
#     for (int i = 0; i < 32; i++) {
#         if ((n & mask) != 0) {
#             bits++;
#         }
#         mask <<= 1;
#     }
#     return bits;
# }
# 
n = 11

res = Solution().hammingWeight(n)
print("res :", res)