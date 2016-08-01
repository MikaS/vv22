# Twitter

import oauth2 as oauth
import urllib2 as urllib

api_key = "7eFxMn6jhb7nbUrSjNSH92Q2H"
api_secret = "hAJvwKCykc1MStaQH9T37XYMP88Pppi6C1Nrn3FSfZo7kh7eU1"
access_token_key = "2608376858-DTpCSPnDJQLU6JMxDTPT6OBzninIc7k4X1GuPeZ"
access_token_secret = "DModyEm6IxQz7YDHbnpufOpoDpb7ypvYMUlN1o1FKhWYC"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=api_key, secret=api_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, http_method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

"""
"""
def streaming(word):
  url = "https://stream.twitter.com/1.1/statuses/filter.json?track=" + word
  parameters = []
  response = tr.twitterreq(url, "POST", parameters)
  for line in response:
    j = json.loads(line)
    for tweet in j:
      print tweet['text'].encode('ascii','ignore')

if __name__ == '__main__':

   name = 'lepen'
   streaming(name)