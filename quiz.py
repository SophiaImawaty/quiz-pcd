from PIL import Image
import numpy as np
import random

def convert_to_grayscale(image_path):
    image = Image.open(image_path).convert('L')
    return image

def get_image_dimensions(image):
    width, height = image.size
    return width, height

def get_pixel_min_max(image):
    pixel_array = np.array(image)
    pixel_min = np.min(pixel_array)
    pixel_max = np.max(pixel_array)
    return pixel_min, pixel_max

def normalize_image(image):
    image_array = np.array(image)
    normalized_image = image_array / 255.0
    return normalized_image

def flip_image_horizontal(image):
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    return flipped_image

def flip_image_vertical(image):
    flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    return flipped_image

def add_gaussian_noise(image, mean, std_dev):
    image_array = np.array(image)
    noise = np.random.normal(mean, std_dev, image_array.shape)
    noisy_image_array = np.clip(image_array + noise, 0, 255).astype(np.uint8)
    noisy_image = Image.fromarray(noisy_image_array)
    return noisy_image

def add_salt_pepper_noise(image, salt_prob, pepper_prob):
    image_array = np.array(image)
    noisy_image_array = np.copy(image_array)
    num_salt = int(salt_prob * image_array.size)
    salt_coords = [np.random.randint(0, i - 1, num_salt) for i in image_array.shape]
    noisy_image_array[salt_coords] = 255

    num_pepper = int(pepper_prob * image_array.size)
    pepper_coords = [np.random.randint(0, i - 1, num_pepper) for i in image_array.shape]
    noisy_image_array[pepper_coords] = 0

    noisy_image = Image.fromarray(noisy_image_array)
    return noisy_image

# Contoh penggunaan:
input_image_path = "D:\avatar-the-last-airbender-3.png"  # Ganti dengan path gambar input yang sesuai

# 1. Mengonversi gambar ke skala abu-abu
grayscale_image = convert_to_grayscale(input_image_path)

# 2. Mendapatkan dimensi gambar
width, height = get_image_dimensions(grayscale_image)

# 3. Mencari nilai piksel maksimum dan minimum
pixel_min, pixel_max = get_pixel_min_max(grayscale_image)

# 4. Melakukan normalisasi dari rentang 0-255 ke 0-1
normalized_image = normalize_image(grayscale_image)

# 5. Melakukan transformasi geometri: flip horizontal dan flip vertical
flipped_horizontal_image = flip_image_horizontal(grayscale_image)
flipped_vertical_image = flip_image_vertical(grayscale_image)

# 6. Menambahkan noise pada gambar: Gaussian dan Salt Pepper
noisy_gaussian_image = add_gaussian_noise(grayscale_image, mean=0, std_dev=10)
noisy_salt_pepper_image = add_salt_pepper_noise(grayscale_image, salt_prob=0.05, pepper_prob=0.05)
