import json
from models import chatgpt_config
from openai import OpenAI

class GPTModel:
    
    def __init__(self, model, system_prompt, tools=[], image_included=False):
        self.model = model
        self.system_prompt=system_prompt
        self.tools = tools
        self.image_included = image_included
        self.client = OpenAI(api_key=chatgpt_config.openai_api_key)
        self.output_format = {
            "answer": "",
            "tool_calls": False
        }

    def free_history(self):
        self.history=[]
    
    def anwser_question(self, question_content):
        messages = []
        messages.append({"role": "system", "content": self.system_prompt})
        messages.append({"role": "user", "content": [
                        {
                            "type": "text",
                            "text": question_content
                        },
                    ]},)
        
        if len(self.tools) > 0 and not self.image_included:
            messages.append({"role": "function", "name": self.tools[0]["function"]["name"], "content": self.tools[0]["function"]["rule"]})

        if not self.image_included:
            if len(self.tools)>0:
                response = self.client.chat.completions.create(
                            model=self.model,
                            messages=messages,
                            tools=self.tools,
                            temperature=1
                        )
            else:
                response = self.client.chat.completions.create(
                            model=self.model,
                            messages=messages,
                            temperature=1
                        )
            
        if response.choices[0].message.content:
            self.output_format["answer"] = response.choices[0].message.content
        
        if response.choices[0].message.tool_calls:
            self.output_format["answer"] = eval(response.choices[0].message.tool_calls[0].function.arguments)
            self.output_format["tool_calls"] = True

        print(response)
        return self.output_format
    
if __name__ == "__main__":
    tools = [
        {
            "type": "function",
            "function": {
                    "rule": "Always call this function to return a certain format for user",
                    "name": "get_answer",
                    "description": "Get the answer of chatgpt on a certain format",
                    "parameters": {
                        "type": "object",
                        "properties": {
                                "score": {
                                    "type": "string",
                                    "description": "The score of user content"
                                },
                                "content": {
                                    "type": "string",
                                    "description": "The answer of chatgpt"
                                }
                            },
                        "required": ["score", "content"]
                    },
            }
        }
    ]
    system_prompt="you are a helpful assistant"
    gptmodel = GPTModel("gpt-3.5-turbo-0125", system_prompt, tools=tools)
    gptmodel.anwser_question("hello")