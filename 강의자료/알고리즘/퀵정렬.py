# 대충 리스트가 있다고 하면
# 기준 값을 하나 잡고 그 값을 기준으로 좌 우로 2개의 파티션을 만든다.

def quick_sort(a: list) -> list:
    n = len(a) #리스트의 길이구함
    if n <= 1:
        print("길이가 1이라서 return",a) #리스트의 길이가 1이라면 a를 그대로 반환
        return a
    
    pivot = a[-1] #피벗으로 잡은 기준값
    a_left = []
    a_right = []
    print("길이:",n ,"피벗:", pivot)
    
    for i in range(0,n-1):
        if a[i] < pivot:
            a_left.append(a[i])
        else:
            a_right.append(a[i])

    print("왼쪽:",a_left,"오른쪽:",a_right)
    print("return : left_",quick_sort(a_left) +["기준값", pivot], [pivot] + quick_sort(a_right),"right")
    
    return quick_sort(a_left) + [pivot] + quick_sort(a_right) # 재귀함수로 자기 자신을 부름

a = list(input())

print(quick_sort(a))