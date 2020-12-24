class Solution(object):

  def evalRPN(tokens):
      stack = []

      # if not operators 
          # stack.append()
      #if operators 
          # stack.pop 
          # stack.pop
          # what kind of an operator. do process + - / *
        
      for char in tokens:

          if char not in "+-/*":
              stack.append(int(char))
              continue

          operant2 = stack.pop()
          operant1 = stack.pop()

          result = 0
          if char == "+":
              result = operant1 + operant2
          elif char == "*":
              result = operant1 * operant2
          elif char == "/":
              result = int(operant1 / operant2)
          elif char == "-":
              result = operant1 - operant2
          stack.append(result)

      return result


# tokens = ["2", "1", "+", "3", "*"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(Solution.evalRPN(tokens))
        