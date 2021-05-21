class QSSLoad:
    def __init__(self):
        pass

    @staticmethod
    def readQssFile(qssFileName):
        with open(qssFileName, 'r',  encoding='UTF-8') as file:
            return file.read()
