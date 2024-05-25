def solution(X, Y, D):
    # Implement your solution here
    if D == 0:
        return 0
    else:
        position = X
        count = 0
        while position < Y:
            position += D
            count += 1
        return count
