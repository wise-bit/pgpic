import math
from PIL import Image


def pgp_to_hex_visualization(pgp_file_path, output_image_path):
    # Step 1: Read the ASCII-armored PGP public key file
    with open(pgp_file_path, "r") as file:
        pgp_data = file.read()

    start_marker = "-----BEGIN PGP PUBLIC KEY BLOCK-----"
    end_marker = "-----END PGP PUBLIC KEY BLOCK-----"
    start_index = pgp_data.find(start_marker)
    end_index = pgp_data.find(end_marker, start_index + len(start_marker))
    pgp_block = pgp_data[start_index : end_index + len(end_marker)]

    binary_data = bytes.fromhex(pgp_block.encode("utf-8").hex())
    hexcodes = "".join(f"{byte:02x}" for byte in binary_data)

    binary_string = "".join(format(byte, "08b") for byte in binary_data)

    hex_value = ""
    for i in range(0, len(binary_string), 8):
        decimal_data = int(binary_string[i : i + 8], 2)
        hex_value += hex(decimal_data)[2:]

    hex_string = hex_value.zfill((len(hex_value) + 6 - 1) // 6 * 6)
    hex_groups = [hex_string[i : i + 6] for i in range(0, len(hex_string), 6)]

    print(len(hex_groups))

    side_length = math.ceil(math.sqrt(len(hex_groups)))
    image = Image.new("RGB", (side_length, side_length), "white")

    for i, hex_group in enumerate(hex_groups):
        rgb_color = tuple(int(hex_group[i : i + 2], 16) for i in (0, 2, 4))
        image.putpixel((i % side_length, i // side_length), rgb_color)

    upscaled_image = image.resize((image.width * 100, image.height * 100), Image.NEAREST)
    upscaled_image.save("output_image.png")
    # upscaled_image.show()


if __name__ == "__main__":
    pgp_to_hex_visualization("../keys/wisebit.asc", "../keys/wisebit.png")
