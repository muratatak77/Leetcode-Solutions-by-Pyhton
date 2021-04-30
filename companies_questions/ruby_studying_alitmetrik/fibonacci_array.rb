# 
# Fn = Fn-1 +  Fn-2
# 
# F0 = 0 and F1 = 1, F2 = 1
# 

@result = [0,1]
def fib_array(n)
	print(" n : ", n)
	puts ""
	if n <= @result.size
		print("n : ", n, " - result : " , @result)
		puts ""
		return @result[n-1]
	else
		temp =  fib_array(n-1) + fib_array(n-2)
		print("		temp : ", temp)
		puts ""
		@result << temp
		return temp
	end
end



res = fib_array(4)
print("res array : ", @result)
puts ""