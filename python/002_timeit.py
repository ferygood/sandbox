import timeit

# the timeit module lets you measure the execution time of samll bits of Python code
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)

timeit.timeit('"-".join(map(str, range(100)))', number=10000)
