#learn iterator and iterable
#it is the iterable, x is the iterator

it=["iam","an","engineer"]
x=iter(it)

while True:
    try:
        print(next(x))
    except StopIteration:
        print("No more values to print")
        break