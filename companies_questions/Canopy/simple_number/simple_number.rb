require 'test/unit'

class SimpleNumber < StandardError
	
	def initialize(num) 
		raise unless num.is_a?(Numeric)
		@x = num
	end

	def add(y)
		raise SimpleNumber, "Y can not be negative number!" if y < 0
		@x + y
	end

	def multiply(y)
		@x * y
	end

end

class TestSimpleNumber < Test::Unit::TestCase

	def setup
		@num = SimpleNumber.new(2)
	end

	def teardown
		@num = nil
	end

	def test_simple
		assert_equal(4, @num.add(2))
		assert_equal(6, @num.multiply(3))
	end

	def test_typecheck
		assert_raise( RuntimeError ) {SimpleNumber.new('a')}
	end

	def test_failure
		assert_equal(3, @num.add(2),  "Adding doesn't work!")
	end

	# def test_negative
	# 	assert_raise( SimpleNumber ) {@num.add(-3)}
	# 	# assert_raises SimpleNumber  do
	# 		# @num.add(-1)
	# 	# end
	# end

	def test_negative_y
  		assert_raises RuntimeError do
    		@num.add(-3)
 		end
	end



end