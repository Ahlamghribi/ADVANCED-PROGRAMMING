
city_population = [] 
while True:
    city_name = input("Enter city name (or type 'stop' to finish): ")
     
    if city_name.lower() == 'stop':
        break
    
    population = len(city_name) * 1000000
    
    city_population.append((city_name, population))

city_population.sort(key=lambda x: x[1], reverse=True)

print("\nCities sorted by population:")
for city, population in city_population:
    print(f"{city}: {population} citizens")
