# Team 16 (Green Coders) - Solar Offset

This is the repository created for the purpose of COM6103 Team Software Project.

## Team Composition

|        **Name**       | **Team** |
|:---------------------:|:--------:|
|      Fathiya Umer     | Frontend |
| Jithendran Adikesavan |  Backend |
|    Maitreya Gurjar    |  Backend |
|      Ruiyong Cao      | Frontend |
|       Ruoxun Xu       | Frontend |
|      Thania Vivek     |  Backend |


## Front-end Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## How to run the application

### Running with Docker

If you are running on x86 based operating system, you can run with the following command
```
$ docker-compose -f docker-compose.yml -f docker-compose-x86.yml up
```

If you are running on arm based operating system, you can run with the following command
```
$ docker-compose -f docker-compose.yml -f docker-compose-arm64.yml up
```

## Style-check for Python
The support for linting python code has been added. To get the report as a text file, run the following command in the terminal
```
$ pylint flask_app/ --rcfile=pylintrc.ini > pylint_report.txt
```

The report will be generated with the filename pylint_report.txt. 
Please ensure your code always evaluates above 8 on 10.
