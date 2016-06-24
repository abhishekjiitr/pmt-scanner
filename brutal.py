import requests, webbrowser
from bs4 import BeautifulSoup
import mysql.connector
cnx = mysql.connector.connect(user='root', password='abhi2254015', host='127.0.0.1', database='results')
cursor = cnx.cursor()

print(cursor)
# url = 'www.google.com'

def query(rollno="123456", name="Default", father="Default Father", dob="DOB", total="0", rank="999999"):
	global cursor
	global cnx
	entry = ("INSERT INTO pmt "
               "(rollno, name, father, dob, total_percentile, rank)"
               "VALUES (%s, %s, %s, %s, %s, %s)");
	data = (rollno, name, father, dob, total, rank)
	cursor.execute(entry, data)
	cnx.commit()
# query()	

def getresult(roll):
	payload = {'rollno': roll}
	headers = {
	    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
	}
	url = 'http://bfuhs.ac.in/Resultpmt16/pmtsearch.asp'
	r = requests.post(url, headers=headers, data=payload)
	resp = r.text
	soup = BeautifulSoup(resp, 'html.parser')
	print(soup.prettify())

	if soup.font.text != ' Invalid Roll No.':
		print("YOHOOO " + roll)
		filter1 = soup.find_all('font')
		for i in range(len(filter1)):
			x = filter1[i].string
			print("$"+str(x)+"$")
		# webbrowser.open('result.html')
	else:
		print("Failed: "+roll)
	# print(soup.font1e0xt == )
# for i in range(900000, 920000):
		# getresult(str(i+j))
getresult('900001')