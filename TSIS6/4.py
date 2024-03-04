with open(r"einstein.txt", 'r') as fp:
	lines = len(fp.readlines())
	print('Total Number of lines:', lines)


def count_lines(filename):
    try:
        with open(filename, 'r') as file: # read until point or dot
            line_count = 0
            for line in file:
                #print(line)
                line_count += 1
        return line_count
    except FileNotFoundError:
        print("File not found.")


filename = 'einstein.txt' 
lines = count_lines(filename)
print("Number of lines in the file:", lines)
