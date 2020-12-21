import re

REGEX = r'^(\w+)-(.+)\.osr$'
REGEX_COMPILED = re.compile(REGEX, re.MULTILINE)


def replay_name(name: str) -> bool:
    """
    Validate replay name
    """

    return REGEX_COMPILED.match(name) is not None
