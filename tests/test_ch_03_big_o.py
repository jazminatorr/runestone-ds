import pytest
from src.ch_03_complexity_analyisis import ch_03_04_annagram_example as annagram

class TestIsAnnagram:

    @pytest.mark.parametrize(
        "str1, str2, expected_result",
        [
            ("jazmin", "jizman", True),
            ("jazmin", "JIZMAN", True),
            ("jazmin", "alejan", False)
        ]
    )
    def test_annagram_first(self, str1: str, str2: str, expected_result):
        assert annagram.is_annagram_01(str1, str2) == expected_result, \
        f"Expected {str1} to be an annagram of {str2}: {expected_result}"

    @pytest.mark.parametrize(
        "str1, str2, expected_result",
        [
            ("jazmin", "jizman", True),
            ("jazmin", "JIZMAN", True),
            ("jazmin", "alejan", False)
        ]
    )
    def test_annagram_second(self, str1: str, str2: str, expected_result):
        assert annagram.is_annagram_02(str1, str2) == expected_result, \
        f"Expected {str1} to be an annagram of {str2}: {expected_result}"

    @pytest.mark.parametrize(
        "str1, str2, expected_result",
        [
            ("jazmin", "jizman", True),
            ("jazmin", "JIZMAN", True),
            ("jazmin", "alejan", False)
        ]
    )
# TODO: Uncomment this test when is_annagram_03() is implemented
#    def test_annagram_third(self, str1: str, str2: str, expected_result):
#        assert annagram.is_annagram_03(str1, str2) == expected_result, \
#        f"Expected {str1} to be an annagram of {str2}: {expected_result}"
#        pass

    @pytest.mark.parametrize(
        "str1, str2, expected_result",
        [
            ("jazmin", "jizman", True),
            ("jazmin", "JIZMAN", True),
            ("jazmin", "alejan", False)
        ]
    )
    def test_annagram_fourth(self, str1: str, str2: str, expected_result):
        assert annagram.is_annagram_04(str1, str2) == expected_result, \
        f"Expected {str1} to be an annagram of {str2}: {expected_result}"