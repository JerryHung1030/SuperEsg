# ESGKiller

This project will automatically fill in the "Love Earth Diary" of cdri esp.

## Directory structure

```
├── build
│   └── ...
├── dist
│   ├── ESGKiller_macOs
│   │   ├── ...
│   │   └── ESGKiller
│   └── ESGKiller.exe
├── ESGKiller.py
├── ESGKiller.spec
└── README.md
```
## Version

```
20221023 v1.0 - provide basic functions.
20221027 v1.1 - add two args (-speficy yyyy-nn-dd, -days [1-5] ).
20221110 v1.2 - fix some bugs
```

## Run

This executable file will automatically fill in Love Earth Diary, and the values ​​in the form will be filled in with random value.
Detailed instructions for use are as follows :

__default__

```
(MON)      : Automatically fill in the previous Saturday and Sunday and today's forms.
(TUE->FRI) : Automatically fill in today's forms.
```

```
    # double click ESGKiller.exe in the folder dist/
```

__Specify Date__

This executable can also specify the date you want to fill in. 
Notes : The format needs to meet the following specifications : yyyy-mm-dd.
ex : ESGKiller.exe 2022-10-20

```
    # open cmd.exe
    cd SuperEsg\dist\
    ESGKiller.exe -speficy yyyy-mm-dd
```

__days want to fill__

According to how many days you want to fill out the form

```
    # open cmd.exe
    cd SuperEsg\dist\
    ESGKiller.exe -daysbefore [1-5]
```