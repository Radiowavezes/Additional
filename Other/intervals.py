def sum_of_intervals(intervals):

    uniq_intervals = set(intervals)
    uniq_intervals = sorted(uniq_intervals, key=lambda x: x[0])
    result_intervals = []
    start = int(uniq_intervals[0][0])
    stop = int(uniq_intervals[0][1])
    counter = 0

    for interval in uniq_intervals[1:]:
        if int(interval[0]) not in range(start, stop):
            result_intervals.append((start, stop))
            start = int(interval[0])
            if start == int(uniq_intervals[-1][0]):
                stop = int(uniq_intervals[-1][1])
                result_intervals.append((start, stop))
        else:
            stop = int(interval[1])
    if len(result_intervals) > 0:
        for start, stop in result_intervals:
            while start < stop:
                counter += 1
                start += 1
    else:
        while start < stop:
            counter += 1
            start += 1
    
    return counter


intervals = [(1, 5), (6, 10)]
print(sum_of_intervals(intervals))