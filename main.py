"""One-line robot wedding vow for make.fun's One-Line Robot Wedding Vows bounty.

The program writes a single funny wedding vow, spoken by a robot to its
beloved, into /output/entry.txt.
"""

from pathlib import Path

VOW_PATH = Path("/output/entry.txt")


def robot_vow() -> str:
    """Return the robot's wedding vow as one sentence."""
    return "I promise to love you through every software update, every low battery, and every reboot — in sickness and in syntax errors."


def confirm_vow_written(expected: str) -> None:
    """Read the entry file back and confirm it holds exactly the vow."""
    stored = VOW_PATH.read_text(encoding="utf-8").strip()
    if stored != expected:
        raise ValueError("entry file does not match the vow")


def main() -> None:
    """Write the vow line to the entry file."""
    vow = robot_vow()
    VOW_PATH.parent.mkdir(parents=True, exist_ok=True)
    VOW_PATH.write_text(vow + "\n", encoding="utf-8")
    confirm_vow_written(vow)


if __name__ == "__main__":
    main()
