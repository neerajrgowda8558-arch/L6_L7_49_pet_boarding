
import pytest
from pet_boarding import boarding_fee, admission_ok, checkout_status


def test_included_days():
    assert boarding_fee("dog", 1, False) == 0


def test_unknown_pet():
    with pytest.raises(ValueError):
        boarding_fee("bird", 3, False)


def test_negative_days():
    with pytest.raises(ValueError):
        boarding_fee("cat", -1, False)


def test_premium_pet():
    assert boarding_fee("cat", 5, True) == 20


def test_dog_extra_days():
    assert boarding_fee("dog", 5, False) == 90


def test_cat_extra_days():
    assert boarding_fee("cat", 5, False) == 40


def test_long_stay_dog():
    assert boarding_fee("dog", 15, False) == 585


def test_long_stay_cat():
    assert boarding_fee("cat", 15, False) == 360


def test_senior_admission():
    assert admission_ok(10, 3, True) is True


def test_young_pet():
    assert admission_ok(0, 3, False) is False


def test_normal_admission():
    assert admission_ok(4, 2, False) is True


def test_checkout_open():
    assert checkout_status(40, True, False) == "open"


def test_checkout_late():
    assert checkout_status(20, True, False) == "late"


def test_checkout_closed():
    assert checkout_status(0, True, False) == "closed"


def test_checkout_weekend():
    assert checkout_status(40, False, True) == "open"


def test_checkout_normal():
    assert checkout_status(20, False, False) == "open"
