from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import connection
from django.db import connections
# Create your views here.

def index(request):
	template = loader.get_template('index.html')
	return HttpResponse("Players Page")


def findBowlers(request):
	template = loader.get_template('findBowlers.html')	
	titles = ('name','team','from','to','matches','inns','balls','runs','wickets','BBI','average','economy','strike rate','4wkts','5wkts')
 	if(request.method=='POST'):
		print request.POST

	#build query
		d = request.POST
		empty=True	
		c = 0
		for key in request.POST:
			if(d[key]!=''):
				c = c+1
		if(c>1):
			empty=False

		r=""
	
		if(d['years1']!=''):
			r = r + " spanfrom >= " + d['years1'] + " AND"
		if(d['years2']!=''):
			r = r + " spanto <= " + d['years2'] + " AND"
	

		if(d['matches1']!=''):
			r = r + " matches >= " + d['matches1'] + " AND"
		if(d['matches2']!=''):
			r = r + " matches <=" + d['matches2'] + " AND"
		
		if(d['inn1']!=''):
			r = r + " inns >= " + d['inn1'] + " AND"
		if(d['inn2']!=''):
			r = r + " inns <= " + d['inn2'] + " AND"

		if(d['balls1']!=''):
			r = r + " bf >= " + d['balls1'] + " AND"
		if(d['balls2']!=''):
			r = r + " bf <= " + d['balls2'] + " AND"

		if(d['runs1']!=''):
			r = r + " runs >= " + d['runs1'] + " AND"
		if(d['runs2']!=''):
			r = r + " runs <= " + d['runs2'] + " AND"

		if(d['wk1']!=''):
			r = r + " wickets >= " + d['wk1'] + " AND"
		if(d['wk2']!=''):
			r = r + " wickets <= " + d['wk2'] + " AND"

		if(d['avg1']!=''):
			r = r + " average >= " + d['avg1'] + " AND"
		if(d['avg2']!=''):
			r = r + " average <= " + d['avg2'] + " AND"
		
		if(d['ec1']!=''):
			r = r + " econ >= " + d['ec1'] + " AND"
		if(d['ec2']!=''):
			r = r + " econ <= " + d['ec2'] + " AND"

		if(d['sr1']!=''):
			r = r + " sr >= " + d['sr1'] + " AND"
		if(d['sr2']!=''):
			r = r + " sr <= " + d['sr2'] + " AND"

		if(d['fours1']!=''):
			r = r + " fours >= " + d['fours1'] + " AND"
		if(d['fours2']!=''):
			r = r + " fours <= " + d['fours2'] + " AND"
		
		if(d['fives1']!=''):
			r = r + " fives >= " + d['fives1'] + " AND"
		if(d['fives2']!=''):
			r = r + " fives <= " + d['fives2'] + " AND"

		with connection.cursor() as cursor:
			try:
				if empty: 
					cursor.execute("SELECT * FROM player_bowling" , [])
				else:
					r = r[:-3]
					print "Query: ",r
					cursor.execute("SELECT * FROM player_bowling where "+r, [])
				rows = cursor.fetchall()
				template = loader.get_template('results.html')
				return HttpResponse(template.render({'rows':rows,'titles':titles}, request))
			except Exception as e:
				print e.message
	return HttpResponse(template.render({}, request))





	
	return HttpResponse(template.render({}, request))


def findBatsman(request):
	template = loader.get_template('findBatsman.html')
	titles = ('Name', 	'Team', 	'From' ,'To' ,'Matches','Innings' ,'Not out' ,'Runs' ,'Highest' ,'Average' ,'Balls faced' ,'Strike rate' ,'100s' ,'50s' ,'0s')
	if(request.method=='POST'):
		print request.POST
		

		#build query
		d = request.POST
		empty=True	
		only1=False
		c = 0

		for key in request.POST:
			if(d[key]!=''):
				c = c+1
		if(c>1):
			empty=False
		if(c==2):
			only1 = True
		r=""
	
		if(d['years1']!=''):
			r = r + " spanfrom >= " + d['years1'] + " AND"
		if(d['years2']!=''):
			r = r + " spanto <= " + d['years2'] + " AND"
	

		if(d['matches1']!=''):
			r = r + " matches >= " + d['matches1'] + " AND"
		if(d['matches2']!=''):
			r = r + " matches <=" + d['matches2'] + " AND"
		

		if(d['nouts1']!=''):
			r = r + " nouts >= " + d['nouts1'] + " AND"
		if(d['nouts2']!=''):
			r = r + " nouts <= " + d['nouts2'] + " AND"
		

		if(d['inn1']!=''):
			r = r + " inns >= " + d['inn1'] + " AND"
		if(d['inn2']!=''):
			r = r + " inns <= " + d['inn2'] + " AND"
		

		if(d['runs1']!=''):
			r = r + " runs >= " + d['runs1'] + " AND"
		if(d['runs2']!=''):
			r = r + " runs <= " + d['runs2'] + " AND"


		if(d['avg1']!=''):
			r = r + " average >= " + d['avg1'] + " AND"
		if(d['avg2']!=''):
			r = r + " average <= " + d['avg2'] + " AND"
		
		if(d['hs1']!=''):
			r = r + " highest >= " + d['hs1'] + " AND"
		if(d['hs2']!=''):
			r = r + " highest <= " + d['hs2'] + " AND"

		if(d['balls1']!=''):
			r = r + " bf >= " + d['balls1'] + " AND"
		if(d['balls2']!=''):
			r = r + " bf <= " + d['balls2'] + " AND"


		if(d['huns1']!=''):
			r = r + " huns >= " + d['huns1'] + " AND"
		if(d['huns2']!=''):
			r = r + " huns <= " + d['huns2'] + " AND"

		if(d['fifs1']!=''):
			r = r + " fifs >= " + d['fifs1'] + " AND"
		if(d['fifs2']!=''):
			r = r + " fifs <= " + d['fifs2'] + " AND"

		if(d['ducks1']!=''):
			r = r + " ducks >= " + d['ducks1'] + " AND"
		if(d['ducks2']!=''):
			r = r + " ducks <= " + d['ducks2'] + " AND"

		if(d['sr1']!=''):
			r = r + " sr >= " + d['sr1'] + " AND"
		if(d['sr2']!=''):
			r = r + " sr <= " + d['sr2'] + " AND"
		

		print "Query: ",r


		#all of them are none
		
		with connection.cursor() as cursor:
			try:
				if empty: 
					cursor.execute("SELECT * FROM player_batting" , [])
				else:
					r = r[:-3]
					print "Query: ",r
					cursor.execute("SELECT * FROM player_batting where "+r, [])
				rows = cursor.fetchall()
				template = loader.get_template('results.html')
				return HttpResponse(template.render({'rows':rows}, request))
			except Exception as e:
				print e.message
		
	return HttpResponse(template.render({}, request))



