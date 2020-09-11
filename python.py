import socket, sys, os, requests

number = 1
linenumber = 0
i = 1
while True:
	with open("proxies.txt") as file_in:
		lines = []
		for line in file_in:
			lines.append("https://" + line)
	proxy = {"https" : lines[linenumber]}
	print(proxy)
	print("Essaie n.{0}".format(number))
	while i < 25:
		try:
			req=requests.get("https://leposteurip.000webhostapp.com", proxies=proxy)
			print("Essai n.{0}", format(i))
			print("Proxy : " + lines[linenumber])
			print("Succes")
		except:
			print("Erreur !")


		print("Changement de proxy")
		if linenumber == 196:
			linenumber = 0
			print(linenumber)
		else:
			linenumber += 1
			number += 1
			print(linenumber)
		print("Next... ;)")
