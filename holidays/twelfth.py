def range_generator(start, stop, step=1):
    while start <= stop:
        yield start
        start += step

def custum_range_generator(*args):
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop = args
        step = 1
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise TypeError("Custum_range_generator expected at most 3 arguments, got 4")
    
    while (step > 0 and start < stop) or (step < 0 and start > stop):
        yield start
        start += step


gen = custum_range_generator(15) 
for num in gen:
    print(num)