import gnupg

gpg = gnupg.GPG(gnupghome="../.gnupg/")


def encrypt(ptfile, path="raw_data/"):
    with open(path + ptfile, "rb") as f:
        status = gpg.encrypt_file(
            fileobj_or_path=f,
            recipients=["admin@satrajit.ca"],
            output=path + ptfile + ".encrypted",
        )

    print(status.ok)
    print(status.stderr)


def decrypt(ptfile, path="raw_data/"):
    with open(path + ptfile, "rb") as f:
        status = gpg.decrypt_file(
            fileobj_or_path=f,
            passphrase="passphrasetest",
            output=path + ptfile + ".encrypted",
        )

    print(status.ok)
    print(status.stderr)


if __name__ == "__main__":
    # encrypt(ptfile="input.txt")
    decrypt(ptfile="input.txt.encrypted")

    pass
