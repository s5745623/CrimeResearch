#Steven Chang

#Data Analytics Project 1

# -*- coding: utf-8 -*-


import requests
import pprint


#collecting data crime.txt
url = "https://data.montgomerycountymd.gov/resource/yc8a-5df8.json?$$app_token=tX2XTxtf7mZd8F5eQ7enqtsPO"

response = requests.get(url)

data = response.json()

f = open("crime.txt","w")
f.write(response.text)
f.close()

#downloaded data
print("\nTotal amount of downloaded data:",len(data))
print("\nTotal amount of attributes:",len(data[0]))


#count null agency

count = 0
d = 0
for d in data:
    if "agency" not in d:
        count += 1

print("\n\n\nTotal number of 'null' agency:\n" ,count)


#ratio of null agency

ratio_agency = 0
ratio_agency = (count / len(data)) * 100
print("\nPercentage of the 'null' agency received in the attribute agency:\n", ratio_agency, "%")



#count null case_number

count = 0
d = 0
for d in data:
    if "case_number" not in d:
        count += 1

print("\n\n\nTotal number of 'null' case_number:\n" ,count)


#ratio of null case_number

ratio_case_number = 0
ratio_case_number = (count / len(data)) * 100
print("\nPercentage of the 'null' case_number received in the attribute case_number:\n", ratio_case_number, "%")

#count null city

count = 0
d = 0
for d in data:
    if "city" not in d:
        count += 1

print("\n\n\nTotal number of 'null' city:\n" ,count)


#ratio of null city

ratio_city = 0
ratio_city = (count / len(data)) * 100
print("\nPercentage of the 'null' city received in the attribute city:\n", ratio_city, "%")

#count null date

count = 0
d = 0
for d in data:
    if "date" not in d:
        count += 1

print("\n\n\nTotal number of 'null' date:\n" ,count)


#ratio of null date

ratio_date = 0
ratio_date = (count / len(data)) * 100
print("\nPercentage of the 'null' date received in the attribute date:\n", ratio_date, "%")

#count null district

count = 0
d = 0
for d in data:
    if "district" not in d:
        count += 1

print("\n\n\nTotal number of 'null' district:\n" ,count)


#ratio of null district

ratio_district = 0
ratio_district = (count / len(data)) * 100
print("\nPercentage of the 'null' district received in the attribute district:\n", ratio_district, "%")

#count null incident_id

count = 0
d = 0
for d in data:
    if "incident_id" not in d:
        count += 1

print("\n\n\nTotal number of 'null' incident_id:\n" ,count)


#ratio of null incident_id

ratio_incident_id = 0
ratio_incident_id = (count / len(data)) * 100
print("\nPercentage of the 'null' incident_id received in the attribute incident_id:\n", ratio_incident_id, "%")

#count null incident_type

count = 0
d = 0
for d in data:
    if "incident_type" not in d:
        count += 1

print("\n\n\nTotal number of 'null' incident_type:\n" ,count)


#ratio of null incident_type

ratio_incident_type= 0
ratio_incident_type = (count / len(data)) * 100
print("\nPercentage of the 'null' incident_type received in the attribute incident_type:\n", ratio_incident_type, "%")

#count null location

count = 0
d = 0
for d in data:
    if "location" not in d:
        count += 1

print("\n\n\nTotal number of 'null' location:\n" ,count)


#ratio of null location

ratio_location= 0
ratio_location = (count / len(data)) * 100
print("\nPercentage of the 'null' location received in the attribute location:\n", ratio_location, "%")

#count null police_district_number

count = 0
d = 0
for d in data:
    if "police_district_number" not in d:
        count += 1

print("\n\n\nTotal number of 'null' police_district_number:\n" ,count)


#ratio of null police_district_number

ratio_police_district_number = 0
ratio_police_district_number = (count / len(data)) * 100
print("\nPercentage of the 'null' police_district_number received in the attribute police_district_number:\n", ratio_police_district_number, "%")


#count null start_date

count = 0
d = 0
for d in data:
    if "start_date" not in d:
        count += 1

print("\n\n\nTotal number of 'null' start_date:\n" ,count)


#ratio of null start_date

ratio_start_date= 0
ratio_start_date = (count / len(data)) * 100
print("\nPercentage of the 'null' start_date received in the attribute start_date:\n", ratio_start_date, "%")

#count null state

count = 0
d = 0
for d in data:
    if "state" not in d:
        count += 1

print("\n\n\nTotal number of 'null' state:\n" ,count)


#ratio of null state

ratio_state= 0
ratio_state = (count / len(data)) * 100
print("\nPercentage of the 'null' state received in the attribute state:\n", ratio_state, "%")

#count null narrative

count = 0
d = 0
for d in data:
    if "narrative" not in d:
        count += 1

print("\n\n\nTotal number of 'null' narrative(Class Description):\n" ,count)


#ratio of null narrative

ratio_nar = 0
ratio_nar = (count / len(data)) * 100
print("\nPercentage of the 'null' narrative received in the attribute narrative:\n", ratio_nar, "%")

#count null places

count = 0
d = 0
for d in data:
    if "place" not in d:
        count += 1

print("\n\n\nTotal number of 'null' places:\n" ,count)


#ratio of null places

ratio_place = 0
ratio_place = (count / len(data)) * 100
print("\nPercentage of the 'null' places received in the attribute place:\n", ratio_place, "%")


#count null beat

count = 0
d = 0
for d in data:
    if "beat" not in d:
        count += 1

print("\n\n\nTotal number of 'null' beat:\n" ,count)


#ratio of null beat

ratio_beat = 0
ratio_beat = (count / len(data)) * 100
print("\nPercentage of the 'null' beat received in the attribute beat:\n", ratio_beat, "%")

#count null pra

count = 0
d = 0
for d in data:
    if "pra" not in d:
        count += 1

print("\n\n\nTotal number of 'null' pra:\n" ,count)


#ratio of null pra

ratio_pra= 0
ratio_pra = (count / len(data)) * 100
print("\nPercentage of the 'null' pra received in the attribute pra:\n", ratio_pra, "%")

#count null sector

count = 0
d = 0
for d in data:
    if "sector" not in d:
        count += 1

print("\n\n\nTotal number of 'null' sector:\n" ,count)


#ratio of null sector

ratio_sector= 0
ratio_sector = (count / len(data)) * 100
print("\nPercentage of the 'null' sector received in the attribute sector:\n", ratio_sector, "%")



#count null zip

count = 0
d = 0
for d in data:
    if "zip_code" not in d:
        count += 1

print("\n\n\nTotal number of 'null' zipcode:\n" ,count)


#ratio of null zip

ratio_zip = 0
ratio_zip = (count / len(data)) * 100
print("\nPercentage of the 'null' zipcode in the attribute zipcode:\n", ratio_zip, "%")




#count null end date/time

count = 0
d = 0
for d in data:
    if "end_date" not in d:
        count += 1

print("\n\nTotal number of 'null' end date/time:\n" ,count)

#ratio of end date/time

ratio_end = 0
ratio_end = (count / len(data)) * 100
print("\nPercentage of the 'null' end date/time:\n", ratio_end, "%")





#counting Agency not MCPD
count = 0
d = 0
for d in data:
    if d["agency"] != "MCPD":
        count += 1

print("\n\n\n\n\n\n\n\n\n\nTotal number of Agencies is not MCPD:\n" ,count)

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

print("\n\n\n\n\n\nShow from high to low in the amounts of crime occur in each district:\n")
pprint.pprint([(w, district[w]) for w in sorted(district, key=district.get, reverse=True)])


#Feature Generation
#seperate the TOP THREE CRIME RATE districts into 2014 2015 2016

print("\n\nTOP THREE Crime Rate Districts:")

d = 0
count = 0
for d in data:
    if d["district"] == "SILVER SPRING":
        if "2014" in d["start_date"]:
            count += 1

print("\nTop 1:\nCrime occurred in Silver Spring 2014\n",count)

d = 0
count = 0
for d in data:
    if d["district"] == "SILVER SPRING":
        if "2015" in d["start_date"]:
            count += 1

print("Top 1:\nCrime occurred in Silver Spring 2015\n",count)

d = 0
count = 0
for d in data:
    if d["district"] == "SILVER SPRING":
        if "2016" in d["start_date"]:
            count += 1

print("Top 1:\nCrime occurred in Silver Spring 2016\n",count)

d = 0
count = 0
for d in data:
    if d["district"] == "WHEATON":
        if "2014" in d["start_date"]:
            count += 1

print("\n\nTop 2:\nCrime occurred in Wheaton 2014\n",count)

d = 0
count = 0
for d in data:
    if d["district"] == "WHEATON":
        if "2015" in d["start_date"]:
            count += 1

print("Top 2:\nCrime occurred in Wheaton 2015\n",count)

d = 0
count = 0
for d in data:
    if d["district"] == "WHEATON":
        if "2016" in d["start_date"]:
            count += 1

print("Top 2:\nCrime occurred in Wheaton 2016\n",count)

d = 0
count = 0
for d in data:
    if d["district"] == "MONTGOMERY VILLAGE":
        if "2014" in d["start_date"]:
            count += 1

print("\n\nTop 3:\nCrime occurred in Montgomery Village 2014\n",count)

d = 0
count = 0
for d in data:
    if d["district"] == "MONTGOMERY VILLAGE":
        if "2015" in d["start_date"]:
            count += 1

print("Top 3:\nCrime occurred in Montgomery Village 2015\n",count)

d = 0
count = 0
for d in data:
    if d["district"] == "MONTGOMERY VILLAGE":
        if "2016" in d["start_date"]:
            count += 1

print("Top 3:\nCrime occurred in Montgomery Village 2016\n",count)

#calculate total of each place crime occured
count = 0
d = 0
place = {}
for d in data:
    if d["place"] not in place:
        place[d["place"]] = 0
    place[d["place"]] += 1

#Child abuse in single family from 2013 to 2016
print("\n\nChild abuse in single family from 2013 to 2016:\n")

d = 0
count = 0
for d in data:
    if "Single Family" in d["place"]:
        if "ABUSE/CHILD" in d["narrative"]:
            if "2013" in d["start_date"]:
                count += 1

print("abuse2013\n",count)

d = 0
count = 0
for d in data:
    if "Single Family" in d["place"]:
        if "ABUSE/CHILD" in d["narrative"]:
            if "2014" in d["start_date"]:
                count += 1

print("abuse2014\n",count)

#
d = 0
count = 0
for d in data:
    if "Single Family" in d["place"]:
        if "ABUSE/CHILD" in d["narrative"]:
            if "2015" in d["start_date"]:
                count += 1

print("abuse2015\n",count)

#
d = 0
count = 0
for d in data:
    if "Single Family" in d["place"]:
        if "ABUSE/CHILD" in d["narrative"]:
            if "2016" in d["start_date"]:
                count += 1

print("abuse2016\n",count)

#highest crime occur district

print("\n\n\nShow from high to low in crime occur in different places:\n")
pprint.pprint([(w, place[w]) for w in sorted(place, key=place.get, reverse=True)])

#calculate total of each class description of crime
count = 0
d = 0
narrative = {}
for d in data:
    if d["narrative"] not in narrative:
        narrative[d["narrative"]] = 0
    narrative[d["narrative"]] += 1

#highest crime occur district

print("\n\n\nShow from high to low in the class description of crime:\n")
pprint.pprint([(w, narrative[w]) for w in sorted(narrative, key=narrative.get, reverse=True)])






