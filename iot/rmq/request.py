import requests

class Request():
    def __init__(self, url):
        self.url = url
    def pretty_print_POST(self, req):
        print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
        ))
    def sendPostRequest(self, header, data):
        #r = requests.Request('POST', url=self.url, headers=header, data=data)
        #prepared = r.prepare()
	#self.pretty_print_POST(prepared)
        r = requests.post(url=self.url, headers=header, data=data)
	if r.text:
            return r.text
        return False

    def sendGetRequest(self, header=None):
        r = requests.get(self.url, headers=header)
        if r.text:
            return r.text
        return False
