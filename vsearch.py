def search4vowels(phrase:str) -> set:
    """Return any vowels foun in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intesection(set(phrase))
def search4letters(phrase:str, letters:str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intesection(set(phrase))
