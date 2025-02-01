from line import Line

def make_line_list(arr, x, y):

    line_list = []

    string_arr = str(arr)

    X = x
    Y = y

    for character in string_arr:

        if character == "{":
            line_list.append(Line(X, Y, ""))
            X = x + 18
            Y += 20

        if character == "}":
            line_list.append(Line(X, Y, ""))
            X = x + 18
            Y += 20

        if character == ",":
            line_list.append(Line(X, Y, ","))
            Y += 20
            X = x + 18
        
        else:
            line_list.append(Line(X, Y, character))
            X += 10

    return line_list


