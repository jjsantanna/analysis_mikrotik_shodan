#!/usr/bin/python3

import sys, getopt
import json, gzip
import smtplib

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
	except getopt.GetoptError:
		print ('test.py -i <inputfile.json.gz>')
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print ('test.py -i <inputfile.json.gz> ')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg

	print ('Input file is "', inputfile)
# ######################################################################
# ######################################################################
	outputfile_name = inputfile.split('.')[0]+'_simplified.json'
	outputfile = open(outputfile_name, 'w')

	data=[]
	for line in gzip.open(inputfile, 'r'):
		loaded_line = json.loads(line)
		try:
			ip = loaded_line['ip_str']
		except:
			ip = ""
		try:
			port = loaded_line['port']
		except:
			port = ""
		try:
			cc = loaded_line['location']['country_code3']
		except:
			cc = ""
		try:
			version = loaded_line['version']
		except:
			version = ""    
		try:
			product = loaded_line['product']
		except:
			product = ""
		    
		json.dump({'ip':ip,'port':port,'cc': cc,'version':version,'product': product}, outputfile)

		outputfile.write("\n")
	outputfile.close()
# ######################################################################
# ######################################################################
	gmail_user = 'jjsantanna.script@gmail.com'
	gmail_password = 'hosRep-tibjiw-xatca2'

	sent_from = gmail_user
	to = ['j.j.santanna@utwente.nl']
	subject = 'Script Ended'
	body = "This is an automatic message!\nHey bitch, the data was simplified!"

	email_text = "From: %s\nTo: %s\nSubject: %s\n\n%s\n" % (sent_from, ", ".join(to), subject, body)

	try:
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		server.sendmail(sent_from, to, email_text)
		server.close()
		print ('Email sent!')
	except:
		print ('Something went wrong...')


if __name__ == "__main__":
   main(sys.argv[1:])