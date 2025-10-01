import random
import string

class JetSetGo:
    def __init__(self, familyName):
        self.familyName = familyName
        self.name = self.generate_identifier()

    @staticmethod
    def generate_identifier():
        # Generates a unique identifier like JSG123 or JSG4F7
        chars = string.ascii_uppercase + string.digits
        return 'JSG' + ''.join(random.choices(chars, k=3))
