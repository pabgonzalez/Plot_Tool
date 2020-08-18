def spice_parser(filepath):
    with open(filepath, "r") as tf:
        lines = list(tf)
        lines.pop(0)

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
        lines.pop(0)

        freq = []
        abs_val = []
        phase = []
        for line in lines:
            words = line.split(",")
            freq.append(float(words[0]))
            abs_val.append(float(words[1]))
            phase.append(float(words[2][:-1]))

    return freq, abs_val, phase
