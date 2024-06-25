
def printInc(n):

    # base
    if n==0:
        return;

    # recurrsive work
    printInc(n-1)

    # my work
    print(n)

if __name__ == '__main__':
    printInc(5)