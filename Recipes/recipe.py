import fnmatch

cook_book = {}
dish = ''
ing = []
num = 999

with open('recipes.txt') as f:
	for line in f.readlines():
		line = line.replace('\n', '')

		if not('|' in line) and not(fnmatch.fnmatch(line, "[0-9]")):
			dish = line
			ing = []

		elif '|' in line:
			ing.append(line.split('|'))


		elif fnmatch.fnmatch(line, "[0-9]"):
			num = int(line)

			
		if len(ing) == num:
			tmp = []
			for el in ing:
				temp_dct = {}
				temp_dct['ingredient_name'] = el[0]
				temp_dct['quantity']		= el[1]
				temp_dct['measure']			= el[2]
				tmp.append(temp_dct)

			if dish not in cook_book or len(cook_book[cook_book.index(dish)]) < num:
				cook_book[dish] = tmp

			


def get_shop_list_by_dishes(dishes, person_count):
	shop_list = {}

	for dish in dishes:
		for k, v in cook_book.items():
			if dish == k:
				for lst in v:
					shop_list[lst['ingredient_name']] = {'measure': lst['measure'], 'quantity': int(lst['quantity'])*person_count}
	print(shop_list)




get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)








