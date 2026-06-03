from PIL import Image

def encrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y][:3]

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[x, y] = (r, g, b)

    img.save(output_image)
    print(f"Encrypted image saved as {output_image}")


def decrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y][:3]

            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[x, y] = (r, g, b)

    img.save(output_image)
    print(f"Decrypted image saved as {output_image}")


def main():
    print("Image Encryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")

    choice = input("Enter choice (1/2): ")

    image_path = input("Enter image path: ")
    output_path = input("Enter output image path: ")
    key = int(input("Enter secret key (0-255): "))

    if choice == "1":
        encrypt_image(image_path, output_path, key)
    elif choice == "2":
        decrypt_image(image_path, output_path, key)
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()