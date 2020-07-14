with open("AviationData.txt") as file:
    aviation_data = file.read().splitlines()

aviation_list = list()
for row in aviation_data:
    row = row.split("|")
    aviation_list.append(row)
#linear algorithm implementation   
lax_code = list()
for row in aviation_list:
    for item in row:
        if item == "LAX94LA336":
            lax_code.append(row)
            
#log(n) algorithm needs to implemented later
# code for algorithm
# more code


#aviation_data as a list of dict
aviation_dict_list = list()
header = aviation_data[0].split("|")
for row in aviation_data[1:]:
    row = row.split("|")
    row_dict = dict()
    for key, item in enumerate(row):        
        row_dict[header[key]] = item
        aviation_dict_list.append(row_dict)

lax_dict = list()       
for d in aviation_dict_list:
    if "LAX94LA336" in d:
        lax_dict.append(d)
#Count up how many accidents occurred in each U.S. state, and assign the result to
state_accidents = dict()
for row in aviation_list:
    # extract state name
    loc = row[4]
    if loc in state_accidents:
        state_accidents[loc] += 1
    else:
        state_accidents[loc] = 1
        
#sort state_accidents by descending order
state_accidents = sorted(state_accidents.items(), key=lambda x: x[1], reverse=True)
most_aviation_state = list(state_accidents.keys())[0]

#count how many fatalities and serious injuries occurred during each month
