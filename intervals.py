def sum_of_intervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])

    reg = 1
    result_list = []
    start = intervals[0][0]
    ammount = 0
    while reg < len(intervals):
        if intervals[reg][0] <= intervals[reg - 1][1]:
            reg += 1
        else:
            result_list.append((start, intervals[reg - 1][1]))
            start = intervals[reg][0]
            reg += 1
        if reg == len(intervals):
            if len(result_list) == 0:
                result_list.append((start, (max(intervals, key=lambda x: x[1]))[1]))
                ammount = abs(result_list[0][1] - result_list[0][0])
            else:
                result_list.append(intervals[reg - 1])
                for i in result_list:
                    ammount += abs(i[1] - i[0])
    if reg == len(intervals):
        ammount = abs(intervals[0][1] - intervals[0][0])

    return ammount


intervals = [(1, 5)]
print(sum_of_intervals(intervals))