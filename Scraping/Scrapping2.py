from lxml import html
import requests
import csv


print "Downloading Player Bowling Data"

#Variables for data
noOfPages = 48


#Fetching data
for pageNo in range(1,49):

	print "Downloading page no: "+ str(pageNo)
	page = requests.get('http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;page='+str(pageNo)+';template=results;type=bowling')
	tree = html.fromstring(page.content)


	names = tree.xpath('//tr[@class="data1"]/td/a/text()')
	teams = tree.xpath('//tr[@class="data1"]/td[1]/text()')
	spans = tree.xpath('//tr[@class="data1"]/td[2]/text()')
	matches = tree.xpath('//tr[@class="data1"]/td[3]/text()')
	inn = tree.xpath('//tr[@class="data1"]/td[4]/text()')
	balls = tree.xpath('//tr[@class="data1"]/td[5]/text()')
	runs = tree.xpath('//tr[@class="data1"]/td[6]/text()')
	wkts = tree.xpath('//tr[@class="data1"]/td[7]/b/text()')
	bbi = tree.xpath('//tr[@class="data1"]/td[8]/text()')
	ave = tree.xpath('//tr[@class="data1"]/td[9]/text()')
	econ = tree.xpath('//tr[@class="data1"]/td[10]/text()')
	sr = tree.xpath('//tr[@class="data1"]/td[11]/text()')
	fours = tree.xpath('//tr[@class="data1"]/td[12]/text()')
	fives = tree.xpath('//tr[@class="data1"]/td[13]/text()')


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
	with open('playersBowling.csv', 'a') as csvfile:
	    fieldnames = ['name', 'teams','spanFrom','spanTo','matches','inn','balls','runs','wkts','bbi','ave','econ','sr','fours','fives']
	    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	    counter =0
	    for name in names:

	    	#span split
	    	spanFrom = spans[counter].split('-')[0]
	    	spanTo  = spans[counter].split('-')[1]
	    	#team split
	    	pteams = teams[counter].replace('(',"").replace(')',"").replace(' ',"").split('/')
	    	for team in pteams:
	    		writer.writerow({'name': names[counter],'teams':team,'spanFrom':spanFrom,'spanTo':spanTo,'matches':matches[counter],'inn':inn[counter],'balls':balls[counter],'runs':runs[counter],'wkts':wkts[counter],'bbi':bbi[counter],'ave':ave[counter],'econ':econ[counter],'sr':sr[counter],'fours':fours[counter],'fives':fives[counter] })	
	    	counter=counter+1
	    
	csvfile.close()


