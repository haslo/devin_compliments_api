import pytest
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
    'verbs': ['enlightens', 'uplifts', 'encourages']
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
