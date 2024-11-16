from difflib import SequenceMatcher


def similarity_score(keyword, title):
        return round(SequenceMatcher(None, keyword.lower(), title.lower()).ratio()*100,2)