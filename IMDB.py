#IMDB - Coded by batman1721 @ https://github.com/batman1721

import csv #Built-in module at least in >2.7 Python versions

min_voters=50000 #Minumum voters
min_rating=8 #Minimum Avg. Rating
year=2017 #Lower limit for start year
l_year=2018 #Upper limit for start year
tipo='tvSeries' #Type of title
#movie
#tvSeries
#short
#tvEpisode
#tvMovie
ad='0' #Adult title set to 1, Non-Adult set to 0
genero='' #Genre
#Comedy
#Drama
#Action
#Romance
#Terror
#Thriller
#Crime
#Sci-Fi


rat=[]
#Swap path to your own
with open('C:/title.ratings.tsv/data.tsv') as f:
    reader = csv.reader(f,delimiter='\t')
    for row in reader:
      try:
        if int(row[2])>min_voters and float(row[1])>min_rating:
            rat.append(row)
      except:
        rat.append(row)

names=[]
idd=[]
#Swap path to your own
with open('C:/title.basics.tsv/data.tsv') as f2:
  reader = csv.reader(f2,delimiter='\t')
  for row in reader:
    names.append(row)
    idd.append(row[0])
n=0
for i in xrange(len(rat)):
  indice=idd.index(rat[i][0])
  if names[indice][1]==tipo and names[indice][4]==ad and int(names[indice][5])>=year and (int(names[indice][5])<=l_year or names[indice][5]=='') and ((genero in names[indice][8])==True or genero==''):
    print 'id='+rat[i][0] +' '+ names[indice][2] +' Rating='+ rat[i][1] +' Voters='+ rat[i][2]+ ' '+names[indice][8] +' '+names[indice][5]
    n+=1

print n
