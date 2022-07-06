<h2> <a href="https://github.com/ShubhPatil95/DVC-04-Simple_DVC_Project"> 05-DVC_Metrics_Tracking </a></h2>

<p>
<strong> In this tutorial we will see how DVC helps to track the metrics and reproduce the projects </strong>

### Step1
* Create a folders under name DVC-05-Metrics_Tracking. Further create a code.py and Iris_Flower_Dataset.csv files and reports folder inside of DVC-05-Metrics_Tracking.
```ruby
mkdir DVC-05-Metrics_Tracking
cd DVC-05-Metrics_Tracking
touch code.py Iris_Flower_Dataset.csv
mkdir reports
```
### Step2
* Initiate the Git and DVC
```ruby
git init
dvc init
``` 

``` 
### Step3
* Create a github repository under name DVC-05-Metrics_Tracking and add git remote repository.
```ruby
git remote add origin https://github.com/ShubhPatil95/DVC-05-Metrics_Tracking.git
```

### Step4  
* Copy and paste containt of code.py and Iris_Flower_Dataset.csv from here [code.py](https://github.com/ShubhPatil95/DVC-05-Metrics_Tracking/blob/main/code_initial.py) and [Iris_Flower_Dataset.csv](https://raw.githubusercontent.com/ShubhPatil95/DVC-05-Metrics_Tracking/main/Iris_Flower_Dataset.csv)


### Step5
* Lets run code.py and see the outputs and you will see outputs shown below.
```ruby
python3 code.py
```
<br>Outputs:
<br>Accuracy==> 0.9666666666666667
<br>Recall==> 0.9666666666666667
<br>Precision==> 0.9692307692307692

### Step6
* Now, if you want to change the hyperameters of model then you should have to make changes in code.py. Which is not a easy and convenient option.
* Hence, here we will keep all those hyperameter in seperate file name params.yaml and code.py will read those parameters from params.yaml. So if we want to change any paramters now we have to just change the params.yaml instead of code.py

### Step7
* Create an file params.yaml which will stores all those parameters of code.py. Just copy and paste params.yaml from here [params.yaml](https://github.com/ShubhPatil95/DVC-05-Metrics_Tracking/blob/3371603cdbcaf07d710e35676139ec72ee15054d/params.yaml)
```ruby
touch params.yaml
```
### Step8
* Now in code.py, provide all hyperparamters reading from params.yaml. Just copy and paste updated code.py from here[code.py](https://github.com/ShubhPatil95/DVC-05-Metrics_Tracking/blob/b4181cb7feefd8c6b2a6f8eb97f6edb75ba7bfb6/code.py)
* In updated code.py we are exporting 2 file, scores.json and params.json in foler name: reports. These are the 2 file are tracking our metrics and same names are mentioend on params.yaml as well.

### Step7
* Lets run a code.py and you will now see output as below.
```ruby
python3 code.py
```
<br>Outputs:
<br>Accuracy==> 0.9666666666666667
<br>Recall==> 0.9666666666666667
<br>Precision==> 0.9692307692307692

### Step8
* Create a dvc.yaml file. Copy and paste dvc.yaml from [dvc.yaml](https://github.com/ShubhPatil95/DVC-05-Metrics_Tracking/blob/b4181cb7feefd8c6b2a6f8eb97f6edb75ba7bfb6/dvc.yaml)
* Here in this example we only have one stage name, create_model.
* This will keep the details of stages, dependencies,parameters,metrics and outputs ofeach stage.
```ruby
touch dvc.yaml
```

### Step9
* Run a command dvc repro, which will run dvv.yaml file which will trigger code.py.
* Run a command dvc dag, which show the component of pipeline in block diagram.
* Run a command dvc metrics show, which will show the metrics and parameters of current execution.
```ruby
dvc repro
dvc dag
dvc metrics show
```
### Step10
*Push the changes to github
```ruby
git add .
git commit -m "First Commit"
git branch -M main 
git push -u origin main
```
## Step11
*Now just change below 2 parameters in params.yaml and run dvc repro and see the revised results.
  <br>random_state: 20
  <br>test_size: 0.5
```ruby
dvc repro
```
<br>Accuracy==> 0.8266666666666667
<br>Recall==> 0.8266666666666667
<br>Precision==> 0.8533333333333334

## Step12
*To see a metrics of current execution, run a command dvc metrics show
*To see difference in current execution and last committed execution run a command dvc metrics diff
```ruby
dvc metrics show
dvc metrics diff
```
### Step13
*Push the changes to github
```ruby
git add .
git commit -m "Second Commit"
git push -u origin main
```
</p>


