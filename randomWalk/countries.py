from pygal_maps_world.i18n import COUNTRIES

# for code in sorted(COUNTRIES.keys()) :
#     print(code,COUNTRIES[code])

def get_country_code(country_name):
    for code , name in COUNTRIES.items():
        if name == country_name:
            return code
        return None
# a = get_country_code('Afghanistan')
# print(a)