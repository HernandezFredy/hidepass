#!/usr/bin/python3
import sys
import os

try:
	from .getput import getchar,putchar
except ImportError:
	import msvcrt

def hidepass(prompt = "", replaceChar = "*"):

	password = ""
	count = 0
	backspace = chr(127)

	for i in prompt:
		if os.name == "posix":
			putchar(i)

		elif os.name == "nt" or os.name == "dos":
			msvcrt.putwch(i)

	while True:

		if  os.name == "posix":
			captureKey = getchar()

		elif os.name == "nt" or os.name == "dos":
			captureKey = msvcrt.getwch()


		if captureKey == "\n" or captureKey == "\r":
			break

		if captureKey == "\b" or captureKey == backspace:
			password = password [ :-1 ]
			count -= 1

			if count >= 0:
				if os.name == "posix":
					putchar("\b")
					putchar(" ")
					putchar("\b")
				elif os.name == "nt" or os.name == "dos":
					msvcrt.putwch("\b")
					msvcrt.putwch(" ")
					msvcrt.putwch("\b")

		else:
			if count <= 0:
				count = 0

			password += captureKey
			count += 1

			if os.name == "posix":
				putchar(replaceChar)

			elif os.name == "nt" or os.name == "dos":
				msvcrt.putwch(replaceChar)


	print("\n")
	return password if password != "" else None

if __name__ == '__main__':
	pswd = hidepass("Passsword: ")
	print("The password is: ",pswd)
