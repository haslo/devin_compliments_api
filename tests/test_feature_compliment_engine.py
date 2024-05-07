import pytest
from unittest.mock import patch
from engines.feature_compliment_engine import FeatureComplimentEngine

# Mock dictionaries for testing
mock_dictionaries = {
    'quality_templates': [
        "{feature} is as {adjective} as a {natural_phenomenon}, truly {positive_adjective}.",
        "You have the {positive_trait} of a {celestial_body}, always {action}.",
        "Your {personal_quality} shines brighter than a {shiny_object}, {verb} everyone."
    ],
    'features': ['wisdom', 'kindness', 'strength'],
    'adjectives': ['bright', 'warm', 'inviting'],
    'actions': ['inspiring others', 'lifting spirits'],
    'positive_adjectives': ['amazing', 'incredible', 'remarkable'],
    'person_roles': ['friend', 'mentor', 'leader'],
    'personal_qualities': ['generosity', 'creativity', 'passion'],
    'natural_phenomena': ['sunset', 'ocean wave', 'mountain peak'],
    'positive_traits': ['grace', 'determination', 'humility'],
    'celestial_bodies': ['star', 'planet', 'comet'],
    'positive_things': ['adventure', 'journey', 'experience'],
    'shiny_objects': ['gem', 'diamond', 'treasure'],
    'verbs': ['enlightens', 'uplifts', 'encourages'],
    'action_templates': [
        "You {verb} everyone with your {adjective} {noun}.",
        "Your ability to {verb} is {adjective} and {positive_adjective}, like a {noun}."
    ],
    'singular_nouns': ['smile', 'laughter', 'style', 'approach', 'perspective', 'insight', 'dedication', 'spirit', 'energy', 'presence', 'eagle', 'dolphin', 'lion', 'moon', 'sun', 'constellation', 'diamond', 'butterfly', 'work of art', 'genius', 'star', 'talent', 'prodigy', 'wizard', 'champion', 'eyes', 'adventure', 'masterpiece', 'journey', 'idea', 'performance', 'soul', 'painting', 'star', 'gemstone', 'lantern', 'firefly', 'candlelight', 'sunrise', 'moonbeam', 'glitter', 'sparkle', 'gleam']
}

# Initialize the FeatureComplimentEngine with mock dictionaries
engine = FeatureComplimentEngine(mock_dictionaries)

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
    word = engine.select_appropriate_word('features')
    assert isinstance(word, str), "The method should return a string."

def test_select_appropriate_word_returns_appropriate_word():
    word = engine.select_appropriate_word('features')
    assert word in mock_dictionaries['features'], "The method should return a word from the correct category."

def test_select_appropriate_word_handles_grammar():
    action_phrase = engine.select_appropriate_word('actions')
    assert action_phrase.startswith('to '), "The action phrase should start with 'to ' if it is more than one word."

@patch('engines.feature_compliment_engine.random.choice')
def test_select_appropriate_word_adds_articles_correctly(mock_random_choice):
    # Set the side_effect of mock_random_choice to the list of nouns
    # This will make random.choice return each noun in order during the test
    mock_random_choice.side_effect = mock_dictionaries['singular_nouns']
    # Test that singular countable nouns receive an article
    for noun in mock_dictionaries['singular_nouns']:
        word = engine.select_appropriate_word('features')
        if noun[0] in 'aeiouAEIOU':
            expected_word = 'an ' + noun
        else:
            expected_word = 'a ' + noun
        assert word == expected_word, f"The word '{word}' should be '{expected_word}'."
    # Reset the side_effect to None to avoid affecting other tests
    mock_random_choice.side_effect = None

    # Test that non-singular countable nouns do not receive an article
    for noun in mock_dictionaries['personal_qualities']:
        mock_random_choice.return_value = noun
        word = engine.select_appropriate_word('personal_qualities')
        assert not word.startswith(('a ', 'an ')), f"The word '{word}' should not start with an article."

# New tests to ensure grammatical correctness of the compliments
def test_compliment_grammatical_structure():
    # This test will check if the generated compliment follows a grammatical structure
    compliment = engine.generate_compliment()
    # Check that the compliment contains necessary components
    assert 'Your' in compliment or 'You' in compliment, "The compliment should address the recipient directly."
    # Check for the presence of a verb in the expected position within the compliment
    verb_detected = False
    for template in mock_dictionaries['action_templates']:
        if '{verb}' in template:
            # Find the position of the placeholder in the template
            verb_position = template.split().index('{verb}')
            # Split the compliment into words and get the word at the expected verb position
            compliment_words = compliment.split()
            if len(compliment_words) > verb_position:
                # Check if the word at the expected position is a verb
                verb_detected = compliment_words[verb_position].rstrip('.').lower() in [verb.lower() for verb in mock_dictionaries['verbs']]
                if verb_detected:
                    break
    print(f"Generated compliment: {compliment}")  # Debugging output
    assert verb_detected, "The compliment should contain a verb in the expected position."
    print(f"Adjectives in mock dictionary: {mock_dictionaries['adjectives']}")  # Debugging output
    assert any(adjective in compliment for adjective in mock_dictionaries['adjectives']), "The compliment should contain an adjective."
    assert any(noun in compliment for noun in mock_dictionaries['singular_nouns']), "The compliment should contain a noun."
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
            if stripped_word.lower() in [noun.lower() for noun in mock_dictionaries['singular_nouns']]:
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
    for verb in mock_dictionaries['verbs']:
        compliment = f"You {verb} everyone with your kindness."
        assert verb.endswith('s'), "The verb should be conjugated correctly, ending with 's' in the present tense."
