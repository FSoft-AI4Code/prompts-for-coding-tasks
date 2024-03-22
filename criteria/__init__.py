from .task_achievement import TaskAchievement
from .coherence_and_cohesion import CoherenceAndCohesion
from .lexical_resources import LexicalResource
from .grammatical import Grammatical
from .general import GeneralAssessing


def score(user_content):
    output = {
        "task_assess": {},
        "coherence_assess": {},
        "lexical_assess": {},
        "gram_assess": {},
        "general_assess": {}
    }
    
    task_assess = TaskAchievement()
    coherence_assess = CoherenceAndCohesion()
    lexical_assess = LexicalResource()
    gram_assess = Grammatical()
    general_assess = GeneralAssessing()
    
    output["task_assess"] = task_assess.assess(user_content)
    output["coherence_assess"] = coherence_assess.assess(user_content)
    output["lexical_assess"] = lexical_assess.assess(user_content)
    output["gram_assess"] = gram_assess.assess(user_content)
    output["general_assess"] = general_assess.assess(user_content)
    return output
    