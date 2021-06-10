require './client_2'
require 'json'

class Main2
  # This is the entrypoint of the application

  # token: "c10917b75eab44f38fa617b809733ee4"
  # 
  class Company
    
    def initialize()
      
    end
  end

  class Employee

    attr_accessor :user_id, :id, :title, :body
    def initialize(user_id, id, title, body)
      @user_id = user_id 
      @id = id
      @title = title
      @body = body
    end


  end

  def self.run
    client = Client2.new(token: "c10917b75eab44f38fa617b809733ee4")
    @store_map = {}
    @update_count = 0

    data = ""
    data = client.run
    begin
      data = JSON.parse(data)
    rescue JSON::ParserError => pe
      puts "JSON Parse Error #{pe.message}"
    rescue StandardError => se
      puts "StandardError Error #{se.message}"
    end

    result = []
    data.each do |item|
      if item['userId'] == 1
        result << Employee.new(item['userId'], item['id'], item['title'], item['body'])
      end
    end

    puts "result : #{result}"

    # 3.times do
    #   data = ""
    #   data << client.run
    #   begin
    #     data = JSON.parse(data)
    #   rescue JSON::ParserError => err
    #     puts "Err : #{err.to_json}"
    #   end

    #   data['data'].each do |up_item|
    #     up_item.each do |item|
    #       name = item['name']
    #       income_data = item['income_data']
    #       empl = Employee.new(name, income_data)
    #       unless @store_map.include? empl.name
    #         @store_map[name] = empl
    #       else
    #         check_and_update(name, income_data)
    #       end
    #     end
    #   end
    # end
    # puts " @store_map.length : #{@store_map.length}"
    print_json()
  end

  def self.check_and_update(name, new_income_data)
    old_obj = @store_map[name]
    old_obj.income_data.each do |old_income|
      new_income_data.each do |new_income|
        if old_income['month'] == new_income['month'] && old_income['income'] != new_income['income']
          puts "We updated Employee name : #{old_obj.name}  from : #{old_income['income']} /  to : #{new_income['income']}"
          old_income['income'] = new_income['income']
          @update_count += 1
        end
      end
    end
  end

  def self.print_json()
    # [
    #   {
    #     name : Casey Kemmer,
    #     income: [
      #       {Jan : 1234},
      #       {Feb : 1234}
    #     
    #   }
    # ]
    res = []
    @store_map.each do |k,v|
      temp = {}
      temp[:name] = k
      obj_arr = []
      v.income_data.each do |inc|
        obj = {}
        obj[inc['month']] = inc['income']
        obj_arr << obj
      end
      temp[:income] = obj_arr
      res << temp
    end
    puts "res : #{res}"
    puts "There are #{res.length} employees. We have #{@update_count} update income info."
  end

end

Main2.run