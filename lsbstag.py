from PIL import Image


def encode_image(image_path, message, output_path):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    message += "###"  
    data_index = 0
    binary_message = ''.join([format(ord(i), "08b") for i in message])
    msg_len = len(binary_message)
    
    for y in range(height):
        for x in range(width):
            pixel = list(img.getpixel((x, y)))
            for n in range(3):  # R, G, B
                if data_index < msg_len:
                    pixel[n] = pixel[n] & ~1 | int(binary_message[data_index])
                    data_index += 1
            encoded.putpixel((x, y), tuple(pixel))
            if data_index >= msg_len:
                break
        if data_index >= msg_len:
            break
    
    encoded.save(output_path)
    print(" Message encoded successfully into", output_path)



def decode_image(encoded_path):
    img = Image.open(encoded_path)
    binary_data = ""
    
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.getpixel((x, y))
            for n in range(3):
                binary_data += str(pixel[n] & 1)
    
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded = ""
    for byte in all_bytes:
        decoded += chr(int(byte, 2))
        if decoded[-3:] == "###":
            break
    return decoded[:-3]



original_image = r"c:\Users\deept\OneDrive\Pictures\ludemeula-fernandes-9UUoGaaHtNE-unsplash.jpg"  # your input image
encoded_image = "encoded.png"
secret_message = "This is a secret message!"

encode_image(original_image, secret_message, encoded_image)
decoded_message = decode_image(encoded_image)
print(" Decoded message:", decoded_message)
