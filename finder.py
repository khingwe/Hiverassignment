class Finder:
    """
    Finder class takes input a list of words
    during the instance creation
    """

    def __init__(self, words):
        """
        Constructor Accepts the list of word
        """
        try:
            if not self.check_input(words):
                raise ValueError
            self.words_list = []
            self.actual = words
            for word in words:
                self.words_list.append(self.char_dict(word))
        except Exception as ex:
            print("ERROR: Instance Creation failed due to :".format(str(ex)))
            raise ex

    @staticmethod
    def check_input(words):
        """
        Check input is list or not
        """
        if isinstance(words, list):
            return True
        return False

    def char_dict(self, word):
        """
        Creating the dictionry for the input word
        if word is have integer input also process it
        """
        try:
            if isinstance(word, int):
                word = str(word)
            char_dict = {}
            if word is None:
                return None
            for x in word:
                char_dict[x] = char_dict.get(x, 0) + 1
            return char_dict
        except Exception as ex:
            print("ERROR: Word to dict creation is failed :{}".format(str(ex)))
            raise ex


    def find(self, word):
        """
        Find the word in the available word list
        """
        try:
            if word is None:
                return False
            out = []
            char_c = self.char_dict(word)
            for x in range(0, len(self.words_list)):
                if char_c == self.words_list[x]:
                    out.append(self.actual[x])
            if len(out) == 0:
                return None
            elif len(out) == 1:
                return out[0]
            else:
                return out
        except Exception as ex:
            print("ERROR: Word to dict creation is failed :{}".format(str(ex)))
            raise ex

def main():
    try:
        finder = Finder([None,"dsa",None,"sad"])
        print(finder.find("sad"))
        finder = Finder([None,"dsadd",None,"s", 123])
        print(finder.find("sda"))
    except Exception as e:
        raise e


if __name__=="__main__":
    main()
