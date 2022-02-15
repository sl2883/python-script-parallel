    import requests
    
    headers = { 'X-CleverTap-Account-Id': '464-49W-WR6Z', 'X-CleverTap-Passcode': 'AMA-AUE-YWUL', 'Content-Type': 'application/json', }
    
    params = ( ('batch_size', '50'), )
    data = '{"event_name":"Product viewed 2","from":20211201,"to":20220106}'
    
    response = requests.post('https://us1.api.clevertap.com/1/events.json', headers=headers, params=params, data=data)
    
    print(response.text)
