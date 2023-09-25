from pathlib import Path

ROOT_PATH = Path(__file__).parent
CHROME_DRIVER_PATH = ROOT_PATH / "bin" / "chromedriver"

WAITING_TIME = 5

if __name__ == "__main__":
    print("ROOT DIR: " + ROOT_PATH, "\nCHROME DRIVER PATH: " + CHROME_DRIVER_PATH)
