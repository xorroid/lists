import math

def sortedIndex(a: list, item):
  start = 0
  end = len(a)
  depth = math.log(len(a) + 1, 2)
  i = 0
  while i <= math.ceil(depth):
    mid = (start + end) // 2
    if start >= end:
      break
    if item == a[mid]:
      return mid
    elif item > a[mid]:
      start = mid + 1
    else:
      end = mid
    i += 1
  return mid

def sortedInsert(a: list, item):
  a.insert(sortedIndex(a, item), item)
  return a
