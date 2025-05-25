a = input("Enter elements of Set A separated by spaces: ")
a = set(a.split())
a = {int(i) for i in a}

b = input("Enter elements of Set B separated by spaces: ")
b = set(b.split())
b = {int(i) for i in b}

a_union_b = a | b
a_intersection_b = a & b
a_diff_b = a - b
b_diff_a = b - a

print("Union:", a_union_b)
print("Intersection:", a_intersection_b)
print("A-B:", a_diff_b)
print("B-A:", b_diff_a)
