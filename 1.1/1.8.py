
def longest_shortest_word(text):
    words = text.split()
    if len(words) > 0:
        longest_word = max(words, key=len)
        shortest_word = min(words, key=len)
        return longest_word, shortest_word
    else:
        return None, None

text = "I am a student,i am studying Programming language C in Peking University."
longest_word, shortest_word = longest_shortest_word(text)
print("最长的单词是：", longest_word)
print("最短的单词是：", shortest_word)