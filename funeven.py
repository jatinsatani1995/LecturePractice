def evennumbers(inputlist):
    evennumbers = [num for num in inputlist if num % 2 == 0]
    print("Even Numbers:", evennumbers)


samplelist = [1, 2, 3, 4, 5, 6, 7, 8, 9]


evennumbers(samplelist)
