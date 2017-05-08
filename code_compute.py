import tweepy
import urllib
import os
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_api(cfg):
        auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
        auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
        return tweepy.API(auth)

#YOU SHOULD PUT YOUR OWN TWITTER CREDENTIALS HERE 
#Sending tweet
def tweeter(message):
        cfg = {
            "consumer_key"        : "",
            "consumer_secret"     : "",
            "access_token"        : "",
            "access_token_secret" : ""
            }

        api = get_api(cfg)
        tweet = message
        status = api.update_status(status=tweet)

#This function will count the number of line of the file
def blocks(files, size=65536):
    while True:
        b = files.read(size)
        if not b: break
        yield b

	
	
def find_line(file,date_wanted):
	for line in f:
		date_unix=line.split(",")[0]
		if ((int(date_unix)-int(date_wanted))<(60*60) and (int(date_unix)-int(date_wanted))>0) or ((int(date_unix)-int(date_wanted))>(60*60) and (int(date_unix)-int(date_wanted))<0):
			print "I found the line !"	
			print line
			return line
				
				
				
				
f=open("krakenEUR.csv","r")
number_lines=sum(bl.count("\n") for bl in blocks(f))
one_yr_ago = datetime.now() - relativedelta(years=1)
timestamp = (one_yr_ago - datetime(1970, 1, 1)).total_seconds()
f=open("krakenEUR.csv","r")
#line_wanted=find_line(f,number_lines,timestamp)
line_wanted=find_line(f,timestamp)
old_price_btc=line_wanted.split(",")[1]
old_price_100=float(100)/float(old_price_btc) #Compute the bitcoins for 100 euros spent
f=open("krakenEUR.csv","r")
full=f.readlines()
new_price_btc=float(str(full[number_lines-1]).split(",")[1])*old_price_100
diff_price=float(new_price_btc)-float(100)
if diff_price<0:
	status="Having bought for 100 euros of Bitcoin one year ago, you would have made a depreciation of "+str(diff_price)+" euros"
else:
	status="Having bought for 100 euros of Bitcoin one year ago, you would have made a capital gain of "+str(diff_price)+" euros"
tweeter(status)	
