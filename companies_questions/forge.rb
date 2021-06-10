# Let's code Tic-Tac-Toe!
# The program should be an interactive command line program that prompts both players for their moves.
# After each player's move, the board should be displayed so that the next player can see what the state of the board is.

# X X 0
# 0 X X
# X 0 0

# The program should be able to stop if any of the game's rules are met.
# Bonus: can you allow the player to specify the size of the board? (otherwise than the standard 3x3)
# Bonus: can you implement the board check in constant time?
# Bonus: can you write an automated test suite?
# Bonus: implement a simple 1-player vs computer version (feel free to come up with any algorithm for doing so)

# Focus on correctness and clean coding. Feel free to use any programming paradigms you see fit -- object oriented programming, functional programming, CQRS, etc

# input = gets
# puts input

class TicTacTao

    def initialize(n)
        @board = Array.new(n)
        @n = n
        @n.times do |row_index|
            @board[row_index] = Array.new(@n)
            @n.times do |column_index|
                @board[row_index][column_index] = ""
            end
        end
    end
    
    def move
        puts "Player move row, col, mark"
        data = gets
        row, col, mark = data.split(" ")
        
        row = row.to_i
        col = col.to_i
        mark = mark.to_s
        
        @board[row][col] = mark
        
        puts "@board : #{@board}"
        
        if check_row(row, mark)
            if check_column(col, mark)
                if check_diagonal(mark)
                    return mark
                end
            end
        end
        #no wins
        0
    end
    
    def check_row(row, mark)
        for col in (0..@n-1)
           if @board[row][col] != mark
                return false
           end
        end
        true
    end
    

    def check_column(col, mark)
        for row in (0..@n-1)
           if @board[row][col] != mark
                puts "check_column false : #{col} - Mark : #{mark}"
                return false
           end
        end
        true
    end
    
    def check_diagonal(mark)
        for row in (0..@n-1)
           if @board[row][@n - row - 1] != mark
                puts "check_diagonal false : Mark : #{mark}"
                return false
           end
        end
        true
    end
    
end


tct = TicTacTao.new(3)

9.times do |call|
    tct.move
end