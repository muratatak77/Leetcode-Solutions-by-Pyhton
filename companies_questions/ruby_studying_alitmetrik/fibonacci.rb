require 'test/unit'
# 
# Fn = Fn-1 +  Fn-2
# 
# F0 = 0 and F1 = 1, F2 = 1
# 
def fib(n)
	if n < 0
		print("Incorrect Input")
		raise "Can not be negative number"
	elsif n == 1
		return 0
	elsif n == 2
		return 1
	else
		return fib(n-1) + fib(n-2)
	end
end

res = fib(4)
print("res : ", res)
puts ""


class TestFibonacci < Test::Unit::TestCase

	def test_number_1_should_be_0
		assert_equal(fib(1), 0)
		assert_not_nil(fib(1))
		assert_kind_of(Integer, fib(1))
	end

	def test_number_2_should_be_1
		assert_equal(fib(2), 1, "2 Fib Should be 1")
	end

	def test_number_negative_number
		assert_raises "Can not be negative number" do
			fib(-1)			
		end
	end

	def test_number_4_should_be_24
		assert_equal(fib(4), 2, "4 fib should be 2")
	end
end