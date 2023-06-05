from app.password import password_verification, mistakes_messages
import pytest

@pytest.mark.password
@pytest.mark.positive
@pytest.mark.parametrize('valid_password', ["Qwerty1!", "dAfsfaa1@", "Asdfghjklqwert#tyuiopLkjhgfdsa7",
                                            "HauvfabdiubdiHGHYscjhdbshadshbjbasdvbasdbvlajHHHsdbvja1sbdjvbsd$"],
                         ids=['Valid password include 8 chars', "Valid password include 9 chars",
                              "Valid password include 31 chars", "Valid password include 64 chars"])
def test_positive_value_of_password(valid_password):
    """Password tests include positive data"""
    login = 'maxim@gmail.com'
    assert password_verification(login, valid_password) == True

@pytest.mark.password
@pytest.mark.negative
@pytest.mark.parametrize('invalid_password', ["", "Aa1!@#$", "abc1!@#$", "3B!K@E#$G",
                                              "98Kdaf767hbS",
                                              "jabvjkabrvhbakjhfbvjasbvjhajhvrb#zsjfhajbvjLDvbjgichjslvvkzkLvfb",
                                              "123Afmaxim!@#$*&-"],
                         ids=['0 chars', "7 valid chars", "8 chars without uppercase",
                              "9 chars without lowercase", "12 chars without special chars !@#$",
                              "64 chars without digits", "include substring from login"])
def test_negative_value_of_password(invalid_password):
    """Password tests include negative data"""
    login = 'maxim@gmail.com'
    assert password_verification(login, invalid_password) in mistakes_messages.values(), "Password valid!"


