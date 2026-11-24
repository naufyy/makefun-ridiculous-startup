#!/usr/bin/env python3
"""Write the make.fun entry pitch to /output/entry.txt."""
import os

PITCH = (
    "We flush strangers' toilets for a living: snowbirds pay $30 a week so "
    "dry drain traps don't fill their empty Florida condos with sewer gas "
    "and roaches."
)


def main() -> None:
    assert PITCH.strip(), "pitch is blank"
    assert 1 <= len(PITCH) <= 200, f"pitch length {len(PITCH)} out of range"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)
    print(PITCH)
    print(f"length: {len(PITCH)}")


if __name__ == "__main__":
    main()
