from PIL import Image
import numpy as np

def encode_image(image_path, secret_data, output_image_path):
    try:
        # Open the image and convert to RGB
        image = Image.open(image_path)
        image = image.convert('RGB')
        pixels = np.array(image, dtype=np.uint8)  # Ensure uint8 format

        # Convert secret data to binary
        secret_data = ''.join(format(ord(char), '08b') for char in secret_data)
        secret_data += '1111111111111110'  # Delimiter to mark the end

        # Check if the data can fit in the image
        data_len = len(secret_data)
        max_capacity = pixels.shape[0] * pixels.shape[1] * 3  # Each pixel has 3 color channels
        if data_len > max_capacity:
            raise ValueError("Data too large to fit in the image!")

        # Embed the data into the image
        data_index = 0
        for row in range(pixels.shape[0]):
            for col in range(pixels.shape[1]):
                for color in range(3):  # RGB channels
                    if data_index < data_len:
                        # Modify the LSB of the pixel while ensuring uint8 range
                        new_value = (int(pixels[row, col, color]) & ~1) | int(secret_data[data_index])
                        pixels[row, col, color] = np.uint8(np.clip(new_value, 0, 255))  # Ensure within range
                        data_index += 1
                    else:
                        break  # Stop modifying pixels once data is fully embedded

        # Convert back to uint8 before saving
        pixels = pixels.astype(np.uint8)

        # Save the modified image
        encoded_image = Image.fromarray(pixels)
        encoded_image.save(output_image_path)
        print(f"Data encoded and saved to {output_image_path}")

    except Exception as e:
        print(f"Error during encoding: {e}")

def decode_image(image_path):
    try:
        # Open the image and convert to RGB
        image = Image.open(image_path)
        image = image.convert('RGB')
        pixels = np.array(image, dtype=np.uint8)

        # Extract the LSBs from the image
        binary_data = ''
        for row in range(pixels.shape[0]):
            for col in range(pixels.shape[1]):
                for color in range(3):  # RGB channels
                    binary_data += str(pixels[row, col, color] & 1)

        # Find the delimiter '1111111111111110' and extract the message
        delimiter = '1111111111111110'
        end_index = binary_data.find(delimiter)
        if end_index == -1:
            return "No hidden message found."

        # Convert binary data into text
        all_bytes = [binary_data[i:i+8] for i in range(0, end_index, 8)]
        decoded_data = ''.join(chr(int(byte, 2)) for byte in all_bytes)

        return decoded_data

    except Exception as e:
        return f"Error during decoding: {e}"

def main():
    print("Welcome to Steganography Tool!")
    choice = input("Do you want to (1) Encode or (2) Decode? Enter 1 or 2: ")

    if choice == '1':
        # Encoding
        image_path = input("Enter the path of the image to encode: ").strip('"')
        secret_message = input("Enter the secret message to hide: ")
        output_image_path = input("Enter the output image path (e.g., output.png): ").strip('"')

        try:
            encode_image(image_path, secret_message, output_image_path)
            print("Message successfully encoded!")
        except Exception as e:
            print(f"Error: {e}")

    elif choice == '2':
        # Decoding
        image_path = input("Enter the path of the image to decode: ").strip('"')
        try:
            decoded_message = decode_image(image_path)
            print(f"Decoded message: {decoded_message}")
        except Exception as e:
            print(f"Error: {e}")

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
