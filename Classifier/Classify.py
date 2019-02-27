from Classifier.Cymon_API import *

#Returns False for good websites, and True for bad websites
def check_IP(ip):
    data = ip_events(ip)
    if data == None:
        return False
    elif data["count"]>0:
        return True
    else:
        return False


#d = check_IP('5.248.253.193')
#print(d)
