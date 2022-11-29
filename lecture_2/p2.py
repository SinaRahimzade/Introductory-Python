def inch_to_centimeter(inch):
    return round(inch * 2.54, 4)


def centimeter_to_inch(centimeter):
    return round(centimeter / 2.54, 4)


def centimeter_to_foot(centimeter):
    return round(centimeter / 30.48, 4)


def foot_to_centimeter(foot):
    return round(foot * 30.48, 4)


inp = input()
unit = inp.split(" ")[1]
value = float(inp.split(" ")[0])

if unit == "cm":
    print(centimeter_to_inch(value), "inch")
    print(centimeter_to_foot(value), "ft")
if unit == "inch":
    print(inch_to_centimeter(value), "inch")
if unit == "ft":
    print(foot_to_centimeter(value), "ft")
