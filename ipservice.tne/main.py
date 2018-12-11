import requests, re, webbrowser

def supply(inputVal):
    if len(inputVal) > 1: raise ValueError('Too many arguments')
    endPoint = 'http://ip-api.com/json/'
    ipPattern = re.compile('\d+\.\d+\.\d+\.\d+')
    if ipPattern.match(inputVal[0]) or len(inputVal[0]) == 0:
        response = requests.get(endPoint + str(inputVal[0])).json()
        return {'name': '{}: {}'.format(response['query'], response['city']),
        'content': 'ISP: {}'.format(response['isp']),
        'innerItem': endPoint + str(inputVal[0])}

def serve(inputVal):
    innerURL = inputVal['innerItem']
    webbrowser.open(innerURL)
