import gnupg
from dotenv import load_dotenv
import os

load_dotenv()

gnupg = gnupg.GPG(gnupghome="../.gnupg/")
gnupg.encoding = "utf-8"

path = "../raw_data/"
ptext = "input.txt.gpg"

stream = open(path + ptext, "rb")

decrypted_data = gnupg.decrypt_file(
    stream,
    passphrase=os.getenv("password"),
    output=f"{path}{ptext}.verified",
)

print(decrypted_data.status)
print(decrypted_data.valid)
