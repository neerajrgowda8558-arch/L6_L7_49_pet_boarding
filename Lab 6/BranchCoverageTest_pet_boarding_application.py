
import pytest
from pet_boarding import boarding_fee, admission_ok, checkout_status


@pytest.mark.parametrize("pet,days,premium,expected", [
    ("dog", 1, False, 0),
    ("cat", 4, True, 0),
    ("rabbit", 5, True, 20),
    ("dog", 5, False, 90),
    ("cat", 5, False, 40),
    ("dog", 15, False, 585),
    ("cat", 15, False, 360),
    ("dog", 3, True, 0),
    ("rabbit", 4, False, 0),
])
def test_boarding_branches(pet, days, premium, expected):
    assert boarding_fee(pet, days, premium) == expected


def test_unknown_pet():
    with pytest.raises(ValueError):
        boarding_fee("bird", 3, False)


def test_negative_days():
    with pytest.raises(ValueError):
        boarding_fee("cat", -1, False)


@pytest.mark.parametrize("age,vaccinations,senior,expected", [
    (10, 3, True, True),
    (10, 2, True, False),
    (0, 3, False, False),
    (4, 2, False, True),
    (4, 1, False, False),
])
def test_admission_branches(age, vaccinations, senior, expected):
    assert admission_ok(age, vaccinations, senior) is expected


@pytest.mark.parametrize("minutes,long_stay,weekend,expected", [
    (40, True, False, "open"),
    (20, True, False, "late"),
    (0, True, False, "closed"),
    (20, False, False, "open"),
    (10, False, False, "late"),
    (-1, False, False, "closed"),
    (40, False, True, "open"),
    (25, False, True, "late"),
    (0, False, True, "closed"),
])
def test_checkout_branches(minutes, long_stay, weekend, expected):
    assert checkout_status(minutes, long_stay, weekend) == expected
