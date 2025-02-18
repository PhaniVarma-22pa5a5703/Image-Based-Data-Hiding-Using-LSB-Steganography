# Image-Based Data Hiding Using LSB Steganography

## Overview
This project is a **GUI-based steganography tool** that enables users to securely hide and extract messages within image files using **Least Significant Bit (LSB) steganography**. It is built using **Python, Tkinter** for the graphical user interface, and the **stegano** library for data embedding.

## Features
- **Open and display image files** (PNG, JPG) for steganographic operations.
- **Hide messages** within images securely using a secret key.
- **Retrieve hidden messages** from an image by entering the correct key.
- **Save modified images** containing hidden data.
- **User-friendly graphical interface** built with Tkinter.

## Technologies Used
- **Python**
- **Tkinter** (for GUI)
- **Pillow (PIL)** (for image processing)
- **stegano** (for LSB-based steganography)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/image-steganography.git
   cd image-steganography
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python Data_Hiding_within_image.py
   ```

## Usage
1. **Open Image**: Select an image file (PNG or JPG) to use for hiding data.
2. **Enter Secret Key**: Type a secret key to secure your hidden message.
3. **Hide Data**: Enter the text message and press "Hide Data" to embed it within the image.
4. **Save Image**: Save the modified image with hidden data.
5. **Retrieve Data**: Load the modified image, enter the correct secret key, and press "Show Data" to extract the hidden message.

## Screenshots
(Add screenshots of the application here)

## License
This project is open-source and available under the **MIT License**.

## Author
Developed by **[Your Name]**.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit pull requests.

## Acknowledgments
- **stegano** library for LSB steganography.
- **Pillow** for image processing.
- **Tkinter** for GUI development.

