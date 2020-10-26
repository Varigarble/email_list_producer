"""Produce a list of most common email formats, based on person names"""

name_first = input("enter first name or 0: ", )
name_middle = input("enter middle name: ", )
name_last = input("enter last name: ", )
email_domain = "@" + input("enter stuff after '@': ", )

names = []
if name_first != "0":
    names.append(name_first)
if name_middle != "0":
    names.append(name_middle)
if name_last != "0":
    names.append(name_last)
reset_names = names
prefixes = [''.join(names)]
emails = []  # prefixes@email_domain

#  Add initial dot permutations prior to string slicing
if len(names) == 3:
    i_dot_names_0 = [names[0]] + [names[1]] + ['.'] + [names[2]]
    prefixes.append(''.join(i_dot_names_0))
i_dot_names_1 = [names[0]] + ['.'] + [names[1]]
if len(names) == 3:
    i_dot_names_1 = i_dot_names_1 + [names[2]]
prefixes.append(''.join(i_dot_names_1))
if len(names) == 3:
    i_dot_names_2 = [names[0]] + ['.'] + [names[1]] + ['.'] + [names[2]]
    prefixes.append(''.join(i_dot_names_2))

i = len(names) - 1
curr_name = names[i]

while i >= 0:
    #  Perform no string slice if an initial was entered to avoid endless loop
    if (curr_name == reset_names[i]) and (len(curr_name) == 1):
        prefixes.append(''.join(names))
        i -= 1

    if curr_name == reset_names[i]:
        curr_name = curr_name[:1]
        names = names[0:i] + [curr_name] + reset_names[i+1:]

        dot_names_0 = [names[0]] + [names[1]] + ['.']  # assume there are only two names
        if len(names) == len(dot_names_0):
            dot_names_0 = dot_names_0 + [names[-1]]  # add the 3rd name
        if (dot_names_0[-1] != '.') and (dot_names_0 not in prefixes):
            prefixes.append(''.join(dot_names_0))

        dot_names_1 = [names[0]] + ['.'] + [names[1]]
        if len(names) == len(dot_names_1):
            dot_names_1 = dot_names_1 + [names[-1]]
        if (dot_names_1[-1] != '.') and (dot_names_1 not in prefixes):
            prefixes.append(''.join(dot_names_1))

        if len(names) == 3:
            dot_names_2 = [names[0]] + ['.'] + [names[1]] + ['.'] + [names[2]]
            if dot_names_2 not in prefixes:
                prefixes.append(''.join(dot_names_2))

        prefixes.append(''.join(names))

        i = len(names) - 1
        curr_name = names[i]
    else:
        i -= 1
        curr_name = names[i]

for prefix in prefixes:
    combine = prefix + email_domain
    emails.append(combine)

for email in emails:
    print(emails.index(email), email)

title = prefixes[0] + ' potential emails'

with open(str(title) + '.txt', 'a') as file:
    for email in emails:
        file.write(email)
        file.write('\n')

'''Varigarble -- 2020'''
