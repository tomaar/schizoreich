def load_tags():
    with open("../../common/country_tags/00_countries.txt") as file:
        list1 = [line[:3] for line in file]
    with open("../../common/country_tags/01_countries.txt") as file:
        list2 = [line[:3] for line in file]
    with open("../../common/country_tags/new_countries.txt") as file:
        list3 = [line[:3] for line in file]
    list = list1 + list2 + list3
    return list

print(load_tags())