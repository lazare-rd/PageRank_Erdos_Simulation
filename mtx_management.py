def read_file(filename):
    with open(filename) as f:
        content = f.readlines()
    i = -1
    loop = True
    while loop :
        i+=1
        if content[i][0] != '%':
            loop = False
    N = clean_value(content[i])[0]
    content = content[i+1:]
    for i, x in enumerate(content) :
        content[i] = clean_value(x)
    return (content, N)

def clean_value(line):
    values = line.split()
    return [int(x) for x in values]

def build_matrix(data):
    P = []
    line_count = [0 for x in range(data[1])]
    curr_y = data[0][0][1]
    last_shift = 0
    for i, x_y in enumerate(data[0]) :
        line_count[x_y[0]-1] += 1
        if x_y[1] != curr_y:
            tempo = [x[0] for x in data[0][last_shift:i]]
            P.append((curr_y, tempo))
            curr_y = x_y[1]
            last_shift = i
    tempo = [x[0] for x in data[0][last_shift:i+1]]
    P.append((curr_y, tempo))
    return (P, line_count, data[1])