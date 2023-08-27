# This is a sample Python script.
import math
import sys

import pytest


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

@pytest.mark.skipif(sys.version_info[0] == 2, reason="Only Python3")
def test_sqrt():
    assert math.sqrt(4) == 2


def test_sqrt_for_nine():
    assert math.sqrt(9) == 3
    assert 1/0 == 0


@pytest.mark.xfail
def test_sqrt_for_nine_failed():
    assert math.sqrt(9) == 2.5



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
