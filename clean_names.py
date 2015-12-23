with open("corrected6.txt", "wt") as fout:
    with open("corrected5.txt", "rt") as fin:
        for line in fin:
            fout.write(line.replace('g + +', 'g++'))

