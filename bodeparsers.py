
def spice_parser(filepath):
    with open(filepath, "r") as tf:
        lines = list(tf)
        firstword = lines[0].replace(',', ' ').split()[0]
        numeric = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '-', '+', 'e', 'E'}
        while set(firstword).issubset(numeric) == False:
            lines.pop(0)
            firstword = lines[0].replace(',', ' ').split()[0]

        freq = []
        abs_val = []
        phase = []
        for line in lines:
            words = line.split("\t")
            freq.append(float(words[0]))
            bode = words[1]
            val = bode.split(",")
            abs_val.append(float(val[0][1:-2]))
            phase.append(float(val[1][:-3]))

    return freq, abs_val, phase

def csv_parser(filepath):
    with open(filepath, 'r') as tf:
        lines = list(tf)
        firstword = lines[0].replace(',', ' ').split()[0]
        numeric = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '-', '+', 'e', 'E'}
        while set(firstword).issubset(numeric) == False:
            lines.pop(0)
            firstword = lines[0].replace(',', ' ').split()[0]

        freq = []
        abs_val = []
        phase = []
        for line in lines[:-1]:
            words = line.replace(',', ' ').split()
            if len(words) >= 3:
                words[2].replace('\n', '')
                if len(words[0]) > 0 and len(words[1]) > 0 and len(words[2]) > 0:
                    freq.append(float(words[0]))
                    abs_val.append(float(words[1]))
                    phase.append(float(words[2]))

    return freq, abs_val, phase
