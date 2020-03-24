# NYC Open Parking and Camera Violation 
![](https://media.giphy.com/media/tAB101YENjLdC/giphy.gif)
### Data source: [Open Parking and Camera Violations](https://dev.socrata.com/foundry/data.cityofnewyork.us/nc67-uf89)

Through this project, you will 
1. Leverage a python client of the Socrata API to connect to the Open Parking and Camera Violations (OPCV) API.
2. Load all the data into an ElasticSearch instance.
3. Visualize / analyze with Kibana.  

* Software Require: Docker Desktop

## Part 1 Python Scripting
To support the command line arguments:

**$ docker run -e APP_KEY={YOUR_APP_KEY} -t bigdata:1.0 python main.py int int results.json**

*int1 = page_size, int2 = num_pages, result.json = output* :sweat:
```console
Structure:
    bigdata
    +-- Dockerfile
    +-- main.py
    +-- requirements.txt
    +-- src
    |   +-- api.py
```
```
Dockerfile: image (contain all the setting we need)
requirement.txt: packages we need
main.py: Program that allow us to use command line as the trigger
api.py: contain our self-define function, helping us to get data by using api
```
## Part 2 Loading into ElasticSearch
For part 2, I revise the code in bigdata and create the folder 'part 2'

To support the command line arguments:

**docker-compose run -e APP_KEY={YOUR_APP_KEY} -v ${pwd}:/app pyth python -m main --page_size=int --num_pages=int --output=result.json --elastic=True --index=index_name**

*Optional:*

*--num_pages, the program will load all the data if you did not specify.*

*--output, If not provided, your script should simply print results to stdout. If provided, your script should write the data to the file (in this case, results.json).*

*--elastic, upload to elasticsearch*

*--index, name your index*

## Part 3 Visualizing and Analysis on Kibana
* Timeline of the data

![](https://github.com/mendel462/BigData_OCVA-/blob/master/part%203/Kibana.PNG)
* Dashboard!!! :satisfied:

![](https://github.com/mendel462/BigData_OCVA-/blob/master/part%203/Kibana%20Dashboard.png)
