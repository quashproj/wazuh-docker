
#!/var/ossec/framework/python/bin/python3
import requests
import sys
import json
import logging
import os

from requests import packages
 
###################################
# Setup LOGGER
###################################
debug_enabled = True
info_enabled = True

# Set paths
pwd = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
log_file = '{0}/logs/integrations.log'.format(pwd)
logger = logging.getLogger(__name__)

# Set logging level
if debug_enabled:
    logger.setLevel(logging.DEBUG)
elif info_enabled:
    logger.setLevel(logging.INFO)
else:
    logger.setLevel(logging.WARNING)

# Create the logging file handler
fh = logging.FileHandler(log_file)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.debug('quash - configured logger ...')


# Silence insecure request warning
requests.packages.urllib3.disable_warnings()

###################################
# Main FN
###################################
def quash():
    try:

        source_path = None
        api_key = None
        hook_url = None

        source_path = sys.argv[1]
        api_key = sys.argv[2]
        hook_url = sys.argv[3]

        if len(sys.argv) < 4:
            logger.error("quash - missing required arguments. Usage: script.py <source_path> <api_key> <hook_url>")
            raise IndexError("Missing required arguments. Usage: script.py <source_path> <api_key> <hook_url>")


        logger.debug('quash - source path: %s', source_path)
        
        with open(source_path, 'r') as alert_file:
            alert_json = json.load(alert_file)
        
        json_string = json.dumps(alert_json, indent=2)

        alert_level = alert_json['rule']['level']
        ruleid = alert_json['rule']['id']

        logger.debug('quash - alert JSON: %s %s', alert_level, ruleid)

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + api_key,
            "X-Argo-E2E": "true"
        }

        response = requests.post(hook_url, headers=headers, data=json_string, verify=False)
        
        if response.status_code == 200:
            logger.debug("quash - alert successfully sent to hook URL")
        else:
            logger.error("quash - failed to send alert. Status code: %d, Response: %s", response.status_code, response.text)

    except IndexError:
        logger.error("quash - missing required arguments. Usage: script.py <source_path> <api_key> <hook_url>")
    except FileNotFoundError:
        logger.error("quash - source file not found: %s", source_path)
    except json.JSONDecodeError as e:
        logger.error("quash - error decoding JSON from source file: %s", str(e))
    except requests.RequestException as e:
        logger.error("quash - error making request to hook URL: %s", str(e))
    except Exception as e:
        logger.error("quash - an unexpected error occurred: %s", str(e))

if __name__ == "__main__":
    quash()
