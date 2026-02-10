from src.utils.password.managet import PasswordManager


def test_password_hash_and_check_roundtrip() -> None:
    plain = "StrongPass1!"
    hashed = PasswordManager.hash(plain)

    assert isinstance(hashed, str)
    assert hashed != plain
    assert PasswordManager.check(plain, hashed) is True


def test_password_check_fails_for_wrong_password() -> None:
    plain = "StrongPass1!"
    wrong = "WrongPass1!"
    hashed = PasswordManager.hash(plain)

    assert PasswordManager.check(wrong, hashed) is False
