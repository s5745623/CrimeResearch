#Steven Chang

# -*- coding: utf-8 -*-


import requests
import pprint


#crime.txt
url = "https://data.montgomerycountymd.gov/resource/yc8a-5df8.json?$$app_token=tX2XTxtf7mZd8F5eQ7enqtsPO"

response = requests.get(url)

data = response.json()

f = open("crime2.txt","w")
f.write(response.text)
f.close()


#count null zip

count = 0
d = 0
for d in data:
    if "zip_code" not in d:
        count += 1

print("Total number of empty zipcode:\n" ,count)

#ratio of null zip

ratio_zip = 0
ratio_zip = (count / len(data)) * 100
print("\nPercentage of the null zipcode in the attribute zipcode:\n", ratio_zip, "%")


#counting Agency not MCPD
count = 0
d = 0
for d in data:
    if d["agency"] != "MCPD":
        count += 1

print("\n\nTotal number of Agencies is not MCPD:\n" ,count)

#ratio of Agency not MCPD
ratio_agency = 0
ratio_agency = (count / len(data)) * 100
print("\nPercentage of the Agency which is not MCPD:\n", ratio_agency, "%")

#count class description with value of stolen belongings in the statement
count = 0
d = 0
for d in data:
    if "$" in d["narrative"]:
        count += 1

print("\n\nClass description with value of stolen belongings:\n", count)

#percent of the total of class description with fine
ratio_fine = 0
ratio_fine = (count / len(data)) * 100

print("\nPercentage of the Class description with value of stolen belongings:\n", ratio_fine, "%\n\n")



#calculate total of each different cities
count = 0
d = 0
district = {}
for d in data:
    if d["district"] not in district:
        district[d["district"]] = 0
    district[d["district"]] += 1

#highest crime occur district

print("Show highest amounts of crime occur district to the lowest:\n")
pprint.pprint([(w, district[w]) for w in sorted(district, key=district.get, reverse=True)])






