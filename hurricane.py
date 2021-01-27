#Return "damages not recorded" as NA values
def convert_damages_data(damages):
    conversion = {"M": 1000000,
              "B": 1000000000}
print(type(damages))

update_damages = list()
for damage in damages:
    if damage == "Damages not recorded":
        update_damages.append(damage)

for damage in update_damages:
    if damage == "Damages not recorded":
        damage[0:] == "NA"
    
