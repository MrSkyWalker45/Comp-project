import json

datafile = "places.json"
global d
d = {	"Blr-Mum":900,"Blr-Del":2000,"Blr-Klt":1800,"Blr-Hyd":500,
		"Mum-Del":1200,"Mum-Klt":1700,"Mum-Hyd":700,"Del-Klt":1300,
		"Del-Hyd":1400,"Klt-Hyd":1500,"Mum-Blr":900,
		"Del-Blr":2000,"Klt-Blr":1800,"Hyd-Blr":500,
		"Del-Mum":1200,"Klt-Mum":1700,"Hyd-Mum":700,"Klt-Del":1300,
		"Hyd-Del":1400,"Hyd-Klt":1500,
}



# def test_read(n,k):
	d[n] += k
	return d 
	
	