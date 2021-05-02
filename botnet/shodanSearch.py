import shodan
import sys
import os

# Configuration
API_KEY = os.getenv('APIKEY') 

# Input validation
if len(sys.argv) == 1:
    print('Usage: {0} <search query>'.format(sys.argv[0]))
    sys.exit(1)

try:
    # Setup the api
    api = shodan.Shodan(API_KEY)

    # Perform the search
    query = ' '.join(sys.argv[1:])
    result = api.search(query)

    # Loop through the matches and write th result to iplist.txt file
    with open('./iplist.txt', 'w') as ipes:
        for service in result['matches']:
            ipes.write(service['ip_str'] + '\n')

    print('The Open Docker API Hosts have been added into iplist.txt')
except Exception as e:
    print('Error: %s' % e)
    sys.exit(1)
