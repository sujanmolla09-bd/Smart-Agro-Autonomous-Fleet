import os
from strands_agents import Agent
import google.genai as genai

class AgroFleetStrandsAgent(Agent):
    """
    AWS Strands SDK Wrapper for Smart Agro Autonomous Fleet.
    Integrates Gemini AI inference into AWS Strands Agent workflow.
    """
    def __init__(self, name="GoodNeighbor_AgroCoordinator"):
        super().__init__(name=name)
        # Initialize Gemini client using existing GCP environment
        self.ai_client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    def execute_community_task(self, prompt_text: str):
        """
        Translates community input into autonomous fleet actions via Gemini backend.
        """
        response = self.ai_client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt_text
        )
        return response.text

if __name__ == "__main__":
    agent = AgroFleetStrandsAgent()
    print("AWS Strands Agent initialized successfully with Gemini Backend.")
