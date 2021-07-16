# convert decimal color code to hexadecimal 
def to_hex(d):
    hex_int1 = d//16
    hex_rem1 = d%16
    hex_rem2 = hex_int1%16

    hex_dictionary = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", \
        10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}

    hex_code = "{0}{1}".format(hex_dictionary[hex_rem2], hex_dictionary[hex_rem1])
    return hex_code

# convert rgb to hexadecimal
def hex_color(red, green, blue):
    print("#{0}{1}{2}".format(to_hex(red), to_hex(green), to_hex(blue)))

hex_color(10, 32, 255)