from Cymon_API import *
import re
import whois
import datetime
import tldextract as tld

# Extract domain part of URL
def getDomain(url):
    t_url = tld.extract(url)
    dm = t_url.domain
    sdm = t_url.subdomain
    sfx = t_url.suffix
    if sdm == '':
        domain = dm + '.' + sfx
    else:
        domain = sdm + '.' + dm + '.' + sfx
    return domain


# 1.1.1 Check if url contains an IP address
def is_ip(url):
    finder = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    check = finder.search(url)
    if check is not None:
        return 1
    return -1


# 1.1.2 Check if URL is too long
def is_too_long(url):
    if (len(url) < 54):
        return -1
    if (len(url) >= 75):
        return 1
    else:
        return 0


# 1.1.3 Check if URL is shortened
def is_shortened(url):
    if ('bit.ly' in url):
        return 1
    return -1


# 1.1.4 Check if URL contains @
def has_at(url):
    if ('@' in url):
        return 1
    return -1


# 1.1.5 Check if URL contains redirect
def has_redirect(url):
    finder = re.compile(r'//')
    fs = finder.search(url)
    if fs is None:
        return -1
    else:
        location = fs.end()
        if (location > 7):
            return 1
    return -1


# 1.1.6 Check if - is in domain name
def has_dash(url):
    extracted_url = tld.extract(url)
    if ('-' in extracted_url.domain or '-' in extracted_url.subdomain):
        return 1
    return -1


# 1.1.7 Check the number of subdomains
def has_multi_subdomain(url):
    finder = re.compile(r'www\.')
    url = finder.sub('', url)
    t_url = tld.extract(url)
    dm = t_url.domain
    sdm = t_url.subdomain
    dot_count = dm.count('.') + sdm.count('.') + (not sdm == '') + 1
    if (dot_count == 1):
        return -1
    if (dot_count > 2):
        return 1
    else:
        return 0


# 1.1.8 Check if URL uses HTTPS
def has_https(url):
    # Get https certificate
    if 'https' in url:
        return 1
    return -1


# 1.4.2, 1.4.1, 1.1.9 Check DNS record exists, age of domain, and time until expiration
def domain_features(url):
    out = [1, 1, 1]
    try:
        q = whois.query(getDomain(url))
        if q is not None:
            out[0] = -1
            today = datetime.datetime.now()
            creation_date = q.creation_date
            if creation_date is None:
                out[1] = 1
            else:
                age = (today - creation_date).days * 1. / 365
                if (age <= 0.5):
                    out[1] = 1
                else:
                    out[1] = -1
            expiration_date = q.expiration_date
            if expiration_date is None:
                out[2] = 1
            else:
                lifetime = (expiration_date - today).days * 1. / 365
                if (lifetime <= 1):
                    out[2] = 1
                else:
                    out[2] = -1
        else:
            out = [1, 1, 1]
    except:
        out = [1, 1, 1]

    return out


# 1.4.2
def webTraffic(url):
    alexa_rank = seo.get_alexa(url)
    if alexa_rank is None:
        return 1
    elif alexa_rank < 100000:
        return -1
    else:
        return 0


# 1.4.4
def googleIndex(url):
    try:
        result = search(url, num=1, stop=1, pause=2)
        if len(list(result)) == 0:
            return 1
        else:
            return -1
    except:
        return 1


# 1.4.7 Check if domain is blacklisted
def check_domain(url):
    finder = re.compile(r'www\.')
    url = finder.sub('', url)
    t_url = tld.extract(url)
    dm = t_url.domain
    sdm = t_url.subdomain
    sfx = t_url.suffix
    data = lookup_domain(sdm + '.' + dm + '.' + sfx)
    if data == None:
        return 1
    elif len(data) > 1:
        return -1
    else:
        return 1


# 1.1.12 Check if https is in domain name
def https_in_domain(url):
    dm = getDomain(url)
    if ('https' in dm):
        return 1
    else:
        return -1


def getFeatures(url):
    whois_features = domain_features(url)
    features = [0] * 13
    features[0] = is_ip(url)  # 1.1.1
    features[1] = is_too_long(url)  # 1.1.2
    features[2] = is_shortened(url)  # 1.1.3
    features[3] = has_at(url)  # 1.1.4
    features[4] = has_redirect(url)  # 1.1.5
    features[5] = has_dash(url)  # 1.1.6
    features[6] = has_multi_subdomain(url)  # 1.1.7
    features[7] = has_https(url)  # 1.1.8
    features[8] = whois_features[2]  # 1.1.9
    features[9] = https_in_domain(url)  # 1.1.12
    features[10] = whois_features[0]  # 1.4.2
    features[11] = whois_features[1]  # 1.4.1
    # features[11] = googleIndex(url)          #1.4.4
    features[12] = check_domain(url)  # 1.4.7
    return features