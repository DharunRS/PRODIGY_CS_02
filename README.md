This Python script demonstrates image encryption and decryption using a simple technique of adding and subtracting a key value from each pixel in the image:

1. The encrypt_image() function takes an input image path, output image path, and a key as input. It opens the input image, converts it to RGB mode, and converts the image data into a NumPy array. Then, it adds the key value to each pixel value, ensuring that the result stays within the range of 0 to 255 (8-bit color range). The resulting encrypted pixel values are saved as a new image.

2. The decrypt_image() function is similar but performs the inverse operation. It subtracts the key value from each pixel value to decrypt the image.

3. In the main block, a key value is defined, and the encrypt_image() function is called to encrypt the input image. Then, the decrypt_image() function is called to decrypt the encrypted image back to its original form.

Users can replace "input_image.jpg" with the path to their desired input image and specify the desired output paths for the encrypted and decrypted images. They can also adjust the key value to customize the encryption/decryption process.
