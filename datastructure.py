# list datastructure - its just a variable that will store multiple variables.
# list are mutable/changeable and are ordered in that the first element doesn't change unless changed.(works for first two)
# everything inside the list is called an element
my_list = ["apple", "banana", "cherry", "watermelon", "oranges"]
my_list.sort()
print(my_list)
my_numlist = [11, -13, 0, 1, 65, 6, 57, -28,79]
my_numlist.append(67)
my_numlist.sort()

print(my_numlist)


my_list[1]="pineapples"
print(f"I love eating {my_list[1]}")

# tuple datastructures- they are immutable/unchangeable
my_tuple = ("mercedes", "toyota", "subaru", "nissan","bmw","rangerover")

print(my_tuple)
print(f"{my_tuple[3]} is manufactured in Japan")

# set datastructure- it is unordered
# mainly used in
my_set = {"Kenya", "Uganda", "Nigeria", "Mozambique", "south africa"}
my_set.add("Senegal")

print(my_set)

# dictionaries data structures- it is immutable
my_dic={"Name":"Ken", "Age": "30", "Gender":"Male", "Proffesion": "software engineering"}
print(my_dic)
print(f"My name is {my_dic['Name']}")
print(f"My age is {my_dic['Age']}" f" " f"and i am a {my_dic['Gender']}" f" " f"and my proffesion is {my_dic['Proffesion']}")