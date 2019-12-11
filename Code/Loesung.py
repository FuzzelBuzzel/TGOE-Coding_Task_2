def merge(list_input):

    if not list_input:
        return "leere Liste"

    try:
        # Sortieren der Liste.
        list_input.sort(key=lambda x: x[0])

        # Fuellen der Liste mit dem kleinsten Intervall
        list_merged = [list_input[0]]

        for current in list_input:
            # Hilfsvariable  zum Merken des vorherigen Intervalls
            previous = list_merged[-1]

            # Untere Grenze des aktuellen-  <= obere Grenze des vorherigen Intervalls
            if current[0] <= previous[1]:
                previous[1] = max(previous[1], current[1])
            else:
                list_merged.append(current)

        return list_merged

    except:
        return "Fehlerhafte Eingabe"


if __name__ == '__main__':

    list_input = [[25,30], [2,19], [14, 23], [4,8]]
    print(merge(list_input))
