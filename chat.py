import openai
import os

class Chat:
    def __init__(self, message, maxToken):
        self.message = message
        self.maxToken = maxToken
    
    def coordinateFormatting(self):
        self.message = (
            "give me the longitude and latitude for " + self.message + ", give me only the numbers where the latitude is first and the longitude is second. Do not include a space inbetween the two values.")
            
    def getResponse(self):
        openai.api_key = os.environ["OPENAI_API_KEY"]
        completion = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = self.message,
            max_tokens= self.maxToken,
            n=1,
            stop=None,
            temperature=0.5,
        )

        return completion.choices[0].text

