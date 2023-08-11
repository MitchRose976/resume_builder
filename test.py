print ('Hello my name is Mitchell')
from bardapi import Bard
import os
import bardapi
# import sys
# print(sys.prefix)
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('GOOGLE_BARD_API_KEY')

bard = bardapi(token = token)

result = bard.get_answer("what is the current stock price of Nvidia?")
print(result)