from criteria import criteria_config
from models.ChatGPTModel import GPTModel

class LexicalResource():
    def __init__(self):
        self.lexical_resources_prompt = """
            User will input the question and his essay.
            You are the IELTS examiner for the writing task 2.
            You have to score an IELTS band (1.0-9.0) for the Lexical Resources criteria.
            Lexical Resources is all about how flexibly and fluently you can find the right words and phrases to convey precise meanings.
            Only score and assess the Lexical Resources, donn't mention any other criteria.
            Provide strength, weaknesses, band and how to improve on Lexical Resources criteria, give examples.
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
                                        "description": "The score of Lexical Resources criteria"
                                    },
                                    "strength": {
                                        "type": "string",
                                        "description": "The strength on Lexical Resources criteria"
                                    },
                                    "weaknesses": {
                                        "type": "string",
                                        "description": "The weaknesses on Lexical Resources criteria"
                                    },
                                    "how_to_improve": {
                                        "type": "string",
                                        "description": "How to improve the Lexical Resources criteria band"
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

        self.gpt_model = GPTModel(criteria_config.lexical_resources_model, self.lexical_resources_prompt, tools=self.tools)

    def assess(self, user_content):
        return self.gpt_model.anwser_question(user_content)