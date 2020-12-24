# Stack Solution
def find_max_length_of_matching_parentheses(brackets):

    # Indices of the opening parentheses will be pushed into the stack and popped back out
    # once the matching closing parenthesis found. The latest not-yet-closed '(' is always
    # at the top of the stack, that is where current substring with balanced parentheses begins.
    
    if not brackets:
    	return 0
    
    # if len(brackets) < 1 or len(brackets) > 10^5:
    	return 0


    stack = []

    # Starting index of the current substring with balanced parentheses when the stack is empty.
    valid_from = 0

    # The longest substring with balanced parentheses we found so far:
    max_length = 0

    for i, bracket in enumerate(brackets):
        if bracket == '(':
            stack.append(i)
        elif bracket == ")":
            if not stack:
                # We found a closing parenthesis with no matching opening one.
                # It means that the substring until and including current index DOES NOT have
                # balanced parentheses and we must "forget about" it until the end of the string.
                valid_from = i + 1
                print("2 - valid_from :", valid_from)
            else:
                # We found a closing parenthesis with a matching opening one.
                # It means that the substring ending at the current index i DOES have balanced parentheses.
                # Let us see if it is longer than max_length.
                stack.pop()
                print("after pop Stack : ", stack)
                print("valid_from :", valid_from)
                if stack:
                    substring_start = stack[-1]
                    print("we have stack substring_start: ", substring_start)
                else:
                    substring_start = valid_from - 1
                    print("if not substring_start: ", substring_start)

                substring_length = i - substring_start
                print("substring_length : ", substring_length)
                max_length = max(substring_length, max_length)
                print("max_length : ", max_length)
                print("====================== ================== ")

    return max_length


brackets = "((((())(((()"
# brackets = "()()()"
brackets = "()()()()()(((((()))(((())))((((())"
brackets = ")))()()"
print(find_max_length_of_matching_parentheses(brackets))