
q  = Queue.new
q << 5


5.times do |i|
	q << i
	puts "#{i} produced"
end

# puts "producer : #{producer}"


5.times do |i|
	value = q.pop
	puts "consumed #{value}"
end

