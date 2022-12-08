import sys

def read_data(day: str, arg: str):
    file_ending = "a" if arg != "test" else "test"
    filename = f"data/{day}_{file_ending}"
    with open(filename) as file:
        return file.read()

if __name__ == "__main__":
    try:
        day = sys.argv[1]
        file_arg = "test"
        if len(sys.argv) > 2 and sys.argv[2] in ["a", "test", "b"]:
            file_arg = sys.argv[2]
        exec(f"from code.{day} import main")
        main(file_arg, read_data(day, file_arg))

    except IndexError as exc:
        print(exc)
        raise SystemExit(f"Which day should we run? Write in numbers")