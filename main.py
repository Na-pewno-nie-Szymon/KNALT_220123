import csv

def low_carb_food(kcal = 0, carbs = 0):
    if kcal != "" and carbs != "":
        if int(kcal)/2 > int(carbs) * 4:
            return True
        return False
    elif kcal == '':
        return False
    elif carbs == '':
        return True
    else: 
        return False

def low_carb_food_cat():
    with open('food/lowCarbFood.csv') as file:
        reader = csv.reader(file, delimiter=';')
        categories = {'Baked Goods'}
        
        rows = []
        for row in reader:
            rows.append(row[0])
            categories.add(row[0])
        categories.remove('ď»żCategory')

        count_food = {}
        for cat in categories:
            count_food[cat] = rows.count(cat)
        
    with open('food/Categorized_low_carb_foods.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        header = []
        row = []
        for key in count_food:
            header.append(key)
            row.append(count_food[key]) 
        
        writer.writerow(header)
        writer.writerow(row)


def main():
    with open('food/foods.csv') as file:
        reader = csv.reader(file, delimiter=';')

        header = []
        header = next(reader)
    
        rows = []
        for row in reader:
            rows.append(row)

    with open('food/lowCarbFood.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        writer.writerow(header)
        for row in rows:
            if low_carb_food(kcal = row[3], carbs= row[6]):
                writer.writerow(row)

    low_carb_food_cat()

if __name__=='__main__': main()
