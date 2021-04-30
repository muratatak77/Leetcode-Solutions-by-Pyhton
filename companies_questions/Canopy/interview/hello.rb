require "test/unit"

class Hello
  def self.world
		"helloworld"
  end

  def initialize(nums)
    @nums = nums
  end

  def get_length
    @nums.length
  end

  def rand_lower_bound
    @nums[1]
  end

  def rand_upper_bound
    @nums[2]
  end

  def output
    len = get_length
    lower = rand_lower_bound
    upper = rand_upper_bound
    arr = []
    arr << lower    
    2.times do
      arr << random(lower..upper)
    end
    arr
    #4 , 6 
    #4,5,6
    #4,4,4
    #4,6,5
    #
  end

end

class HelloTest < Test::Unit::TestCase

	def setup
    @hello = Hello.new([3,4,6])
    # @hello = Hello.new([4,4,4,6])
  end

  def teardown
  end

  def test_successful_world
    assert Hello.world == "helloworld", "You got this!"
  end

  def test_length
    #[10, 1,3,4,5,8,9,3,5,7]
    assert_equal(@hello.get_length, 3)
  end

  def test_rand_lower_bound
    assert_equal(@hello.rand_lower_bound, 4)
  end

  def test_rand_upper_bound
    assert_equal(@hello.rand_upper_bound, 6)
  end
end