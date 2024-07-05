import array


arr =array.array('f', (1.0, 1.5, 2.0, 2.5))
print(arr[1])



def move_zeros(a_list):
    zero_index = 0
    for index, n in enumerate(a_list):
        if n != 0:
            a_list[zero_index] = n
            if zero_index != index:
                a_list[index] = 0
            zero_index += 1
    return(a_list)

a_list = [8, 0, 3, 0, 12]
move_zeros(a_list)
print(a_list)



movie_list = [ "Interstellar", "Inception",
"The Prestige", "Insomnia", "Batman Begins"
]
ratings_list = [1, 10, 10, 8, 6]
print(list(zip(movie_list, ratings_list)))



def return_dups(an_iterable):
    dups = []
    a_set = set()
    
    for item in an_iterable:
        l1 = len(a_set)
        a_set.add(item)
        l2 = len(a_set)
        if l1 == l2:
            dups.append(item)
    return dups

a_list = [
"Susan Adams","Kwame Goodall",
"Jill Hampton","Susan Adams"]
dups = return_dups(a_list)
print(dups)



# Finding the area of ​​intersection of two lists
this_weeks_winners = [2, 43, 48, 62, 64, 28, 3]
most_common_winners = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]

def return_iter(list1, list2):
    list3 = [v for v in list1 if v in list2]
    return list3
return_iter(this_weeks_winners, most_common_winners)

def return_iter_best(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))
return_iter_best(this_weeks_winners, most_common_winners)



this_weeks_winners = [2, 43, 48, 62, 64, 28, 3]
def even_then_odd(l1):
    l1 = []
    l2 = []
    for i in this_weeks_winners:
        if i % 2 == 0:
            l1.append(i)
        else:
            l2.append(i)
    return l1 + l2
even_then_odd(this_weeks_winners)