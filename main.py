import numpy as np

from PIL import Image


# Get image as np array.
image = Image.open("karpathy.jpg")
image = np.array(image)

print(image.shape)
print(image.max(), image.min())
print(image.dtype)

print(image.flat[:10])
print([bin(i) for i in image.flat[:10]])

# Convert message to binary.
message = "I love Andrej Karpathy."
message_bytes = message.encode(encoding="utf-8")
message_nums = list(message_bytes)

message_binary = []
for num in message_nums:
    binary_str = f"{num:08b}"
    message_binary += [int(i) for i in binary_str]
print(message_binary)

# Replace least significant bit in image.
flat_image = image.flat
for i in range(len(message_binary)):
    bit = message_binary[i]

    if bit == 1:
        flat_image[i] |= 1
    else:
        flat_image[i] = int(flat_image[i]) & ~1

print(image.flat[:10])
print([bin(i) for i in image.flat[:10]])

# Save new image.
new_image = Image.fromarray(image)
new_image.save("karpathy_message.jpg")
