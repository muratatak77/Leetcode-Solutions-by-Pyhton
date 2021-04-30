require 'test/unit'

class Matrix
	attr_accessor :data
	
	def initialize(content)
	  @data = generate(content)
	  # puts " DATA generated content : #{content}"
	end

	def get_value(point)
		@data[point.x][point.y]
	end

	private

	def generate(content)
    res = []
    content[1..-1].each do |line|
      res.append(line.strip.chars)
    end
    res
  end

end

class Point
	attr_accessor :x, :y
	def initialize(x, y)
		@x = x
		@y = y
	end
end

class FileConvertMatrix < StandardError

  attr_accessor :content, :x, :y, :path, :point, :matrix

  def initialize(path)
    raise if path.nil? or path.empty?
    @path = path
    @content = ""
    @x = ""
    @y = ""
  end

  def read_file
    file = File.open(@path)
    @content = file.readlines.map(&:chomp)
  end

  def set_x_y
    data = @content[0]
    find_char_count = 0
    data.each_char { |chr|
      if chr != " " && chr.to_i != 0
        @x = chr.to_i if find_char_count == 0
        if find_char_count == 1
          @y = chr.to_i
          break
        end
        find_char_count += 1
      end
    }
  end

  def set_matrix
    @matrix = Matrix.new(@content)
    # print("matrix  ; ", @matrix.inspect)
  end

  def set_point
    @point = Point.new(x,y)
    # puts " Point : #{@point.inspect}"
  end

  def get_char_by_points(x,y)  	
  	raise FileConvertMatrix, "X or Y can not be negative." if x < 0 or y < 0
  	@matrix.get_value(x,y)
  end

end


class FileConvertMatrixTest

end

class HelloTest<Test::Unit::TestCase

  # you can use the class variables @@
  @@cmptr = nil
  def setup
    if @@cmptr.nil?
      @@cmptr = 0
      @fs = FileConvertMatrix.new("file1.txt")
      puts "FS : #{@fs.inspect}"
      @fs.read_file
      @fs.set_x_y
      @fs.set_matrix
      @fs.set_point
      @@fs = @fs
    end
  end


  # def setup
  # 	puts "runs before each test"
  # end

  # def teardown
  # 	puts "runs after each test"
  # end

  # def test_successful_world
  # 	assert Hello.world == "helloworld", "You got this"
  # end

  # def test_fail
  # 	assert(false, "Assertion was false.")
  # end
  #

  def test_file_stream_not_nil
    assert_not_nil(@@fs.content)
    # assert_kind_of Array, @@fs.content
  end

  def test_file_stream_should_be_arr
    assert_kind_of Array, @@fs.content
  end

  def test_file_should_x_2
    assert_equal(2, @@fs.x)
  end

  def test_file_should_y_4
    assert_equal(4, @@fs.y, "it didn't pass.")
  end

  def test_point_should_be_W
    assert_equal("W", @@fs.matrix.get_value(@@fs.point))
  end

  def test_x_should_be_grater_than_0
    assert_compare(@@fs.x, ">", 0)
  end

  def test_point_should_not_empty
    assert_not_nil(@@fs.point)
  end

  def test_raise_nil_path
    assert_raise( RuntimeError ) { FileConvertMatrix.new(nil)}
  end

  def test_point_should_include_O
    assert_include(@@fs.matrix.get_value(@@fs.point), "W" )
  end

  def test_send_variable
  	assert_send([@@fs.matrix.data[0], :member?, "A"]) # -> pass
  end

	def test_negative_x_y
  	assert_raises FileConvertMatrix do
    	@@fs.get_char_by_points(-1,-3)
 		end
	end

	def test_points_value_should_be_string
		assert_instance_of String, @@fs.matrix.get_value(@@fs.point)
	end

	def test_point_key_should_be_string
		assert_instance_of Integer, @@fs.x
	end

	def test_path_exists
		assert(File.exist?(@@fs.path))
	end

	def test_kind_of_matrix_point
		 assert_kind_of Matrix, @@fs.matrix
		 assert_kind_of Point, @@fs.point
	end

end
