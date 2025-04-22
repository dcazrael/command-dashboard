# utils/utilities.py
def replace_umlauts(text: str) -> str:
    """replace special German umlauts (vowel mutations) from text.
    ä -> ae, Ä -> Ae...
    ü -> ue, Ü -> Ue...
    ö -> oe, Ö -> Oe...
    ß -> ss
    """
    vowel_char_map = {
        ord('ä'): 'ae', ord('ü'): 'ue', ord('ö'): 'oe', ord('ß'): 'ss',
        ord('Ä'): 'Ae', ord('Ü'): 'Ue', ord('Ö'): 'Oe'
    }
    return text.translate(vowel_char_map)

def change_umlauts_back(text: str) -> str:
    """change replaced special German umlauts (vowel mutations) back to their original form from text.
    ae -> ä, Ae -> Ä...
    ue -> ü, Ue -> Ü...
    oe -> ö, Oe -> Ö...
    ss -> ß
    """
    vowel_char_map = {
        ord('ae'): 'ä', ord('ue'): 'ü', ord('oe'): 'ö', ord('ss'): 'ß',
        ord('Ae'): 'Ä', ord('Ue'): 'Ü', ord('Oe'): 'Ö'
    }
    return text.translate(vowel_char_map)