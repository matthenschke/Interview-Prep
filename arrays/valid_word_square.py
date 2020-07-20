
def validWordSquare(words):
    if not words or len(words) == 0:
        return True

    for i in range(len(words)):
        cur_word = words[i]
        v_word = ""
        for j in range(len(words[i])):
            v_word += words[j][i]
        if v_word != cur_word:
            return False

    return True
