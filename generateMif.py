higher_bits_file = 'higher_bits.txt' # create string with ' or ""
lower_bits_file = 'lower_bits.txt'
output_file = 'output.mif'

def signed_decimal_to_14bit_binary(value):
    value = int(value)
    if value < 0:
        value = (1 << 14) + value  # Two's complement for negative numbers
    binary_value = bin(value & 0x3FFF)[2:]  # Ensure it is 14 bits 
    # bin(10) returns 0b1010 with 0b as prefix. [2:] removed this prefix
    return binary_value.zfill(14)  # Pad with leading zeros to ensure 14-bit width (14 characters)

with open(higher_bits_file, 'r') as file: # There is no need to call file.close() and also watch out for exceptions
    higher_bits_lines = file.readlines() 

with open(lower_bits_file, 'r') as file:
    lower_bits_lines = file.readlines()

if len(higher_bits_lines) != 1024 or len(lower_bits_lines) != 1024:
    raise ValueError("Both input files must contain exactly 1024 lines of data each.") # raise or throw a exception

# a special syntax to create a new list from old list:
# [newitem for item in iterable if condition]
# Explain in the hello.py: line 96
higher_bits_data = [signed_decimal_to_14bit_binary(line.strip()) for line in higher_bits_lines] # strip() to remove the whitespacing characters
lower_bits_data = [signed_decimal_to_14bit_binary(line.strip()) for line in lower_bits_lines] # [...] collects the data into a new list

combined_data = [higher + lower for higher, lower in zip(higher_bits_data, lower_bits_data)]

mif_content = [] # create a list
mif_content.append("WIDTH=28;") # append to the existing list
mif_content.append("DEPTH=1024;")
mif_content.append("")
mif_content.append("ADDRESS_RADIX=UNS;")
mif_content.append("DATA_RADIX=BIN;")
mif_content.append("")
mif_content.append("CONTENT BEGIN")

for address, data in enumerate(combined_data): # create a iterator with key(order number) and value
    mif_content.append(f"    {address} : {data};")

mif_content.append("END;")

with open(output_file, 'w') as file:
    file.write('\n'.join(mif_content)) # join all items in the mif_content list with \n as separator 

print(f"MIF file '{output_file}' generated successfully.")
