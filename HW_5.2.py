import string


def generate_hashtag(s):
    s = s.translate(str.maketrans('', '', string.punctuation))
    words = s.split()
    capitalized_words = [word.capitalize() for word in words]
    hashtag = '#' + ''.join(capitalized_words)
    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag

print(generate_hashtag("sdasdasdfn ajfandaksnd kn."))  # Вихід: #HelloWorldThisIsATest
print(generate_hashtag(
    "jdbfkdSBFKJHBDFIBSDJKHFBIUdsbfib dihfbisdhBF IBIFJBISDBFIBSdifbisdbf[oJDSF0IQef0n."))
