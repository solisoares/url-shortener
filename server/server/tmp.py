from configparser import ConfigParser
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRETS = BASE_DIR / "secrets.cfg"
PARSER = ConfigParser()
PARSER.read(SECRETS)

print(PARSER.get("DATABASE", "NAME"))
print(PARSER.get("DATABASE", "USER"))
print(PARSER.get("DATABASE", "PASSWORD"))

