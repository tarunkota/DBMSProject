from lxml import html
import requests
import csv


print "Downloading Player Batting Data"

#Variables for data
noOfPages = 48


#Fetching data
for pageNo in range(1,49):

	print "Downloading page no: "+ str(pageNo)
	page = requests.get('http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;page='+str(pageNo)+';template=results;type=batting')
	tree = html.fromstring(page.content)


	names = tree.xpath('//tr[@class="data1"]/td/a/text()')
	teams = tree.xpath('//tr[@class="data1"]/td[1]/text()')
	spans = tree.xpath('//tr[@class="data1"]/td[2]/text()')
	matches = tree.xpath('//tr[@class="data1"]/td[3]/text()')
	inn = tree.xpath('//tr[@class="data1"]/td[4]/text()')
	no = tree.xpath('//tr[@class="data1"]/td[5]/text()')
	runs = tree.xpath('//tr[@class="data1"]/td[6]/b/text()')
	hs = tree.xpath('//tr[@class="data1"]/td[7]/text()')
	ave = tree.xpath('//tr[@class="data1"]/td[8]/text()')
	bf = tree.xpath('//tr[@class="data1"]/td[9]/text()')
	sr = tree.xpath('//tr[@class="data1"]/td[10]/text()')
	hun = tree.xpath('//tr[@class="data1"]/td[11]/text()')
	fif = tree.xpath('//tr[@class="data1"]/td[12]/text()')
	ducks = tree.xpath('//tr[@class="data1"]/td[13]/text()')


	# print "Players: ",names
	# print "Teams:",teams
	# print "spans: ",spans
	# print "matches:",matches
	# print inn
	# print no
	#print runs
	# print hs
	# print ave
	# print bf
	# print sr
	# print hun
	# print fif
	# print ducks

	#Writing data to csv files
	with open('playersBatting.csv', 'a') as csvfile:
	    fieldnames = ['name', 'teams','spanFrom','spanTo','matches','inn','no','runs','hs','ave','bf','sr','hun','fif','ducks']
	    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	    counter =0
	    for name in names:

	    	#span split
	    	spanFrom = spans[counter].split('-')[0]
	    	spanTo  = spans[counter].split('-')[1]
	    	#team split
	    	pteams = teams[counter].replace('(',"").replace(')',"").replace(' ',"").split('/')
	    	for team in pteams:
	    		writer.writerow({'name': names[counter],'teams':team,'spanFrom':spanFrom,'spanTo':spanTo,'matches':matches[counter],'inn':inn[counter],'no':no[counter],'runs':runs[counter],'hs':hs[counter].replace('*',""),'ave':ave[counter],'bf':bf[counter],'sr':sr[counter],'hun':hun[counter],'fif':fif[counter],'ducks':ducks[counter] })	
	    	counter=counter+1
	    
	csvfile.close()


