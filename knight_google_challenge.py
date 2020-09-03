def solution(src, dest):

    #if the start and destination are the same, return 0
    if src == dest: return 0

    #Representation of current game board
    board = [
        [0,1,2,3,4,5,6,7],
        [8,9,10,11,12,13,14,15],
        [16,17,18,19,20,21,22,23],
        [24,25,26,27,28,29,30,31],
        [32,33,34,35,36,37,38,39],
        [40,41,42,43,44,45,46,47],
        [48,49,50,51,52,53,54,55],
        [56,57,58,59,60,61,62,63]
    ]

    #locates the starting number's coordinates on the board
    for row in board:
        if src in row:
            x = board.index(row)
            y = row.index(src)

    #all possible moves by a knight
    possible_moves = [
        #down 2 right 1
        [2, 1],
        #down 2 left 1
        [2, -1],
        #up 2 left 1
        [-2, -1],
        #up 2 right 1
        [-2, 1],
        #left 2 up 1
        [-1, -2],
        #left 2 down 1
        [1, -2],
        #right 2 up 1
        [-1, 2],
        #right 2 down 1
        [1, 2]
    ]

    #function for checking possible moves around a number
    def check_coordinates(x, y):

        #log all coorninates for numbers checked
        coordinates_checked = []

        #check every available move from starting number
        for each_move in possible_moves:
            #if move is on the board
            if (x + each_move[0] >= 0 and x + each_move[0] <= 7 and y + each_move[1] >= 0 and y + each_move[1] <= 7):
                #check if move lands on target number
                if board[x + each_move[0]][y + each_move[1]] == dest: 
                    return "hit"
                #if not, add the coorinates to a list of checked moves
                else:
                    coordinates_checked.append([x + each_move[0], y + each_move[1]])
        
        #once all coordinates have been checked, return list of moves
        return coordinates_checked

    #log of the number of rounds
    number_of_rounds_started = ['1']

    #log of all numbers checked
    all_numbers_checked = [[x, y]]

    #function for queueing jobs
    def job_handler(list_of_numbers = [[x, y]]):

        #tracks the number of jobs completed this round
        number_of_numbers_checked = 0

        #numbers to check until next job
        numbers_for_this_round = len(list_of_numbers)

        #next job list
        new_list_of_numbers = []

        #itterates though current job list
        for number in list_of_numbers:

            #checks possible moves around each number
            numbers_checked = check_coordinates(number[0], number[1])

            #if the target number is in possible moves, return finish
            if (numbers_checked == "hit"): 
                return len(number_of_rounds_started)

            else:
                #itterate though resulting list of numbers checked
                for number in numbers_checked:
                    # if number not already in list add to list
                    if (number not in all_numbers_checked):
                        all_numbers_checked.append(number)
                        new_list_of_numbers.append(number)
                #and add completed job
                number_of_numbers_checked += 1

            #if all numbers have been checked, start a new job with all checked numbers
            if (number_of_numbers_checked == numbers_for_this_round):
                #print("numbers_for_this_round = ", numbers_for_this_round)
                #print("new_list_of_numbers = ", new_list_of_numbers)

                #log another round started
                number_of_rounds_started.append('1')
                
                #restart process with the new numbers
                return job_handler(new_list_of_numbers)

    #initiate the job handler
    return job_handler()


print(solution(0, 0))