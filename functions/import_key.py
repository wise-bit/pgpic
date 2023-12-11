import gnupg

gpg = gnupg.GPG(gnupghome="../.gnupg/")


def import_key(key_path: str):
    key_data = open(key_path).read()
    import_result = gpg.import_keys(key_data)

    gpg.trust_keys(import_result.fingerprints, "TRUST_ULTIMATE")

    mykeys = gpg.list_keys()
    print(mykeys)
