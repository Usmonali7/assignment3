def replace_value(values, index, new_value):
    values[index] = new_value


def find_first(values, target):
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1


def summarize(values):
    stats_record = (min(values), max(values), sum(values))
    return stats_record


days = int(input("Enter the number of days: "))
original = []

for day in range(days):
    water_use = int(input("Enter water use in litres: "))
    original.append(water_use)

updated = original[:]

index = int(input("Enter the index to correct: "))
new_value = int(input("Enter the new water use: "))
replace_value(updated, index, new_value)

target = int(input("Enter the water use to search for: "))

first_index = find_first(updated, target)
matching_count = updated.count(target)

stats_record = summarize(updated)
minimum, maximum, total = stats_record

sorted_values = sorted(updated)

print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_values}")
print(f"Minimum water use: {minimum} litres")
print(f"Maximum water use: {maximum} litres")
print(f"Total water use: {total} litres")

if first_index == -1:
    print("Target not found")
else:
    print(f"First matching index: {first_index}")

print(f"Matching values: {matching_count}")