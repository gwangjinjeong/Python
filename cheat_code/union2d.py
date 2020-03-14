def union2d(arr1, arr2):
  arr1 = np.array(arr1)
  arr2 = np.array(arr2)
  loc = arr2 == 0
  arr2[loc] = arr1[loc]
  return arr2
