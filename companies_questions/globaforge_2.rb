  # we can use a stack to valid braces 
  # like we can add to the stack first "(" char , if next eelemen is ')' we can pop from stack. and we can contunie other braces.
  # is not same 
  # like in our staack : "(}" we can return false

def valid_braces(braces)
  
  if braces.nil?
    return false
  end
    
  open_list = ["(", "{", "["]
  close_list = [")", "}", "]"]
  
  stack = []
  chars = braces.chars
  chars.each do  |char|

    if open_list.include?(char)
      stack << char

      puts "Added new stack : #{stack}"

    elsif close_list.include?(char)

      pos = close_list.index(char)

      puts "  pos : #{pos}"
      puts "  stack : #{stack}"

      if (stack.length > 0) && (open_list[pos] == stack[stack.length-1])
        stack.pop()
      else
        return false
      end


    end
  end
  
  if stack.length == 0
    true
  else
   false
  end
  
end


braces = "()[)"
res = valid_braces(braces)
print("res : ", res)
puts""