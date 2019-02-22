from WeatherSources import Daily, Weekly

print("Daily forecast:", Daily.forecast())
print("Weekly forecast:")
for number, outlook in enumerate(Weekly.forecast(), 1):
    print(number, outlook)
## test