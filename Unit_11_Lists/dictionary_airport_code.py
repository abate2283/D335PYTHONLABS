airport_codes = {
    'New York': 'JFK',
    'Tokyo': 'NRT',
    'Vancouver': 'YVR',
    'Minneapolis': 'MSP',
    'London': 'LHR'
}

new_airport_codes = {
    'San Jose': 'SJC',
    'Austin': 'AUS',
    'Tokyo': 'HND'
}

print(airport_codes.get('Tokyo', 'na'))
print(airport_codes.get('San Jose', 'na'))
airport_codes.update(new_airport_codes)
print(airport_codes.get('Tokyo', 'na'))
print(airport_codes.get('San Jose', 'na'))