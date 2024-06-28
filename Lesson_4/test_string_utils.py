import pytest
from string_utils import StringUtils

@pytest.fixture
def utils():
    return StringUtils()

def test_capitalize(utils):
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("hello") == "Hello"
    assert utils.capitilize("") == ""

def test_trim(utils):
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("hello") == "hello"
    assert utils.trim("") == ""

def test_to_list(utils):
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    assert utils.to_list("apple orange banana", " ") == ["apple", "orange", "banana"]
    assert utils.to_list("", ",") == []

def test_contains(utils):
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("SkyPro", "U") is False
    assert utils.contains("Python", "y") is True
    assert utils.contains("", "a") is False

def test_delete_symbol(utils):
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert utils.delete_symbol("hello", "l") == "heo"
    assert utils.delete_symbol("", "a") == ""

def test_starts_with(utils):
    assert utils.starts_with("SkyPro", "S") is True
    assert utils.starts_with("SkyPro", "P") is False
    assert utils.starts_with("apple", "a") is True
    assert utils.starts_with("", "a") is False