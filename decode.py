import numpy as np

from PIL import Image
from argparse import ArgumentParser


def parse_args() -> tuple[str, str]:
    """Parse args and return image_file and output_file."""
    parser = ArgumentParser()
    parser.add_argument("image_file", help="Path of image with encoded text.")
    parser.add_argument("output_file", help="Path of file to write text to.")

    args = parser.parse_args()
    return args.image_file, args.output_file


if __name__ == "__main__":
    image_file, output_file = parse_args()

    # Get image as np array.
    image = Image.open(image_file)
    image = np.array(image)

    # Get least significant bits.
    bits = []
    for num in image.flat:
        bits += [int(i) for i in f"{num:08b}"[-1:]]

    # Convert bits into bytes and then chars.
    chars = []
    for i in range(0, len(bits), 8):
        if (i + 8) > len(bits):
            break

        byte = "".join([str(j) for j in bits[i : i + 8]])
        char = chr(int(byte, base=2))
        chars.append(char)

    text = "".join(chars)
    with open(output_file, mode="w") as f:
        f.write(text)
        f.write("\n")
