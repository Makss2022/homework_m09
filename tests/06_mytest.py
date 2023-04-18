

from pathlib import Path


result = Path(__file__).absolute().parent.parent.joinpath("qoutes.json")

print(result)
