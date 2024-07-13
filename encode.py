import numpy as np

from PIL import Image
from argparse import ArgumentParser
from pathlib import Path


def parse_args() -> tuple[str, str, str]:
    """Parse args and return text, image_file, and output_file."""
    parser = ArgumentParser()
    parser.add_argument("text", help="Text to be encoded in image.")
    parser.add_argument("image_file", help="Path of image to encode text in.")
    parser.add_argument("output_file", help="Path of output file.")

    args = parser.parse_args()
    return args.text, args.image_file, args.output_file


if __name__ == "__main__":
    text, image_file, output_file = parse_args()

    # Get image as np array.
    image = Image.open(image_file)
    image = np.array(image)

    # Convert message to binary.
    text_bytes = text.encode(encoding="utf-8")
    text_nums = list(text_bytes)

    message_binary = []
    for num in text_nums:
        binary_str = f"{num:08b}"
        message_binary += [int(i) for i in binary_str]

    # Replace least significant bit in image.
    flat_image = image.flat
    for i in range(len(message_binary)):
        bit = message_binary[i]

        if bit == 1:
            flat_image[i] |= 1
        else:
            flat_image[i] = int(flat_image[i]) & ~1

    # Save new image.
    new_image = Image.fromarray(image)
    Path(output_file).parent.mkdir(exist_ok=True)
    new_image.save(output_file)
