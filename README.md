# stegasaurus
Least Significant bit Steganography.

![Cute Typing Stegosaurus](typing_stegosaurus.png "Cute Typing Stegosaurus")

## Usage
* Requirements: `python3`, `numpy`, `pillow`

* `encode.py [text] [image_file] [output_file]`
  * encodes text into an image a using the LSB method.
  * Ex: `python3 encode.py "Stegosauruses love steganography! :)" typing_stegosaurus.png outputs/typing_stegosaurus_encoded.png`
* `decode.py [image_file] [output_file]`
  * decodes text encoded in an image using the LSB method.
  * Ex: `python3 decode.py outputs/typing_stegosaurus_encoded.png outputs/decoded_text.txt`

## Resources
* Computerphile (Mike Pound): https://www.youtube.com/watch?v=TWEXCYQKyDc&ab_channel=Computerphile
* Stable diffusion: Cute typing stegosaurus
