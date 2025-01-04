import requests
import json
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.googlesearch import GoogleSearch
import os
from dotenv import load_dotenv
load_dotenv()

class chatbot:
  

   def __init__(self):
   
    self.web_search_agent=Agent(
    name="web Search agent",
    description="You are a news agent that helps users find the latest news.",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[GoogleSearch()],
    instructions=["Given a topic by the user, respond with 4 latest news items about that topic.",
        "Search for 10 news items and select the top 4 unique items.",
        "Search in English"],
    show_tool_calls=True,
    markdown=True
)

   def get_response(self, user_input: str) -> str:
        response =self.web_search_agent.run(user_input)
         
        print(response)
        if 'content' in response:
            return response['content']
        else:
            return "Sorry, I couldn't retrieve a response at the moment."