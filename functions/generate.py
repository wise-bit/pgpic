import gnupg


def generate_gpg_keys(
    email, passphrase, keyname, key_type="RSA", key_length=2048, gnupghome="../.gnupg/"
):
    gpg = gnupg.GPG(gnupghome=gnupghome)
    gpg.encoding = "utf-8"

    # Generate key input
    input_data = gpg.gen_key_input(
        name_email=email,
        passphrase=passphrase,
        key_type=key_type,
        key_length=key_length,
    )

    try:
        key = gpg.gen_key(input_data)

        if key:
            print("Key generation successful:")
            print(key)

            public_key = gpg.export_keys(str(key))
            with open(f"keys/{keyname}.asc", "w") as f:
                f.write(public_key)

        else:
            print("Key generation failed. No key returned.")

    except Exception as e:
        print("An error occurred:", e)
