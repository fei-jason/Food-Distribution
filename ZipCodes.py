from uszipcode import SearchEngine

search = SearchEngine()

result = search.by_median_household_income(lower=-1, upper=30000, returns=500)

for zipcode in result:
    print(zipcode.major_city)