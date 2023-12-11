from dotenv import dotenv_values

from functions.generate import generate_gpg_keys
from functions.import_key import import_key


if __name__ == "__main__":
    config = dotenv_values(".env")

    email = "admin@satrajit.ca"
    passphrase = config.get("password")
    keyname = config.get("keyname")

    # generate_gpg_keys(email, passphrase, keyname)
    import_key(f"keys/{keyname}.asc")
