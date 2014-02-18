from bs4 import BeautifulSoup
import urllib2
import time

RETRY_TIME = 20.0


def main():
	
	hashtag = "#nfl"
	hashtag = hashtag.strip('#')

	link = "http://www.hashtags.org/analytics/"+ hashtag + "/"
	
	while True:
	    try:
	    	f = urllib2.urlopen(link)
	        break
	    except urllib2.HTTPError:
	        time.sleep(RETRY_TIME)
	        pass

	soup = BeautifulSoup((f.read()))

	getDivs = soup.find_all('div')

	for s in getDivs:
		
		definition = s.getText().strip('\t\n ').encode('utf8')
		
		if 'definition' in str(s.get('id')):
			print definition


if __name__ == '__main__':
	main()
