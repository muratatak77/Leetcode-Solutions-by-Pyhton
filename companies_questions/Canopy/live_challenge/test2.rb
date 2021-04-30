require 'test/unit'

class Combination
  attr_accessor :str
  def initialize(str)
    @str = str.downcase
  end

  def output
    @ans = []
    
    def helper(i, slate)
      puts "slate : #{slate}"
      if i == @str.length
        @ans << slate
      else
        helper(i+1, slate+@str[i].downcase)
        helper(i+1, slate+@str[i].upcase)
      end
    end

    helper(0,"")
    return @ans
  end

end


c  = Combination.new("ab")
res = c.output
puts "res : #{res}"
