import random

def modify_hex_at_position(input_hex, position, max_change_percent):
    # Extract the value to modify
    value_to_modify = input_hex[position:position+8]
    
    # Convert the hex value to an integer
    original_value = int(value_to_modify, 16)
    
    # Calculate the maximum change allowed
    max_change = int(original_value * max_change_percent)
    
    # Generate a random integer within the allowed change range
    random_value = random.randint(original_value - max_change, original_value + max_change)
    
    # Convert the random integer back to a hexadecimal string
    modified_hex = format(random_value, '08x')
    
    # Modify the specified positions in the output hex
    output_hex = input_hex[:position] + modified_hex + input_hex[position+8:]
    
    return output_hex

# Example usage
input_hex = "0100000099085504fbcf0446f8ff474435b59f45eb06b2406c66463c44bb94be00bda13c687a1e3eea5caa41484d15bc18a1273eb3d2d3bc6c6181be015d83bc741c923becd6013fb362bd3ed940f53ec9c1c03eb558f839f58b9ab94e4bf53b8c2d3f3c65427842c9f574428d1e6e426f2f6b42000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c0ac9c3de6fa543dedc7db3d0eb0283d85ad9c3dc6fb543da550dc3dee532f3d88e1b13b405e01bb10104a3b20e52abbdf0e0000060000008403000001000000060000003d27f943657a99bf4ab28cc1165eaa41ef680846d1778241adb86043e12f5c43e47b6843e47b6843cc0f29c10000803f513c574500000000000000005fdbb742b6f4de420000012b00000002037f00000000000000000000000000000000006e000000"
position = 33  # Modify positions 33 to 41
max_change_percent = 0.05
output_hex = modify_hex_at_position(input_hex, position, max_change_percent)
print(output_hex)
input_hex = output_hex
output_hex = modify_hex_at_position(input_hex, position, max_change_percent)
print(output_hex)
output_hex = modify_hex_at_position(input_hex, position, max_change_percent)
print(output_hex)
input_hex = output_hex
output_hex = modify_hex_at_position(input_hex, position, max_change_percent)
print(output_hex)
output_hex = modify_hex_at_position(input_hex, position, max_change_percent)
print(output_hex)
input_hex = output_hex
output_hex = modify_hex_at_position(input_hex, position, max_change_percent)
print(output_hex)
