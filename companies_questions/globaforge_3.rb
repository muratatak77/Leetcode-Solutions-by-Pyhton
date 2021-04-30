require 'set'

def sudokuCheck(grid)

    #edge cases
    return false if grid.nil?
    
    #rows by rows checking 
    hset = Set.new([])
    for i in 0..8
        for j in 0..8
            if hset.include? grid[i][j]
                return false
            else
                hset.add(grid[i][j])
            end
        end
        # puts "hset : #{hset}"
        hset = Set.new([])
    end
            
    #cols by cols checking
    hset = Set.new([])
    for i in 0..8
        for j in 0..8
            if hset.include? grid[j][i]
                return false
            else
                hset.add(grid[j][i])
            end
        end

        hset = Set.new([])
    end
    
    
    #3 by 3 check
    # 0,0 0,1 0,2 | 0,3    0,5 | 0,6   0,8
    # 1,0 1,1 1,2 | 1,3    1,5
    # 2,0 2,1 2,2 | 2,3    2,5 |       2,8
    # 3,0
    
    subs = [[0,3], [3,6], [6,9]]
    subgrids = [] 

    subs.each do |x|
        subs.each do |y|
            subgrids << [x,y]
        end
    end

    # subgrids = [(x,y) for x in subs for y in subs]
    # print("subgrids : ", subgrids)
    puts "subgrids : #{subgrids}"
    subgrids.each do |row_range|
        subgrids.each do |column_range|
            hset = Set.new([])
            puts "row_range : #{row_range}"
            puts "column_range : #{column_range}"

            row_range.each do |row|
                column_range.each do |col|   

                    for i in row[0]..row[1]
                        for j in col[0]..col[1]
                            puts "i : #{i}"
                            puts "j : #{j}"
                            puts "hset : #{hset}"
                            puts "grid[i][j] : #{grid[i][j]}"
                            if hset.include? grid[i][j]
                                return false
                            else
                                hset.add(grid[j][i])
                            end
                        end

                    end
                end
            end
        end
    end

    return true

end
    # for (row_range, column_range) in subgrids:

    #     print("row_range : ", row_range)
    #     print("column_range : ", column_range)

    #     hset = set()
    #     for i in row_range:
    #         for j in column_range:              
    #             if grid[i][j] in hset:
    #                 return False
    #             else:
    #                 hset.add(grid[i][j])
    
    # return True
    

# grid = [
     
#      0  1  2   3  4  5   6  7  8

#  0   [8, 3, 5,  4, 1, 6,  9, 2, 7],

#  1   [2, 9, 6,  8, 5, 7,  4, 3, 1],

#  2   [4, 1, 7,  2, 9, 3,  6, 5, 8],



#  3   [5, 6, 9,  1, 3, 4,  7, 8, 2],

#  4   [1, 2, 3,  6, 7, 8,  5, 4, 9],

#  5   [7, 4, 8,  5, 2, 9,  1, 6, 3],



#  6   [6, 5, 2,  7, 8, 1,  3, 9, 4],

#  7   [9, 8, 1,  3, 4, 5,  2, 7, 6],

#  8   [3, 7, 4,  9, 6, 2,  8, 1, 5]

# ]


grid = [

[8, 3, 5,  4, 1, 6,  9, 2, 7],

[2, 9, 6,  8, 5, 7,  4, 3, 1],

[4, 1, 7,  2, 9, 3,  6, 5, 8],

[5, 6, 9,  1, 3, 4,  7, 8, 2],

[1, 2, 3,  6, 7, 8,  5, 4, 9],

[7, 4, 8,  5, 2, 9,  1, 6, 3],

[6, 5, 2,  7, 8, 1,  3, 9, 4],

[9, 8, 1,  3, 4, 5,  2, 7, 6],

[3, 7, 4,  9, 6, 2,  8, 1, 5]

]


res = sudokuCheck(grid)
print("res : ", res)
