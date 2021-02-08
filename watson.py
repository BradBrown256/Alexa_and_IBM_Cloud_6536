import logging
import json
import base64
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#authenticate with watson using AssistantV2
authenticator = IAMAuthenticator("7ykDaIT5ufnuoC4zVyAxams20tfeU_Nmie5L_RW_6xfr")
assistant = AssistantV2(
    version='2020-09-24',
    authenticator=authenticator
)
assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com')
#assistant.set_service_url('https://gateway.watsonplatform.net/assistant/api')
#assistant.set_disable_ssl_verification(True)

#start a "session" (tell IBM to create and manage a token for you that you can use for authentication until you terminate the session)
#tip, you can get your assistant ID by looking at the URL in the browser for your assistant
#its right after the /assistant part of the url
session = assistant.create_session(assistant_id="1c7b6de3-5873-4a81-aea8-583a760cf6a6").get_result()
print(json.dumps(session, indent=4, sort_keys=True))

#send message to watson and display response received from watson
message = assistant.message(assistant_id="1c7b6de3-5873-4a81-aea8-583a760cf6a6",session_id=session["session_id"],input= {'message_type': 'text','text': 'hello watson'}).get_result()
print(json.dumps(message, indent=4, sort_keys=True))

#send message to watson and display response received from watson
message = assistant.message(assistant_id="1c7b6de3-5873-4a81-aea8-583a760cf6a6",session_id=session["session_id"],input= {'message_type': 'text','text': 'Who are the group members'}).get_result()
print(json.dumps(message, indent=4, sort_keys=True))

#send message to watson and display response received from watson
message = assistant.message(assistant_id="1c7b6de3-5873-4a81-aea8-583a760cf6a6",session_id=session["session_id"],input= {'message_type': 'text','text': 'What is the group number'}).get_result()
print(json.dumps(message, indent=4, sort_keys=True))

#send message to watson and display response received from watson
message = assistant.message(assistant_id="1c7b6de3-5873-4a81-aea8-583a760cf6a6",session_id=session["session_id"],input= {'message_type': 'text','text': 'When is class'}).get_result()
print(json.dumps(message, indent=4, sort_keys=True))

#terminate the session (tell IBM that you are done with your token)
response = assistant.delete_session(assistant_id="1c7b6de3-5873-4a81-aea8-583a760cf6a6", session_id=session["session_id"]).get_result()
print(json.dumps(response, indent=4, sort_keys=True))
