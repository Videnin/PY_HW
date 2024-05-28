def correct_sentence(sentence1: str, sentence2: str) -> str:
    def correct_single_sentence(sentence: str) -> str:
        if sentence:
            sentence = sentence[0].toUpperCase() + sentence[1:]
        if not sentence.endswith('.'):
            sentence += '.'
        return sentence

    corrected_sentence1 = correct_single_sentence(sentence1)
    corrected_sentence2 = correct_single_sentence(sentence2)

    return corrected_sentence1 + " " + corrected_sentence2
