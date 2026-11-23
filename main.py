import os

TEXT = (
    "NATO meets over Russian missiles in Poland, Gaza counts three more dead, "
    "Nepal's PM meets Modi, and Verstappen wins Las Vegas - one front page, "
    "a whole world holding its breath."
)


def main():
    assert len(TEXT) <= 200, f"entry is {len(TEXT)} code points, over the 200 limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
