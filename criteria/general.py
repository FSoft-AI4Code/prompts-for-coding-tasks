from criteria import criteria_config
from models.ChatGPTModel import GPTModel

class GeneralAssessing():
    def __init__(self):
        self.general_prompt = """
            User will input the question and his essay.
            You are the IELTS examiner for the writing task 2.
            You have to score an IELTS band (1.0-9.0) for the essay.
            Provide strength, weaknesses, band and how to improve on the essay, give examples.
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
                                        "description": "The band of essay"
                                    },
                                    "strength": {
                                        "type": "string",
                                        "description": "The strength of essay"
                                    },
                                    "weaknesses": {
                                        "type": "string",
                                        "description": "The weaknesses of essay"
                                    },
                                    "how_to_improve": {
                                        "type": "string",
                                        "description": "How to improve the band of essay"
                                    },
                                    "example": {
                                        "type": "string",
                                        "description": "Example for the improvement"
                                    }
                                },
                            "required": ["band", "strength", "weaknesses", "how_to_improve", "example"]
                        },
                }
            }
        ]

        self.gpt_model = GPTModel(criteria_config.general_assessing_model, self.general_prompt, tools=self.tools)

    def assess(self, user_content):
        return self.gpt_model.anwser_question(user_content)