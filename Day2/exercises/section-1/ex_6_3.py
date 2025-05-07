def raise_stop_iteration():
    lst = [1, 2, 3]
    iterator = iter(lst)

    try:
        print(next(iterator))
        print(next(iterator))
        print(next(iterator))
        # Manually raising StopIteration
        raise StopIteration("No more items")
    except StopIteration as e:
        print(f"Caught exception: {e}")


raise_stop_iteration()
