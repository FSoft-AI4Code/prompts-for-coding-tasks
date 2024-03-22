from criteria import criteria_config
from models.ChatGPTModel import GPTModel

class CoherenceAndCohesion():
    def __init__(self):
        self.coherence_and_cohesion_prompt = """
            User will input the question and his essay.
            You are the IELTS examiner for the writing task 2.
            You have to precisely score an IELTS band (1.0-9.0) for both Coherence and Cohesion criteria based on user essay.
            Coherence means the connection of ideas on a larger scale, while cohesion means connection at a sentence level.
            Only score and assess the Coherence and Cohesion, donn't mention any other criteria.
            Provide strength, weaknesses, band and how to improve on Coherence and Cohesion criteria based on user essay, need to be specific.
        """
        self.tools = [
            {
                "type": "function",
                "function": {
                        "rule": "Always call this function to return a certain format for user",
                        "name": "get_answer",
                        "description": "Get the answer of chatgpt on a certain format",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                    "band": {
                                        "type": "string",
                                        "description": "The score of both Coherence and Cohesion criteria based on user essay"
                                    },
                                    "strength": {
                                        "type": "string",
                                        "description": "The strength on Coherence and Cohesion criteria based on user essay"
                                    },
                                    "weaknesses": {
                                        "type": "string",
                                        "description": "The weaknesses on Coherence and Cohesion criteria based on user essay"
                                    },
                                    "how_to_improve": {
                                        "type": "string",
                                        "description": "How to improve the Coherence and Cohesion criteria band based on user essay"
                                    },
                                },
                            "required": ["band", "strength", "weaknesses", "how_to_improve"]
                        },
                }
            }
        ]

        self.gpt_model = GPTModel(criteria_config.coherence_and_cohesion_model, self.coherence_and_cohesion_prompt, tools=self.tools)

    def assess(self, user_content):
        return self.gpt_model.anwser_question(user_content)