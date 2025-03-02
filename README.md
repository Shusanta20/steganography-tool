# Steganography Tool

## Description
The **Steganography Tool** is a simple Python application that hides secret messages inside images using **Least Significant Bit (LSB) encoding**. It allows users to **encode** a hidden message inside an image and later **decode** it to retrieve the original text. This tool is useful for secure communication, watermarking, or embedding hidden information inside digital images without visible changes.

## Features
- **Encode a Secret Message** into an image without altering its appearance.
- **Decode a Message** from an encoded image to retrieve hidden text.
- **Works with PNG images** (avoid JPEG due to compression issues).
- **Simple Command-Line Interface (CLI)** for easy usage.

## Technologies Used
- **Python**
- **Pillow (PIL)** - For image processing
- **NumPy** - For efficient pixel manipulation

## Installation
1. Install Python (if not already installed) from [python.org](https://www.python.org/).
2. Install required dependencies using pip:
   ```bash
   pip install pillow numpy
   ```

## Usage
### Encoding a Message
1. Run the script:
   ```bash
   python steganography.py
   ```
2. Choose **Option 1 (Encode)**.
3. Enter the path of the image to encode.
4. Enter the secret message to hide.
5. Provide an output file name (e.g., `output.png`).
6. The encoded image will be saved with the hidden message.

### Decoding a Message
1. Run the script:
   ```bash
   python steganography.py
   ```
2. Choose **Option 2 (Decode)**.
3. Enter the path of the encoded image.
4. The hidden message will be displayed.

## Example
### Encoding
```bash
Do you want to (1) Encode or (2) Decode? Enter 1 or 2: 1
Enter the path of the image to encode: input.png
Enter the secret message to hide: Hello World
Enter the output image path: encoded_image.png
Message successfully encoded!
```

### Decoding
```bash
Do you want to (1) Encode or (2) Decode? Enter 1 or 2: 2
Enter the path of the image to decode: encoded_image.png
Decoded message: Hello World
```

## Notes
- **Use PNG format** to prevent data loss due to compression.
- Make sure to use the **same output file** for decoding.

## Author
Created by Shusanta Bargayary

