import re
import more_itertools

file = open('iproutes.txt', 'r')

gig_intf_regex = re.compile(
    r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,3}) | (GigabitEthernet[0-9]/[0-9])')

# merge_all_list = []

for line in file:
    match_pattern = gig_intf_regex.findall(line)
    tuples_to_list = [list(t) for t in zip(*match_pattern)]
    list_marge = list(more_itertools.flatten(tuples_to_list))
    eliminate_empty_string = [i for i in list_marge if i]

    if len(eliminate_empty_string) >= 2:
        print(eliminate_empty_string)
        # test = list.count(eliminate_empty_string[GigabitEthernet0/1])
        # print(test)
        # merge_all_list = eliminate_empty_string[0] + eliminate_empty_string[1]
        # print(merge_all_list)
