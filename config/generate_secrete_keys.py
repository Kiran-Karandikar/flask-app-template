"""
Generate CSRF and Session keys, output to secret_keys.py file.
Outputs secret_keys.py file in current folder
"""
import os.path
import string
# Python Modules
from random import choice
from string import Template

# 3rd Party Modules
# -N/A

# Project Modules
# -N/A

# Global Vars
# File settings
APP_SECRETS = """# CSRF and Session keys
CSRF_SECRET_KEY = '$csrf_key'
SESSION_KEY = '$session_key'"""
FILE_NAME = 'secret_keys.py'
FILE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), FILE_NAME)
FILE_TEMPLATE = Template(APP_SECRETS)


def generate_random_key(length):
	"""
	Generate random key, given a number of characters

	Args:
		length: length of secret key.

	Returns: type:str : Secret key of `length` random characters.
	"""
	chars = string.letters + string.digits
	return ''.join([choice(chars) for i in range(int(length))])


def write_file(contents):
	"""
	Writes the `contents` to the file `FILE_PATH`.

	Args:
		contents: File contents to be written.
	"""
	with open(FILE_PATH, 'wb') as f:
		f.write(contents)


def generate_keyfile(length=50, force_generate=False):
	"""
	Generate random key, given a number of characters

	Args:
		length: length of secret key, default: 50.
		force_generate:
			Overwrite the existing secret_keys.py file with new secret keys.
			Dealt: False.
	"""
	csrf_key = generate_random_key(length)
	session_key = generate_random_key(length)
	output = FILE_TEMPLATE.safe_substitute(
		dict(csrf_key=csrf_key, session_key=session_key)
	)
	if os.path.exists(FILE_PATH):
		if not force_generate:
			raise IOError(
				"Warning: secret_keys.py file exists.  Use `force_generate` "
				"to force overwrite."
			)
		else:
			write_file(output)
	else:
		write_file(output)


if __name__ == '__main__':
	generate_keyfile(force_generate=True)
