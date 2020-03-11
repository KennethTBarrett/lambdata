# lambdata
Lambda School Unit 3 - Lambdata Package

## Installation

First, install the repository from GitHub, then navigate there via command line:

```sh
cd path/to/lambdata
```

## Install Package Dependencies:
```sh
pipenv install
```

## Install Package from Test PiPy
```py
pip install -i https://test.pypi.org/project/lambdata-KennethTBarrett/0.0.1/

```

## Usage

```py
from lambdata.dt import date_splitter, time_splitter

date_splitter(df, 'Column') # Split dates from column in df 'Column', make new columns, and drop the original. Month, Day, Year

time_splitter(df, 'Column') # Split times from column in df 'Column', make new columns, and drop the original. Hour, Minute, Second

```

Required Libraries:
```sh
requirements.txt
```