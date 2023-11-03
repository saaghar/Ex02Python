# Questtion 1
# Write a function tsv2list(FILE), which reads a tab-separated file and returns a list of dictionaries, where
# the first line defines the column names,
# the rest of the lines are implemented as dictionaries with these column names as keys
# values that consist in digits are converted to int (define a separate function convert_value() for this

import csv

def convert_value(s):
    try:
        converted = int(s)
    except ValueError:
        converted = s
    return converted


def tsv2list(file):
    with open(file) as tsv:
        dictlist = list(csv.DictReader(tsv, delimiter="\t"))
    for dict in dictlist:
        for (key,val) in dict.items():
            dict[key] = convert_value(val)
    return dictlist






if __name__ == '__main__':


    file_path = '/Users/saghararab/Desktop/Chalmers/AdvancedPythonChalmers/countries.tsv'
    result = tsv2list(file_path)

    for item in result:
        print(item)


