import sys

from library import ensure_library
from search import KINDS, main


if __name__ == "__main__":
    try:
        main(lambda: ensure_library(check_updates="--show" not in sys.argv[1:]), kinds=tuple(k for k in KINDS if k != "群问题"))
    except (OSError, ValueError, RuntimeError) as exc:
        sys.exit(str(exc))
