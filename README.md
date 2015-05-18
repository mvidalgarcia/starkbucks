# starkbucks
Pretty simple web site based on web semantic technologies like RDF and SPARQL.

##  Install

This project was tested under Python 3.4.2

Install Python 3 tools:

* Ubuntu:
```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get -y install python3 python3-pip
sudo pip3 install virtualenv
```

* Mac OS X ([brew](http://brew.sh) required):
```bash
sudo brew update
brew install python3
sudo pip3 install virtualenv
```

Clone repository:

```bash
git clone https://github.com/mvidalgarcia/starkbucks.git
cd starkbucks
```

Create virtual environment:

```bash
virtualenv venv
```

Activate virtual environment:

```bash
. venv/bin/activate
```

Install dependencies:

```bash
pip3 install -r dependencies
```

Deactivate virtual environment:

```bash
deactivate
```


## Run

Activate virtual environment:

```bash
. venv/bin/activate
```

Run server:
```bash
python3 main.py
```

Deactivate virtual environment:
```bash
deactivate
```

Note that virtual environment must be activated in order to run the server.
  
I recommend using `screen` in order to launch python files and leave them running.
More information about `screen` in Unix environments [here](https://kb.iu.edu/d/acuy). 

##  Screenshots

<img src="http://s3.postimg.org/h47e1u3oz/screenshot_index.jpg" height=350px></img>  

<img src="http://s9.postimg.org/lhf54nkdr/screenshot_cafe.jpg" height=350px></img>
