import csv

create_file = 'file.csv'

data = [
    ['closefriend' , 'Favourite_Movie' ,'Favourite_pet' ],
    ['Heart','state_gate','dog'],
    ['Art','arcene_animation','fox'],
    ['Name','lunetoon','tiger'],
]

with open(create_file,"w",newline='') as file:
    writer = csv.writer(file)

    for row in data:
        writer.writerow(row)

print(f'The process to create {create_file} had done')
