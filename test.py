# coding=utf-8
import hmac
import hashlib
import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.Hash import MD5

priKey = '''-----BEGIN RSA PRIVATE KEY-----
MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAN8M7oBSoZOzAoxL3tmzku/ZTtQn/BBqfe8jj0GZeFKh0IY8qDpFrNONzxp4S+TH4xCXYyEFkkEIcS9SKMCbqbanxyHnwr66Zu3fFHN2O2qalM97ZrcP3+P3ZGi4h8FZoyB2C+YZka4dR5/FlneuNQXEUQ5bC2/LDYjgMu7x1Q5pAgMBAAECgYAbbaCqgP7DheDLVc0aoj1wZx2NczlI33+K96l3HKMyLhnRWAYr3EOLZEXScHaMtJPUh3k2J1Q70QjyE71VKg8tXwZxOrMeUHpysM282C7AG+ujFxkHjzvr8O7EWe0QKb4IOIQnUeE1tFlxeM78AmO86fWSm3PGoTl2bOcdRs1cAQJBAP2txZ+EvoNnmxQcw0/EEWS1pc2aEGhp61unrSF+ZeG/utZrPMO4dimQKBfDgRqJjXtNPq7pmg90QbUWw1MKXekCQQDhF2ooyHeabn+C0F+QKeT1VPMlRDpjXyBBsM/FXp0aPJinVbMWHBEd1VU8qPmE6CH8wv27XheFBbSfGfDrfFyBAkBkYHouIIxx2nEWiDsQOPjY7Ldqn2eWqTKj1bk/44/Uv9TiOxSULU00LQJwRL+1DHCbNXl0JKL9Mnc9fIBVP2jhAkEAq4sGstIkpKM1tmJLkjj7byUwsOQQg48JrEat8cMrg8VOqaicdWsqeEwPS82TbADldha8/MC2uAAjKWXBwBXlAQJAEoKwjINB77XhjfLzmxnPkgJNV4PVLvKe8dP4TCoNvDU64+buLAmmHakdq2+0C7hKyP/IgUlZ+LW0cn+H2EVX/Q==
-----END RSA PRIVATE KEY-----'''

class transfer:

	def money_format(self, value):
		value = "%.2f" % float(value)
		components = str(value).split('.')
		if len(components) > 1:
			left, right = components
			right = '.' + right
		else:
			left, right = components[0], ''
		result = ''
		while left:
			result = left[-3:] + ',' + result
			left = left[:-3]
		return result.strip(',') + right

	def rounding_up(self, value):
		a = int(value/1)
		b = value%1
		if b > 0:
			a = a + 1
		return a
	
	def sign(self, signdate):
		h=MD5.new(signdate)
		signer = PKCS1_v1_5.new(RSA.importKey(priKey))
		signn = signer.sign(h)
		signn=base64.urlsafe_b64encode(signn)
		return signn
	
class test(transfer):
	pass