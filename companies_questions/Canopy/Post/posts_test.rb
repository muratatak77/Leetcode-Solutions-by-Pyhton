require 'test/unit'

class Post
	attr_accessor :title, :body
	def self.connection
		db = SQLite3::Database.open("database/development.db")
		r = yield db
		db.close
		return r
	end
end

class PostsTest < Test::Unit::TestCase
	title = 'testpost'
	body = 'testpost body'
	
	Post.create(title: title, body: body)

	post = Post.find(title)
	assert_equal(body, post.body, "expected post with title #{title} to have been created.")
end