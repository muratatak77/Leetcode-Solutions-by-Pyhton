
def solution(input)
    #we can use a hash map to keeping integer value and index.
    #when we use encounter same item we can start a loop and we can add global result until the first item in the hash map
    hash_map = {}
    n = input.length
    result = []
    for i in (0..n-1)
        if (hash_map.include? input[i]) and (input[i] != input[i-1])
            _start = hash_map[input[i]].to_i + 1 
            _end = i-1
            while (_start <= _end)
                result << input[_start]
                _start += 1
            end
        else
            hash_map[input[i]] = i
        end
    end
    result
end

input = []
input = [1,2,3,4,5,6,7,1]

res = solution(input)
print("res : ", res)


=begin
    T(N) = For loop O(N) , and while O(M) = O(N+M). Overall will be O(N)
    S(N) = I used a hash map means extra space. O(N) in the loop.
=end