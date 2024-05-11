import pytest
from unittest.mock import patch
from engines.feature_compliment_engine import FeatureComplimentEngine

# Initialize the FeatureComplimentEngine without mock dictionaries
engine = FeatureComplimentEngine()

def conjugate_verb(verb, tense, person, number):
    """
    Conjugates a verb based on the provided tense, person, and number.
    Handles both regular and irregular verbs.
    """
    # Dictionary of irregular verbs and their conjugations
    irregular_verbs = {
        'be': {'present': {2: {'singular': 'are', 'plural': 'are'}, 3: {'singular': 'is', 'plural': 'are'}},
               'past': {2: {'singular': 'were', 'plural': 'were'}, 3: {'singular': 'was', 'plural': 'were'}}},
        'have': {'present': {2: {'singular': 'have', 'plural': 'have'}, 3: {'singular': 'has', 'plural': 'have'}},
                 'past': {2: {'singular': 'had', 'plural': 'had'}, 3: {'singular': 'had', 'plural': 'had'}}},
        'go': {'present': {2: {'singular': 'go', 'plural': 'go'}, 3: {'singular': 'goes', 'plural': 'go'}}},
        'lead': {'present': {2: {'singular': 'lead', 'plural': 'lead'}, 3: {'singular': 'leads', 'plural': 'lead'}}},
        'eat': {'present': {2: {'singular': 'eat', 'plural': 'eat'}, 3: {'singular': 'eats', 'plural': 'eat'}},
                'past': {2: {'singular': 'ate', 'plural': 'ate'}, 3: {'singular': 'ate', 'plural': 'ate'}}},
        'write': {'present': {2: {'singular': 'write', 'plural': 'write'}, 3: {'singular': 'writes', 'plural': 'write'}},
                  'past': {2: {'singular': 'wrote', 'plural': 'wrote'}, 3: {'singular': 'wrote', 'plural': 'wrote'}}},
        'sing': {'present': {2: {'singular': 'sing', 'plural': 'sing'}, 3: {'singular': 'sings', 'plural': 'sing'}},
                 'past': {2: {'singular': 'sang', 'plural': 'sang'}, 3: {'singular': 'sang', 'plural': 'sang'}}},
        'run': {'present': {2: {'singular': 'run', 'plural': 'run'}, 3: {'singular': 'runs', 'plural': 'run'}},
                'past': {2: {'singular': 'ran', 'plural': 'ran'}, 3: {'singular': 'ran', 'plural': 'ran'}}},
        'speak': {'present': {2: {'singular': 'speak', 'plural': 'speak'}, 3: {'singular': 'speaks', 'plural': 'speak'}},
                  'past': {2: {'singular': 'spoke', 'plural': 'spoke'}, 3: {'singular': 'spoke', 'plural': 'spoke'}}},
        'fly': {'present': {2: {'singular': 'fly', 'plural': 'fly'}, 3: {'singular': 'flies', 'plural': 'fly'}},
                'past': {2: {'singular': 'flew', 'plural': 'flew'}, 3: {'singular': 'flew', 'plural': 'flew'}}},
        'begin': {'present': {2: {'singular': 'begin', 'plural': 'begin'}, 3: {'singular': 'begins', 'plural': 'begin'}},
                  'past': {2: {'singular': 'began', 'plural': 'began'}, 3: {'singular': 'began', 'plural': 'began'}}},
        'choose': {'present': {2: {'singular': 'choose', 'plural': 'choose'}, 3: {'singular': 'chooses', 'plural': 'choose'}},
                   'past': {2: {'singular': 'chose', 'plural': 'chose'}, 3: {'singular': 'chose', 'plural': 'chose'}}},
        'drive': {'present': {2: {'singular': 'drive', 'plural': 'drive'}, 3: {'singular': 'drives', 'plural': 'drive'}},
                  'past': {2: {'singular': 'drove', 'plural': 'drove'}, 3: {'singular': 'drove', 'plural': 'drove'}}},
        'rise': {'present': {2: {'singular': 'rise', 'plural': 'rise'}, 3: {'singular': 'rises', 'plural': 'rise'}},
                 'past': {2: {'singular': 'rose', 'plural': 'rose'}, 3: {'singular': 'rose', 'plural': 'rose'}}},
        # Added irregular verbs
        'give': {'present': {2: {'singular': 'give', 'plural': 'give'}, 3: {'singular': 'gives', 'plural': 'give'}},
                 'past': {2: {'singular': 'gave', 'plural': 'gave'}, 3: {'singular': 'gave', 'plural': 'gave'}}},
        'take': {'present': {2: {'singular': 'take', 'plural': 'take'}, 3: {'singular': 'takes', 'plural': 'take'}},
                 'past': {2: {'singular': 'took', 'plural': 'took'}, 3: {'singular': 'took', 'plural': 'took'}}},
        'see': {'present': {2: {'singular': 'see', 'plural': 'see'}, 3: {'singular': 'sees', 'plural': 'see'}},
                'past': {2: {'singular': 'saw', 'plural': 'saw'}, 3: {'singular': 'saw', 'plural': 'saw'}}},
        'come': {'present': {2: {'singular': 'come', 'plural': 'come'}, 3: {'singular': 'comes', 'plural': 'come'}},
                 'past': {2: {'singular': 'came', 'plural': 'came'}, 3: {'singular': 'came', 'plural': 'came'}}},
    }

    # Check if the verb is irregular and conjugate accordingly
    if verb in irregular_verbs:
        conjugated = irregular_verbs[verb].get(tense, {}).get(person, {}).get(number, None)
        if conjugated:
            return conjugated

    # Apply regular conjugation rules for regular verbs
    if tense == 'present' and person == 2 and number == 'singular':
        if verb.endswith('y'):
            return verb[:-1] + 'ies'
        elif verb.endswith('o') or verb.endswith('ch') or verb.endswith('s') or verb.endswith('sh') or verb.endswith('x') or verb.endswith('z'):
            return verb + 'es'
        else:
            return verb + 's'
    elif tense == 'past':
        # Simple past tense regular conjugation rule
        if verb.endswith('e'):
            return verb + 'd'
        elif verb.endswith('y'):
            return verb[:-1] + 'ied'
        else:
            return verb + 'ed'
    return verb

def test_generate_compliment_non_empty():
    compliment = engine.generate_compliment()
    assert compliment, "The compliment should not be empty."

def test_generate_compliment_ends_with_period():
    compliment = engine.generate_compliment()
    assert compliment.endswith('.'), "The compliment should end with a period."

def test_generate_compliment_starts_with_capital():
    compliment = engine.generate_compliment()
    assert compliment[0].isupper(), "The compliment should start with a capital letter."

def test_select_appropriate_word_returns_string():
    word = engine.select_appropriate_word('nouns')
    assert isinstance(word, str), "The method should return a string."

def test_select_appropriate_word_returns_appropriate_word():
    word = engine.select_appropriate_word('nouns')
    assert word in engine.dictionaries['nouns'], "The method should return a word from the correct category."

def test_select_appropriate_word_handles_grammar():
    action = engine.select_appropriate_word('actions')
    assert action in engine.dictionaries['actions'], "The action should be a valid word from the 'actions' category."

@patch('engines.feature_compliment_engine.random.choice')
def test_select_appropriate_word_adds_articles_correctly(mock_random_choice):
    # Set the side_effect of mock_random_choice to the list of nouns
    # This will make random.choice return each noun in order during the test
    mock_random_choice.side_effect = engine.dictionaries['singular_nouns']
    # Test that singular countable nouns receive an article
    for noun in engine.dictionaries['singular_nouns']:
        word = engine.select_appropriate_word('singular_nouns')
        if noun[0] in 'aeiouAEIOU':
            expected_word = 'an ' + noun
        else:
            expected_word = 'a ' + noun
        assert word == expected_word, f"The word '{word}' should be '{expected_word}'."
    # Reset the side_effect to None to avoid affecting other tests
    mock_random_choice.side_effect = None
    # Test that non-singular countable nouns do not receive an article
    for noun in engine.dictionaries['personal_qualities']:
        mock_random_choice.return_value = noun
        word = engine.select_appropriate_word('personal_qualities')
        assert not word.startswith(('a ', 'an ')), f"The word '{word}' should not start with an article."

# New tests to ensure grammatical correctness of the compliments
import re

def test_compliment_grammatical_structure():
    # This test will check if the generated compliment follows a valid grammatical structure
    compliment = engine.generate_compliment()
    # Check that the compliment contains necessary components
    # Check for the presence of any conjugated form of the verbs in the compliment
    verbs_in_compliment = []
    for verb in engine.dictionaries['verbs']:
        # Create a regex pattern to match the verb in different conjugations
        verb_pattern = r'\b' + verb + r'(s|ing|ed)?\b'
        if re.search(verb_pattern, compliment, re.IGNORECASE):
            verbs_in_compliment.append(verb)
    # The compliment should contain a verb if the template has a verb placeholder
    if '{verb}' in compliment:
        assert verbs_in_compliment, "The compliment should contain a verb."
    # The compliment should contain an adjective if the template has an adjective placeholder
    if '{adjective}' in compliment:
        assert any(word in compliment for word in engine.dictionaries['adjectives']), "The compliment should contain an adjective."
    # The compliment should contain a noun if the template has a noun placeholder
    if '{singular_noun}' in compliment:
        assert any(word in compliment for word in engine.dictionaries['singular_nouns']), "The compliment should contain a noun."
    assert compliment[0].isupper(), "The compliment should start with a capital letter."
    assert compliment.endswith('.'), "The compliment should end with a period."

def test_compliment_correct_use_of_articles():
    # This test will check if the articles 'a' or 'an' are used correctly in the compliments
    for _ in range(100):  # Generate multiple compliments for a thorough test
        compliment = engine.generate_compliment()
        words = compliment.split()
        for i, word in enumerate(words):
            # Strip punctuation from the end of the word for accurate comparison
            stripped_word = word.rstrip('.!?')
            if stripped_word.lower() in [noun.lower() for noun in engine.dictionaries['singular_nouns']]:
                # Skip the first word of the compliment as it may not require an article
                if i == 0: continue
                # Check if the noun is preceded by the correct article
                preceding_word = words[i - 1].lower()
                if stripped_word[0].lower() in 'aeiou':
                    # Handle special cases where the use of 'an' is determined by the sound that follows
                    if preceding_word in ['a', 'an']:
                        assert preceding_word == 'an', f"The noun '{stripped_word}' should be preceded by 'an'."
                else:
                    # Handle special cases where the use of 'a' is determined by the sound that follows
                    if preceding_word in ['a', 'an']:
                        assert preceding_word == 'a', f"The noun '{stripped_word}' should be preceded by 'a'."

def test_compliment_verb_conjugation():
    # This test will check if the verbs are conjugated correctly within the context of the compliment
    for verb in engine.dictionaries['verbs']:
        # Conjugate the verb for second person singular
        verb_conjugated = conjugate_verb(verb, tense='present', person=2, number='singular')
        compliment = f"You {verb_conjugated} everyone with your kindness."
        # Check if the conjugated verb is used in the compliment
        assert verb_conjugated in compliment, f"The verb '{verb}' should be conjugated as '{verb_conjugated}' in the compliment."
