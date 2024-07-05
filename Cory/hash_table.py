# symbols in the string
def count(a_string):
    a_dict = {}
    for char in a_string:
        if char in a_dict:
            a_dict[char] += 1
        else:
            a_dict[char] = 1
    print(a_dict)
count('Hello')


# two sum
def two_sum_brute(the_list, target):
    index_list = []
    for i in range(0, len(the_list)):
        for j in range(i, len(the_list)):
            if the_list[i] + the_list[j] == target:
                return [the_list[i], the_list[j]]
            
def two_sum(a_list, target):
    a_dict = {}
    for index, n in enumerate(a_list):
        rem = target - n
        if rem in a_dict:
            return index, a_dict[rem]
        else:
            a_dict[n] = index
two_sum([-1, 2, 3, 4, 7], 7)

def del_repeat(a_list):
    a_dict = {}
    except_pron = ('a')
    a_list = a_list.replace('.', ' .').split(' ')
    for i, word in enumerate(a_list):
        if word in except_pron:
            continue
        if word in a_dict:
            a_list.pop(i)
        else:
            a_dict[word] = i
    return ' '.join(a_list).replace(' .', '.')
            
a_list = "I am a self-taught programmer looking for a job as a programmer."  
del_repeat(a_list)  
'ss'.split