def find_i_positions(text):
    positions = []
    for index in range(len(text)):
        if text[index].lower() == "i":
            positions.append(index)
    return positions

text = "hello my name is Ahmed, iam student at iti"
print("Positions of 'i':", find_i_positions(text))