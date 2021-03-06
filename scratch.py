import requests
import time

url = "https://us1.api.clevertap.com/1/upload"


headers = {
  'X-CleverTap-Account-Id': 'TEST-869-K69-446Z',
  'X-CleverTap-Passcode': 'SMS-RIV-AAUL',
  'Content-Type': 'application/json'
}

for x in range(50):

  identity = "sl-py-1-" + str(x)
  email = identity + "@test.com"

  identityPayload = "{" \
            "    \"d\": [" \
            "        {" \
            "            " \
            "            \"identity\": \""+identity+"\"," \
            "            \"type\": \"profile\"," \
            "            \"profileData\": {" \
            "                \"Email\":\""+email+"\"," \
            "                \"dumdum1\":\"1234\"" \
            "            }" \
            "        }" \
            "    ]" \
            "}" \
            ""
  print(identity)
  print(identityPayload)
  responseProfile = requests.request("POST", url, headers=headers, data=identityPayload)
  print(responseProfile)
  ts = str(int(time.time()))
  eventPayload = "{" \
                "    \"d\": [" \
                "         {" \
                "            \"identity\":\""+identity+"\"," \
                "            \"type\": \"event\"," \
                "            \"evtName\": \"Added to Cart 1\"," \
                "            \"evtData\": {" \
                "               \"product Name\": \"Grapes\"," \
                "               \"image\": \"https://images.all-free-download.com/images/graphiclarge/table_grapes_grapes_fruit_214430.jpg\"," \
                "               \"sessionID\": \"1234\"," \
                "               \"hex\": \"123456\"" \
                "            }," \
                "            \"ts\": "+ts+"" \
                "        }" \
                "    ]" \
                "}"
  print(eventPayload)
  responseEvent = requests.request("POST", url, headers=headers, data=eventPayload)
  print(responseEvent)


