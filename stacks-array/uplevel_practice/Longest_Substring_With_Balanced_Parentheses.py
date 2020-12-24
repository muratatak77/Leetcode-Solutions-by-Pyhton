# Complete the function below.

def find_max_length_of_matching_parentheses(brackets):
    #(()((())    
    #stack = "(", "(", ")" 
    
    if not brackets:
        return 0
    
    if len(brackets) < 1 or len(brackets) > 10000000:
        return 0

    stack = []
    count_in = 0
    max_elem = 0
    index_follow = 0
    for i in range(len(brackets)):
        # print("index : ", i)
        if brackets[i] == "(":
            stack.append("(")
            print("index_follow : ", i - index_follow)
            if not i - index_follow == 1:
                print("000000")
                count_in = 0

            print("stack : ", stack)
        elif brackets[i] == ")":
            print(stack)
            #we pop from stack , encounter prev one if stack not emptty
            if stack:
                top_element = stack.pop()
                count_in += 2
                print(count_in)
                max_elem = max(count_in, max_elem)
                print(max_elem)
                index_follow = i
    return max_elem

brackets = "((((())(((()"
# brackets = "()()()"
brackets = "()((()))()((()))"
print(find_max_length_of_matching_parentheses(brackets))