import secrets
from twilio.rest import Client

account_sid = secrets.TWILIO_ACCOUNT_SID
auth_token = secrets.TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)
area_code_wanted = '949'
country = 'US'
local = client.available_phone_numbers(country).local.list(
    area_code=area_code_wanted,
    limit=5
)

for record in local:
    print(record.friendly_name)

# url = "https://api.twilio.com/2010-04-01/Accounts/%s/AvailablePhoneNumbers/US/Local.json?AreaCode=%s" % (account_sid, area_code)
# url = url + "%s:%s" % (account_sid,auth_token)
# # payload = {account_sid:auth_token}
# # res = requests.get(url, data=payload)
# print(url)
# res = requests.get(url)
# print(res.json())
#
# print(url)
#
# # bash = "curl -X GET \"" + url + "\" -u account_sid:auth_token "
# bash = "curl -X GET \"" + url + "\" -u %s:%s" % (account_sid, auth_token)
# print("bash pending is " + bash)
# workValidate = subprocess.check_output(['bash', '-c', bash]).decode("utf-8")
# print(" work validate  ", workValidate)

# curl -X GET "https://api.twilio.com/2010-04-01/Accounts/account_sid/AvailablePhoneNumbers/US/Local.json?AreaCode=949" -u account_sid:auth_token

