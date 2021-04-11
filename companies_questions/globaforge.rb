def possibilities(word)
  
  morses = {
    '.' => "E",
    '-'=>'T',
    '..'=>'I',
    '.-'=>'A',
    '-.'=>'N',
    '--'=>'M',
    '...'=>'S',
    '..-'=>'U',
    '.-.'=>'R',
    '.--'=>'W',
    '-..'=>'D',
    '-.-'=>'K',
    '--.'=>'G',
    '---'=>'O'
  }
   

  if word.include?("?")
    
    values = []
    n = word.split('').length 
    print("n : ", n)
    puts("")

    if n == 1
      values = ['E', 'T']
    else
      chars = word.split('')
      print("chars :", chars)
      puts("")

      indexes = []
      chars.each.with_index do |char,index|
        next if char == "?"
        indexes << index
      end
      print("indexes : ", indexes)
      puts("")

      morses.keys.each do |morse|
 
        next unless morse.length == n
        print("morse : ", morse)
        puts("")

        valid = true
        indexes.each do |index|
          print("index : ", index)
          puts("")
          print("morse.split('')[index] : ", morse.split('')[index])
          puts("")
          puts("----------------------------")
          next if chars[index] == morse.split('')[index]
          valid = false
        end
        print("valid : ", valid)
        puts ""
        values << morses[morse] if valid
        print("values : ", values)
        puts""
      end
    end
    return values
  else
    return [morses["#{word}"]]
  end
   
  
end
      
s = "?."
res = possibilities(s)
print("res :", res)
    
  