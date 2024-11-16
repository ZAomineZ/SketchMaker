import cv2
import matplotlib.pyplot as plt

plt.style.use('ggplot')


def load_and_convert_image(filepath):
    """Load an image and convert it to RGB."""
    img = cv2.imread(filepath)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def display_image(image, title, cmap=None):
    """Display an image with a title and optional colormap."""
    plt.figure(figsize=(8, 8))
    plt.imshow(image, cmap=cmap)
    plt.axis("off")
    plt.title(title)


def save_image(image, output_path):
    """Save an image to the specified file path."""
    cv2.imwrite(output_path, image)


def process_image(filepath, output_path):
    """Process the image to create a sketch effect."""
    # Load and convert the image
    img_rgb = load_and_convert_image(filepath)
    display_image(img_rgb, "Original Image")

    # Convert to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    display_image(img_gray, "GrayScale Image", cmap="gray")

    # Invert the grayscale image
    img_invert = cv2.bitwise_not(img_gray)
    display_image(img_invert, "Inverted Image", cmap="gray")

    # Apply Gaussian blur to the inverted image
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX=0, sigmaY=0)
    display_image(img_smoothing, "Smoothened Image", cmap="gray")

    # Create the final sketch effect
    final_sketch = cv2.divide(img_gray, 255 - img_smoothing, scale=255)
    display_image(final_sketch, "Final Sketch Image", cmap="gray")

    # Save the final sketch image
    save_image(final_sketch, output_path)
    print(f"Final sketch saved to {output_path}")


def main():
    """Main function to process the image."""
    filepath = 'test.jpeg'  # Replace with your image path
    process_image(filepath, "test_coloring.jpeg")
    plt.show()


if __name__ == "__main__":
    main()
