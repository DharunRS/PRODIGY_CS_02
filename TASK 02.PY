from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    image = image.convert("RGB")
    pixels = np.array(image)

    # Encrypt the image by adding the key to each pixel value
    encrypted_pixels = (pixels + key) % 256
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    image = image.convert("RGB")
    pixels = np.array(image)

    # Decrypt the image by subtracting the key from each pixel value
    decrypted_pixels = (pixels - key) % 256
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Decrypted image saved as {output_path}")

if __name__  == "__main__":
    key = 50  # Example key for encryption/decryption

    encrypt_image("input_image.jpg", "encrypted_image.jpg", key)
    decrypt_image("encrypted_image.jpg", "decrypted_image.jpg", key)