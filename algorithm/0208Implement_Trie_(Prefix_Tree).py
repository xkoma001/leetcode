class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sub_tries = dict()
        self.cur_ch = ''
        self.word_count = 0

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        n = len(word)
        pre_obj = self
        for i, ch in enumerate(word):
            if ch in pre_obj.sub_tries:
                pre_obj = pre_obj.sub_tries[ch]
            else:
                cur_obj = Trie()
                cur_obj.cur_ch = ch
                pre_obj.sub_tries[ch] = cur_obj
                pre_obj = cur_obj
            if i == n-1:
                pre_obj.word_count += 1

        return

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        pre_obj = self
        for w in word:
            if w not in pre_obj.sub_tries:
                return False
            pre_obj = pre_obj.sub_tries[w]

        return True if pre_obj.word_count > 0 else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        pre_obj = self
        for w in prefix:
            if w not in pre_obj.sub_tries:
                return False
            pre_obj = pre_obj.sub_tries[w]
        if pre_obj.word_count > 0 or len(pre_obj.sub_tries.keys()) > 0:
            return True
        return False


        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)

