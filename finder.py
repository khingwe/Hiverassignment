class Finder:
  def __init__(self, words):
    self.word_list = []
    self.actual = words
    for word in words:
      self.word_list.append(self.convert_dict(word))

  def convert_dict(self, word):
    if word is None:
      return None
    char_count = {}
    for x in range(0, len(word)):
      if char_count.get(word[x]) is None:
        char_count[word[x]] = 1
      else:
        char_count[word[x]] += 1
    return char_count

  def find(self, word):
    if word is None:
      return False
    out = []
    char_c = self.convert_dict(word)
    for x in range(0, len(self.word_list)):
      if char_c == self.word_list[x]:
        out.append(self.actual[x])
    if len(out) == 0:
      return None
    elif len(out) == 1:
      return out[0]
    else:
      return out
finder = Finder([None,"dsa",None,"sad"])
print(finder.find("sad"))
finder = Finder([None,"dsadd",None,"sad"])
print(finder.find("sda"))
