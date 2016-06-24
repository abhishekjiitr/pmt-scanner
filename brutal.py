import requests, webbrowser
from bs4 import BeautifulSoup
import mysql.connector
cnx = mysql.connector.connect(user='root', password='abhi2254015', host='127.0.0.1', database='results')
cursor = cnx.cursor(buffered=True)


def query(rollno="123456", name="Default", father="Default Father", dob="DOB", total="0", rank="999999"):
	global cursor
	global cnx
	check = ("SELECT name FROM pmt WHERE rollno='%s'")
	data = (rollno)
	cursor.execute(check, data)
	try:
		entry = ("INSERT INTO pmt "
	               "(rollno, name, father, dob, total_percentile, rank)"
	               "VALUES (%s, %s, %s, %s, %s, %s)");
		data = (rollno, name, father, dob, total, rank)
		cursor.execute(entry, data)
		cnx.commit()
		print("%s (%s) is being added to database. :)" % (name, rollno))
	except Exception as e:
		# print(str(e))
		print("%s (%s) already added to database. :)" % (name, rollno))
	
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
	# print(soup.prettify())
	name = "NO ONE"
	father="EDDARD STARK"
	DOB="1000 BC"
	rank="999999999"
	percent = "0"
	if soup.font.text != ' Invalid Roll No.':
		# print("YOHOOO " + roll)
		info = [ str(part.string) for part in soup.find_all('font') ]
		
		for i in range(len(info)):
			x = info[i]
			# print("$"+str(x)+"$")

			if x == "Name":
				name = info[i+1].strip()
				# print(name)
			elif x == "Father's Name":
				father = info[i+1].strip()
				# print(father)
			elif x == "DOB":
				DOB = info[i+1].strip()
				# print(DOB)
			elif x == "Open Merit No.":
				rank = info[i+1].strip()
				# print(rank)
			elif x == "Total Percentile ":
				percent = info[i+1].strip()
				# print(percent)
				break
		query(roll, name, father, DOB, percent, rank)
	else:
		print("Failed to add: "+roll + " :(")
	# print(soup.font1e0xt == )
# for i in range(900000, 920000):
# 		getresult(str(i+j))
getresult('900001')