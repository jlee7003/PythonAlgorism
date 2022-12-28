def solution(A, B):
    Asplit = list(A)
    Bsplit = list(B)
    count = 0
    if(A == B):
      return 0
    for i in A:
      count +=1
      Asplit.insert(0,Asplit[len(A)-1])
      Asplit.pop()
      if Asplit == Bsplit:
        return count
      elif count == len(A):
        return -1




print(solution("apple", "apple"))


# def solution(A, B):
#   for i in range(len(A)):
#     print(A[i])
# solution("hello", "r3ffe")