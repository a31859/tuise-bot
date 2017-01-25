import ConfigParser
import wolframalpha

class Question():
    def __init__(self):
        # get configuration
        configParser = ConfigParser.RawConfigParser()
        configFilePath = r'config/config.cfg'
        configParser.read(configFilePath)
        app_id = configParser.get('main', 'app_id')
        # setup wolfram alpha
        self.wa = wolframalpha.Client(app_id)

    def get_question_result(self, question):
        # clean the question command from the question
        question = question[0].lower().replace("question", "", 1)
        result = "Sorry, couldn't find the answer."
        if question == "":
            return True, result
        res = self.wa.query(question)
        if res["@numpods"] != '0':
            result = ""
            for pod in res.pods:
                for sub in pod.subpods:
                    if sub.plaintext is not None:
                        result += sub.plaintext + "\n"

        return True, result
