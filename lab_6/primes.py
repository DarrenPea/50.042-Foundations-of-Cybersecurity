def square_multiply(a,x,n):
    y = 1
    exp = bin(x)[2:]
    for i in range(len(exp)):
        y = y**2 % n
        if exp[i] == "1":
            y = a*y % n
    return y

if __name__=="__main__":
    print("3**45 % 204324 =", square_multiply(3, 45, 204324))
    print("2**324 % 4328943 =", square_multiply(2, 324, 4328943))
