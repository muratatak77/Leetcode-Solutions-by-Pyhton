require 'net/http'

# THIS FILE SHOULD NOT BE CHANGED AND SHOULD BE USED 'AS IS'
class Client2
  # URL = 'https://flakey-api.crowdai.com/employees'
  URL = 'https://jsonplaceholder.typicode.com/posts'

  attr_reader :token

  # Creates an instance of the Client and sets the access token
  def initialize(token:)
    @token = token
  end

  # # Makes an HTTP GET request to the flakey server API
  # # with the provided access token
  # def run
  #   uri = URI("#{URL}?token=#{@token}")
  #   Net::HTTP.get(uri)
  # rescue StandardError => e
  #   raise "Failed to connect to server: #{e.message}"
  # end

  def run
    begin
      uri = URI("#{URL}?token=#{@token}")
      Net::HTTP.get(uri)  
    rescue StandartError => e
      raise "Failed to connect to server : #{e.message}"
    end
  end

  # def run 
  #   file_name = "data_#{rand(0..2)}.json"
  #   puts "WE ARE READING #{file_name}"
  #   return File.read(file_name)
  # end
end