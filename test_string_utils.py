import pytest
from string_utils import StringUtils

utils = StringUtils()


@pytest.mark.positive
def test_capitalize_positive():
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("Тест") == "Тест"


@pytest.mark.positive
def test_capitalize_numbers_and_dates():
    assert utils.capitalize("123") == "123"
    assert utils.capitalize("04 апреля 2023") == "04 апреля 2023"


@pytest.mark.negative
def test_capitalize_keeps_other_uppercase_bugs():
    assert utils.capitalize("skyPro") == "SkyPro"


@pytest.mark.negative
def test_capitalize_negative_empty():
    assert utils.capitalize("") == ""


@pytest.mark.negative
def test_capitalize_negative_space():
    assert utils.capitalize(" ") == " "


@pytest.mark.negative
def test_capitalize_negative_none():
    with pytest.raises(AttributeError):
        utils.capitalize(None)


@pytest.mark.positive
def test_trim_positive():
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("04 апреля 2023") == "04 апреля 2023"


@pytest.mark.negative
def test_trim_negative_empty():
    assert utils.trim("") == ""


@pytest.mark.negative
def test_trim_negative_space():
    assert utils.trim(" ") == ""


@pytest.mark.negative
def test_trim_negative_none():
    with pytest.raises(AttributeError):
        utils.trim(None)


@pytest.mark.positive
def test_contains_positive():
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("123", "2") is True


@pytest.mark.negative
def test_contains_negative_empty_symbol_bug():
    assert utils.contains("SkyPro", "") is False


@pytest.mark.negative
def test_contains_negative_none():
    with pytest.raises(AttributeError):
        utils.contains(None, "A")


@pytest.mark.positive
def test_delete_symbol_positive():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("04 апреля 2023", "апреля ") == "04 2023"


@pytest.mark.negative
def test_delete_symbol_negative_empty():
    assert utils.delete_symbol("", "A") == ""


@pytest.mark.negative
def test_delete_symbol_negative_none():
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "A")
