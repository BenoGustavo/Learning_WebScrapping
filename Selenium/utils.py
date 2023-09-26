from pathlib import Path
from sys import platform

UNIX_SYSTEMS = ["linux", "linux2", "darwin"]

ROOT_PATH = Path(__file__).parent

# if the platform is a unix based system
if platform in UNIX_SYSTEMS:
    CHROME_DRIVER_PATH = ROOT_PATH / "bin" / "chromedriver"
# else is windows
else:
    CHROME_DRIVER_PATH = ROOT_PATH / "bin" / "chromedriver.exe"

WAITING_TIME = 5

if __name__ == "__main__":
    print("Your platform is: " + platform)
    print(
        "ROOT DIR: " + str(ROOT_PATH),
        "\nCHROME DRIVER PATH: " + str(CHROME_DRIVER_PATH),
    )
