# lambdata
Lambda School Unit 3 - Lambdata Package

Using the package from PIPY instructions:

```py
from lambdata.dt import date_splitter, time_splitter

date_splitter(df, 'Column') # Split dates from column in df 'Column', make new columns, and drop the original. Month, Day, Year

time_splitter(df, 'Column') # Split times from column in df 'Column', make new columns, and drop the original. Hour, Minute, Second

```

```sh
cd path/to/lambdata
```

Install Package Dependencies:
```sh
pipenv install
```