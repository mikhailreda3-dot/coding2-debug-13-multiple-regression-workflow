"""Display your Homework 2 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "20eb8b31fcf2a801727baa3bbf8d2f8d"
GRADE_HASH = "007c12338173e825d1fbbc9f624d019adb1a54def06c4509f791ba439e3de2c1"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 2: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
