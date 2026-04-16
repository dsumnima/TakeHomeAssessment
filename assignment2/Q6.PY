def find_country(countries, target):
    if target in countries:
        return countries.index(target)
    else:
        return "Not Found in List"

# Example
countries = ["Nepal", "India", "China", "USA"]
print(find_country(countries, "India"))
print(find_country(countries, "Japan"))
