import pygame
import os

def calculate_total_size():
    total_size = 0
    
    # Calculate size of loaded images
    for image_name in pygame.image.get_extended():
        image = pygame.image.load(image_name)
        size = image.get_size()
        total_size += size[0] * size[1] * image.get_bytesize()
        pygame.image.quit()

    # Calculate size of loaded sounds
    for sound_name in pygame.mixer.music.get_filenames():
        size = os.path.getsize(sound_name)
        total_size += size
        pygame.mixer.quit()

    return total_size

# Example usage
total_size = calculate_total_size()
print(f"Total size of Pygame resources: {total_size} bytes")
