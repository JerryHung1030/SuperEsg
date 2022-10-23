# ESGKiller

This project will automatically fill in the "Love Earth Diary" of cdri esp.

## Directory structure

```
├── build
├── dist
│   └── ESGKiller.exe
├── ESGKiller.py
├── ESGKiller.spec
└── README.md
```
## Version

```
20221023 v1.0 - provide basic functions.
```

## Run

This executable file will automatically fill in Love Earth Diary, and the values ​​in the form will be filled in with random value.

Mondays : will automatically fill in the previous Saturday and Sunday and today's forms.
from Tuesday to Friday : fill in today's forms.
This executable can also specify the date you want to fill in. The format needs to meet the following specifications : yyyy-mm-dd.
Detailed instructions for use are as follows :

__AutoChoosingDate__

```
    double click ESGKiller.exe in the folder dist/
```

__SpecificDate__

```
    open cmd.exe
    cd SuperEsg\dist\
    ESGKiller.exe [yyyy-mm-dd]
    ex : ESGKiller.exe 2022-10-20
```