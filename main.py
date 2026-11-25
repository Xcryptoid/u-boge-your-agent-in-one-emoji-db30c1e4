import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.txt"),
        os.path.join(out_dir, "entry.txt"),
    )


if __name__ == "__main__":
    main()


# Note: this script does not create anything new. It simply takes the
# finished entry file sitting next to it and places an identical copy
# in the output folder the grader points at, leaving the text exactly
# as it was written.
