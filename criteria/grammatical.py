from criteria import criteria_config
from models.ChatGPTModel import GPTModel

class Grammatical():
    def __init__(self):
        self.Grammatical_prompt = """
            User will input the question and his essay.
            You are the IELTS examiner for the writing task 2.
            You have to score an IELTS band (1.0-9.0) for the Grammatical Range and Accuracy criteria.
            Grammatical Range and Accuracy is the ability to use correct and precise grammar with control.
            Only score and assess the Grammatical Range and Accuracy, donn't mention any other criteria.
            Provide strength, weaknesses, band and how to improve on Grammatical Range and Accuracy criteria, give examples.
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
                                        "description": "The score of Grammatical Range and Accuracy criteria"
                                    },
                                    "strength": {
                                        "type": "string",
                                        "description": "The strength on Grammatical Range and Accuracy criteria"
                                    },
                                    "weaknesses": {
                                        "type": "string",
                                        "description": "The weaknesses on Grammatical Range and Accuracy criteria"
                                    },
                                    "how_to_improve": {
                                        "type": "string",
                                        "description": "How to improve the Grammatical Range and Accuracy criteria band"
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

        self.gpt_model = GPTModel(criteria_config.Grammatical_model, self.Grammatical_prompt, tools=self.tools)

    def assess(self, user_content):
        return self.gpt_model.anwser_question(user_content)