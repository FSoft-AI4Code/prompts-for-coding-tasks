from criteria import criteria_config
from models.ChatGPTModel import GPTModel

class TaskAchievement():
    def __init__(self):
        self.task_achievement_prompt = """
            User will input the question and his essay.
            You are the IELTS examiner for the writing task 2.
            You have to score an IELTS band (1.0-9.0) for the Task Achievement criteria.
            Task Achievement is the ability to answer the question properly where user will be required to write a clear and a well develop answer.
            Only score and assess the Task Achievement, donn't mention any other criteria.
            Provide strength, weaknesses, band and how to improve on Task Achievement criteria, give examples.
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
                                        "description": "The score of Task Achievement criteria"
                                    },
                                    "strength": {
                                        "type": "string",
                                        "description": "The strength on Task Achievement criteria"
                                    },
                                    "weaknesses": {
                                        "type": "string",
                                        "description": "The weaknesses on Task Achievement criteria"
                                    },
                                    "how_to_improve": {
                                        "type": "string",
                                        "description": "How to improve the Task Achievement criteria band"
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

        self.gpt_model = GPTModel(criteria_config.task_achievement_model, self.task_achievement_prompt, tools=self.tools)

    def assess(self, user_content):
        return self.gpt_model.anwser_question(user_content)