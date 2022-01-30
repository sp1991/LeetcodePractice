def twosum(a_list, target):
  a_dict = {}    # Creating an empty dictionary
  
  for idx,value in enumerate(a_list):   # iterating thorugh the list 'a'
    #print(idx,value)
    a_dict[value] = idx  # adding key:value pairs to dict, for a key which is the element of list a, adding its index as value. 
  print(a_dict)

  for idx,value in enumerate(a_list):  #. iterating through each element and its index in the list using enumerate() which returns a tuple of (index, element)
    diff = (target-value)  # caldulating diff
    dict_idx = a_dict.get(diff) # capturing the index of diff from the dictionary if it is present, using get method. get returns NONE of the diff does not exist. 
    if dict_idx is not None and dict_idx != idx: # checking if diff exists and it is not equal to the current element. 
      return [idx, dict_idx]

print(twosum([-1,-2,-3,-4,-5],-8))