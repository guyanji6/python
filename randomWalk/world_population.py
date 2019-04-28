import json
import countries

filename = 'populaition_data.json'
with open(filename) as f:
    pop_data = json.load(f)

for i in pop_data:
    if i['Year'] == '2009':
        country_name = i['Country Name']
        value = int(float(i['Value']))
        # print(country_name + ' : ' +value)
        # print(country_name +' : '+ str(value))
        code = countries.get_country_code(country_name)
        if code:
            print(code+' : '+str(value)+'\n')
        # else:
        #     print('error ' + country_name)