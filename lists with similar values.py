# Define three lists with similar values
list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 6, 7]
list3 = [4, 5, 6, 7, 8]

# Compare common elements between list1 and list2, list1 and list3
common_list2 = len(set(list1) & set(list2))
common_list3 = len(set(list1) & set(list3))

# Print the result
if common_list2 > common_list3:
    print("List2 is more similar to List1.")
elif common_list3 > common_list2:
    print("List3 is more similar to List1.")
else:
    print("List2 and List3 are equally similar to List1.")
