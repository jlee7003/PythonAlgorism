def quick_sort(a:list) -> list:
    n = len(a)
    if n <= 1:
        return a

    pivot = a[-1]
    a_left = []
    a_right = []

    for i in range(0 , n-1):
        if a[i] < pivot:
            a_left.append(a[i])
        else:
            a_right.append(a[i])

    return quick_sort(a_left) + [pivot] + quick_sort(a_right)