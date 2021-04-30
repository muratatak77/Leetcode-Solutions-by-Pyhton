require 'test/unit'
class Test1
  attr_accessor :len, :lower, :upper

  def initialize(len, lower, upper)
    @len = len
    @lower = lower
    @upper = upper
  end

  def output
    res = []
    @len.times do
      res << rand(@lower..@upper)
    end
    res
  end

end

class Test1Test < Test::Unit::TestCase

    def test_output
      t = Test1.new(3,4,6)
      t.output.each do |item|
        assert item >= t.lower
        assert item <= t.upper
      end
    end

end