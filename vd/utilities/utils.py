def webhandler(address):
    if 'http://' in address:
        return address
    return 'http://' + address

def fbhanlder(fb):
    if 'facebook' in fb:
        if 'http://' in fb:
            return fb
    return 'http://www.facebook.com/' + fb

def instahandler(insta):
    if insta[0] == '@':
        return 'http://www.instagram.com/' + insta[1:]