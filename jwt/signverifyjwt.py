# https://blog.miguelgrinberg.com/post/json-web-tokens-with-public-key-signatures
# -------------------------------------------------------------------------------
# require pyjwt
# require cryptography
# ssh-keygen -t rsa -b 4096
import jwt

# sign
payload = {'name': 'pippo'}
private_key = open('id_rsa').read()
algorithm = 'RS256'
token = jwt.encode(payload, private_key, algorithm).decode('utf-8')

print(token)

# verify
public_key = open('id_rsa.pub').read()
algorithms = ['RS256']
payload_decoded = jwt.decode(token, public_key, algorithms)
print(payload_decoded)