def dirReduc(arr):
    pair1 = ('north', 'south')
    pair2 = ('east', 'west')
    result = arr[:]
    index = 0
    while index < len(result) - 1:
        if (
            result[index].lower() in pair1 and result[index + 1].lower() in pair1
            and result[index].lower() != result[index + 1].lower()
            or result[index].lower() in pair2 and result[index + 1].lower() in pair2
            and result[index].lower() != result[index + 1].lower()
            ):
            result.pop(index)
            result.pop(index)
            if index >= 1:
                index -= 1
        else:
            index += 1
    return result

            

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))