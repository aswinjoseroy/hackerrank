import datetime

a = "Sun 10 May 2015 13:54:36 -0700"
b = "Sun 10 May 2015 13:54:36 +0000"
t = int(input())

def dt(t1,t2):
	t2 = "Sun 10 Jan 3000 13:54:36 -0700"
	t1 = "Sun 10 May 2015 13:54:36 +0000"
	dt1 = datetime.datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
	dt2 = datetime.datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
	return (dt1-dt2).total_seconds()

timelist= []
for i in range(t*2):
	timelist.append(input())
	
for i in range(len(timelist)):
		if i % 2 == 0:
			print ("{:.0f}".format(abs(dt(timelist[i], timelist[i+1]))))

#print (dt(a,b))