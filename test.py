from PIL import Image, ImageOps
import os

# Define the folder containing the icons
icon_folder = "C:/Users/Kent/Documents/weather project/icons/"
output_folder = "C:/Users/Kent/Documents/weather project/icons/black_background/"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Function to replace white color with black
def replace_white_with_black(image):
    # Convert image to RGBA (if not already in this mode)
    image = image.convert("RGBA")

    # Get data of image
    data = image.getdata()

    # Create a new list of data with white replaced by black
    new_data = []
    for item in data:
        # Change all white (also shades of whites)
        # (255, 255, 255, 255) to (0, 0, 0, 255)
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            new_data.append((0, 0, 0, item[3]))  # Change white to black
        else:
            new_data.append(item)  # Keep the original color

    # Update image data with the new data
    image.putdata(new_data)
    return image

# Loop through each file in the icon folder
for filename in os.listdir(icon_folder):
    if filename.lower().endswith(('.png', '.jpeg', '.jpg')):  # Check for image files
        # Open the image
        img = Image.open(os.path.join(icon_folder, filename))

        # Replace white with black
        img = replace_white_with_black(img)

        # Check the file extension to decide how to save the image
        if filename.lower().endswith('.png'):
            img.save(os.path.join(output_folder, filename), format="PNG")
        else:  # For JPEG files
            img = img.convert("RGB")  # Convert to RGB mode
            img.save(os.path.join(output_folder, filename), format="JPEG")

print("All icons have been processed and saved with white replaced by black.")
