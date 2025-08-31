# EXPERIMENT_NO_14.1

my_set = {1,2,3,6,8,12,78,45,23,67}
another_set = set([3,4,5,12,78,99,48,9,19,29])
# print(my_set)
# print(another_set)

# EXPERIMENT_NO_14.2

my_set.add(4)
my_set.update([5, 6])
# print(my_set)

my_set.remove(3)
my_set.discard(7)
# print(my_set)


my_set = {1,2,3,6,8,12,78,45,23,67}
another_set = set([3,4,5,12,78,99,48,9,19,29])

union_set = my_set | another_set
union_set = my_set.union(another_set)
# print('union set :', union_set)

intersection_set = my_set & another_set
intersection_set = my_set.intersection(another_set)
# print('intersection set :',intersection_set)

difference_set = my_set - another_set
difference_set = my_set.difference(another_set)
# print('difference set :',difference_set)

sym_diff_set = my_set ^ another_set
sym_diff_set = my_set.symmetric_difference(another_set)
# print('symmetric difference :',sym_diff_set)

is_subset = my_set <= another_set
is_subset = my_set.issubset(another_set)
# print('is subset ?:',is_subset)

is_superset = my_set >= another_set
is_superset = my_set.issuperset(another_set)
# print('is super set ?:',is_superset)

is_disjoint = my_set.isdisjoint(another_set)
# print('is disjoint ?:',is_disjoint)

squares = {x**2 for x in range(1, 6)}
print(squares)
