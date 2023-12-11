import gnupg

gnupg = gnupg.GPG(gnupghome="../.gnupg/")
gnupg.encoding = "utf-8"

path = "../raw_data/"
ptext = "input.txt"

stream = open(path + ptext, "rb")

fp = gnupg.list_keys(secret=True).fingerprints[0]

status = gnupg.encrypt_file(
    stream,
    recipients="admin@satrajit.ca",
    sign=fp,
    passphrase="passphrasetest",
    output=f"{path}{ptext}.gpg",
)

print(status.ok)
print(status.status)
print(status.stderr)
