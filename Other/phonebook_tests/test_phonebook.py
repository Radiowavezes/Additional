import pytest
from phonebook import app_run, add_new, delete, update, search_by_first_name


def test_add_new(monkeypatch):

    def patched_input(prompt=''):
        yield "a"
        yield "Mark"
        yield "Zuckerberg"
        yield "0971234567"
        yield "Chernivtsi"
        yield "e"
    generator = patched_input()
    monkeypatch.setattr('builtins.input', lambda _: next(generator))

    app_run('contacts.json')


def test_search_by_first_name(monkeypatch):
    def patched_input(prompt=''):
        yield "s"
        yield "Mark"
        yield "e"
    generator = patched_input()
    monkeypatch.setattr('builtins.input', lambda _: next(generator))

    app_run('contacts.json')


# make tests isolated
# make a fixture that creates 'contacts.json' and cleans it after the test