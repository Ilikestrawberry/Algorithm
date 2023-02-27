def solution(board):
    o_cnt = 0
    x_cnt = 0
    o_flag = False
    x_flag = False
    for line in board:
        o_line = line.count('O')
        x_line = line.count('X')
        o_cnt += o_line
        x_cnt += x_line
        # 가로 체크
        if o_line == 3:
            o_flag = True
        if x_line == 3:
            x_flag = True
    # 세로 체크
    for idx in range(3):
        if board[0][idx] == board[1][idx] == board[2][idx] == 'O':
            o_flag = True
        elif board[0][idx] == board[1][idx] == board[2][idx] == 'X':
            x_flag = True
    # 대각선 체크
    if board[0][0] == board[1][1] == board[2][2] == 'O' or board[0][2] == board[1][1] == board[2][0] == 'O':
        o_flag = True
    elif board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][2] == board[1][1] == board[2][0] == 'X':
        x_flag = True
    
    if o_cnt < x_cnt:
        return 0
    if o_cnt > x_cnt + 1:
        return 0
    if o_flag == x_flag == True:
        return 0
    if o_flag == True and o_cnt != (x_cnt + 1):
        return 0
    if x_flag == True and o_cnt != x_cnt:
        return 0
    
    return 1