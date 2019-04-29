# importing the requests library
import requests
import json

# api-endpoint
URL = "https://cymon.io"

#Returns info related to IP address
def lookup_ip(ip):
    # sending get request and saving the response as response object
    r = requests.get(url=URL + '/api/nexus/v1/ip/' + ip)
    try:
        data = r.json()  # extracting data in json format
    except:
        data = None
    return data

#Returns log of security events associated with IP address
def ip_events(ip):
    # sending get request and saving the response as response object
    r = requests.get(url=URL + '/api/nexus/v1/ip/' + ip + '/events/')
    try:
        data = r.json()  # extracting data in json format
    except:
        data = None
    return data

#Returns domains associated with IP address
def ip_domains(ip):
    # sending get request and saving the response as response object
    r = requests.get(url=URL + '/api/nexus/v1/ip/' + ip + '/domains/')
    try:
        data = r.json()  # extracting data in json format
    except:
        data = None
    return data

#Returns URLs associated with IP address
def ip_urls(ip):
    # sending get request and saving the response as response object
    r = requests.get(url=URL + '/api/nexus/v1/ip/' + ip + '/urls/')
    try:
        data = r.json()  # extracting data in json format
    except:
        data = None
    return data

#Returns list of IPs with a certain tag in the past 'days' days and start the list at 'offset'
def ip_tags(tag, days=1, offset=0):
    # Options:
    # malware
    # botnet
    # spam
    # phishing
    # malicious activity
    # blacklist
    # dnsbl
    # sending get request and saving the response as response object
    PARAMS = {'days': days, 'offset': offset}
    r = requests.get(url=URL + '/api/nexus/v1/blacklist/ip/' + tag + '/', params=PARAMS)
    try:
        data = r.json()  # extracting data in json format
    except:
        data = None
    return data

#Returns details about a domain
def lookup_domain(domain):
    # sending get request and saving the response as response object
    r = requests.get(url=URL + '/api/nexus/v1/domain/' + domain)
    # print(r.url)
    try:
        data = r.json()  # extracting data in json format
    except:
        data = None
    return data

#Returns domains asssociated with a certain tag
def domain_blacklist(domain, days=1, offset=0):
    # sending get request and saving the response as response object
    PARAMS = {'days': days, 'offset': offset}
    r = requests.get(url=URL + '/api/nexus/v1/blacklist/domain/' + domain + '/', params=PARAMS)
    # print(r.url)
    try:
        data = r.json()  # extracting data in json format
    except:
        data = None
    return data

#Returns details about a URL
def lookup_url(location):
    # sending get request and saving the response as response object
    r = requests.get(url=URL + 'api/nexus/v1/url/' + location)
    try:
        data = r.json()  # extracting data in json format
    except:
        data = None
    return data


def get_event_tags(data):
    tags = []
    if data != None and data['count'] > 0:
        for i in data['results']:
            tags.append(i['tag'])
    return tags


# Print json nicely
def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None


r = requests.get(url='http://localhost:5000/?ip=5.248.253.190')
'''
try:
    data = r.json()  # extracting data in json format
except:
    data = None
'''
print(r.content)