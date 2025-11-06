# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1. Update Recorded Damages
conversion = {"M": 1000000, "B": 1000000000}

def updated_damages(damages):
    updated = []
    for damage in damages:
        if damage == "Damages not recorded":
            updated.append(damage)
        else:
            # Extract numeric part and suffix (M or B)
            if damage[-1] in conversion:
                value = float(damage[:-1]) * conversion[damage[-1]]
                updated.append(value)
            else:
                updated.append("Damages not recorded")
    return updated

updated_damages_list = updated_damages(damages)
print(updated_damages_list)

def create_hurricane_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricanes = {}
    
    for i in range(len(names)):
        hurricanes[names[i]] = {
            'Name': names[i],
            'Month': months[i],
            'Year': years[i],
            'Max Sustained Wind': max_sustained_winds[i],
            'Areas Affected': areas_affected[i],
            'Damage': damages[i],
            'Deaths': deaths[i]
        }
    
    return hurricanes


hurricanes = create_hurricane_dict(
    names, 
    months, 
    years, 
    max_sustained_winds, 
    areas_affected, 
    damages, 
    deaths
)

# Example: View data for the first hurricane
print(hurricanes['Cuba I'])

# 3. Organizing by Year

def organize_by_year(hurricanes):
    hurricanes_by_year = {}

    for hurricane in hurricanes.values():
        year = hurricane['Year']
        if year not in hurricanes_by_year:
            hurricanes_by_year[year] = [hurricane]
        else:
            hurricanes_by_year[year].append(hurricane)
    
    return hurricanes_by_year


hurricanes_by_year = organize_by_year(hurricanes)

# Example: View hurricanes from 1932
print(hurricanes_by_year[1932])


# 4. Counting Damaged Areas

def count_affected_areas(hurricanes):
    area_counts = {}
    
    for hurricane in hurricanes.values():
        for area in hurricane['Areas Affected']:
            if area not in area_counts:
                area_counts[area] = 1
            else:
                area_counts[area] += 1
    
    return area_counts

area_counts = count_affected_areas(hurricanes)

for area, count in list(area_counts.items())[:10]:
    print(f"{area}: {count}")


# 5. Calculating Maximum Hurricane Count

def most_affected_area(area_counts):
    max_area = None
    max_count = 0
    
    for area, count in area_counts.items():
        if count > max_count:
            max_area = area
            max_count = count
    
    return (max_area, max_count)


most_hit_area, hit_count = most_affected_area(area_counts)
print(f"The area most affected by hurricanes is {most_hit_area}, which was hit {hit_count} times.")

# 6. Calculating the Deadliest Hurricane

def deadliest_hurricane(hurricanes):
    max_deaths = 0
    deadliest = ""
    
    for name, data in hurricanes.items():
        if data["Deaths"] > max_deaths:
            max_deaths = data["Deaths"]
            deadliest = name
    
    return (deadliest, max_deaths)


deadliest_name, death_count = deadliest_hurricane(hurricanes)
print(f"The deadliest hurricane was {deadliest_name}, which caused {death_count} deaths.")


mortality_scale = {
    0: 0,
    1: 100,
    2: 500,
    3: 1000,
    4: 10000
}

def rate_by_mortality(hurricanes, scale):
    mortality_dict = {key: [] for key in range(0, 6)}  
    
    for hurricane in hurricanes.values():
        deaths = hurricane["Deaths"]
        
        if deaths == 0:
            mortality_dict[0].append(hurricane)
        elif deaths <= scale[1]:
            mortality_dict[1].append(hurricane)
        elif deaths <= scale[2]:
            mortality_dict[2].append(hurricane)
        elif deaths <= scale[3]:
            mortality_dict[3].append(hurricane)
        elif deaths <= scale[4]:
            mortality_dict[4].append(hurricane)
        else:
            mortality_dict[5].append(hurricane)  # more than 10,000 deaths
    
    return mortality_dict

mortality_ratings = rate_by_mortality(hurricanes, mortality_scale)

for rating, storms in mortality_ratings.items():
    print(f"Mortality Rating {rating}: {len(storms)} hurricanes")

# 8. Calculating Hurricane Maximum Damage

def most_damaging_hurricane(hurricanes):
    max_damage = 0
    most_damaging = ""
    
    for name, data in hurricanes.items():
        damage = data["Damage"]
        
        if damage == "Damages not recorded":
            continue
        
        if damage > max_damage:
            max_damage = damage
            most_damaging = name
    
    return (most_damaging, max_damage)


numeric_damages = updated_damages(damages)

hurricanes = create_hurricane_dict(
    names,
    months,
    years,
    max_sustained_winds,
    areas_affected,
    numeric_damages,  
    deaths
)

most_damaging_name, damage_cost = most_damaging_hurricane(hurricanes)
print(f"The most damaging hurricane was {most_damaging_name}, which caused ${damage_cost:,.0f} in damages.")


# 9. Rating Hurricanes by Damage
damage_scale = {
    0: 0,
    1: 100_000_000,
    2: 1_000_000_000,
    3: 10_000_000_000,
    4: 50_000_000_000
}

def rate_by_damage(hurricanes, scale):
    damage_ratings = {key: [] for key in range(0, 6)} 
    
    for hurricane in hurricanes.values():
        damage = hurricane['Damage']
        
        if damage == "Damages not recorded":
            continue
        
        if damage == 0:
            damage_ratings[0].append(hurricane)
        elif damage <= scale[1]:
            damage_ratings[1].append(hurricane)
        elif damage <= scale[2]:
            damage_ratings[2].append(hurricane)
        elif damage <= scale[3]:
            damage_ratings[3].append(hurricane)
        elif damage <= scale[4]:
            damage_ratings[4].append(hurricane)
        else:
            damage_ratings[5].append(hurricane)  # more than 50B USD
    
    return damage_ratings


damage_ratings_dict = rate_by_damage(hurricanes, damage_scale)

for rating, storms in damage_ratings_dict.items():
    print(f"Damage Rating {rating}: {len(storms)} hurricanes")

