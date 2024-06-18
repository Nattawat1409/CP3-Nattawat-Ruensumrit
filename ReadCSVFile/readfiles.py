import csv

with open('readfiles.txt') as csv_file: # provide the name to call name of 'csv_file'
    csv_reader = csv.reader(csv_file,delimiter=',')
    line_countis = 0
    for row in csv_reader:
        print(f'the {row} are ')
        if line_countis == 0:
            print(f'Column names are {",".join(row)}')
            line_countis += 1
        else:
            print(f'\t{row[0]} have a student ID is {row[1]} ,and have a career is {row[2]} ')
            line_countis += 1

    print(f'Process {line_countis} lines.')