
# Below is a nested dictionary. Nesting of a list within a dictionary is also possible.
my_profile = {
    "Vince": {"age": 27, "origin": 'Kenya', "Tribe": 'chonyi'},
    "Milcah": {"age": 17, "origin": 'Kenya', "Tribe": 'chonyi'},
    
}

# printing the nested dictionary accessing kesys and values:
# print(my_profile["Milcah"]) # printing Milcah's details
# print(my_profile["Milcah"]["age"]) # printing Milcah's age only.
#my_profile["Milcah"]["student_id"]=6190 #adding a phone number
#print(my_profile["Milcah"])
#del my_profile["Milcah"]["age"]
#print(my_profile["Milcah"])


# nesting a list in a dictionary

# names = {
   # "places": ["wayani","golini","mwabuga"]
#}



# nesting a dictionary within a list
#names = [
 #   {"places":'All', "name": 'wayani', "home": 'golini', "wapi": 'mwabuga'}
#]
#print(names[{"name"}])

events_json = {
        "when": "2025-01-22T07:46:07.000Z",
        "created_at": "2025-01-22T07:46:14.823Z",
        "source_info": {
            "ip": "41.73.131.82"
        },
        "customer_id": "1eaa6d35-95d9-4d5f-9d6f-42eae6d80457",
        "severity": "low",
        "endpoint_id": "c4828180-ab83-493b-8406-8dbd20e0ccd2",
        "endpoint_type": "computer",
        "user_id": "6360f332a0944211ed3f4e53",
        "source": "Nwanneka Ofuase",
        "type": "Event::Endpoint::WebControlViolation",
        "name": "'https://s1.ticketm.net' warned due to category 'Shopping'",
        "location": "ManOff02",
        "id": "61613287-011c-4800-a47c-5e9bfecfc322",
        "group": "WEB"
    }

print(type(events_json))


alert_json = [
    {"javaUUID": "c20ac38f-ba3a-143b-8a1b-aa4c4f6be4aa", 
     "actionable": False, 
     "customer_id": "1eaa6d35-95d9-4d5f-9d6f-42eae6d80457", 
     "created_at": "2025-01-26T16:55:18.145Z", 
     "severity": "high", 
     "event_service_event_id": "2ca03cf8-aba3-41b3-a8b1-aac4f4b64eaa", 
     "when": "2025-01-26T16:55:18.129Z", 
     "description": "Firewall has not contacted Sophos Central for the past 779 minutes", 
     "data": {"created_at": 1737910518131, 
    "endpoint_id": "d1d73c13-73b5-4050-9648-6251ccffb6ca", 
    "endpoint_java_id": "d1d73c13-73b5-4050-9648-6251ccffb6ca", 
    "endpoint_platform": "unknown", "endpoint_type": "utm", 
    "event_service_id": {"type": 3, "data": "LKA8+KujQbOosarE9LZOqg=="}, 
    "inserted_at": 1737910518131}, 
    "type": "Event::Firewall::LostConnectionToSophosCentral", 
    "location": "Oghara ", 
    "id": "2ca03cf8-aba3-41b3-a8b1-aac4f4b64eaa"}, 
    {"javaUUID": "d8e2e171-edf8-246f-397d-45d4e5c603fb", 
     "actionable": False, 
     "customer_id": "1eaa6d35-95d9-4d5f-9d6f-42eae6d80457", 
     "created_at": "2025-01-26T19:25:06.563Z", 
     "severity": "medium", 
     "event_service_event_id": "8d2e1e17-de8f-42f6-93d7-544d5e6c30bf", 
     "when": "2025-01-26T19:25:06.540Z", 
     "description": "Rainoil_IPSEC-1 - IPSec Connection Rainoil_IPSEC-1 between 155.93.127.141 and 155.93.94.66 for Child Rainoil_IPSEC-2 terminated. (Remote: 155.93.127.141)", 
     "data": {"created_at": 1737919506550, 
              "endpoint_id": "8ea36a03-9f0d-4518-8cbf-6999c4b849dd", 
              "endpoint_java_id": "8ea36a03-9f0d-4518-8cbf-6999c4b849dd", 
              "endpoint_platform": "unknown", 
              "endpoint_type": "utm", 
              "event_service_id": {"type": 3, "data": "jS4eF96PQvaT11RNXmwwvw=="}, 
              "inserted_at": 1737919506550}, 
    "type": "Event::Firewall::FirewallVPNTunnelDown", 
    "location": "Fynefield", 
    "id": "8d2e1e17-de8f-42f6-93d7-544d5e6c30bf"}, 
    {"javaUUID": "ba2d2b7f-1410-a4ae-4a0f-ad786f7ca610", 
     "actionable": False, 
     "customer_id": "1eaa6d35-95d9-4d5f-9d6f-42eae6d80457", 
     "created_at": "2025-01-26T19:25:10.986Z", 
     "severity": "medium", 
     "event_service_event_id": "abd2b2f7-4101-4aea-a4f0-da87f6c76a01", 
     "when": "2025-01-26T19:25:10.963Z", 
     "description": "VDT_TO_HQ-1 - IPSec Connection VDT_TO_HQ-1 between 155.93.127.141 and 41.216.168.74 for Child VDT_TO_HQ-7 terminated. (Remote: 155.93.127.141)", 
     "data": {"created_at": 1737919510967, 
              "endpoint_id": "f165c74d-c6bc-4953-8e65-9ec461324d0f", 
              "endpoint_java_id": "f165c74d-c6bc-4953-8e65-9ec461324d0f", 
              "endpoint_platform": "unknown", 
              "endpoint_type": "utm", 
              "event_service_id": {"type": 3, 
                                   "data": "q9Ky90EBSuqk8NqH9sdqAQ=="}, 
                "inserted_at": 1737919510967}, 
    "type": "Event::Firewall::FirewallVPNTunnelDown", 
    "location": "ijegun", 
    "id": "abd2b2f7-4101-4aea-a4f0-da87f6c76a01"}]

for i in alert_json: 
    print(alert_json)






