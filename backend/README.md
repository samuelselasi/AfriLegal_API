# Backend Infrastructure

## Content

* [About](#about)
* [Environment](#environment)
* [Modules](#modules)
* [Files](#files)


## About

This directory contains different modes
of AfriLegal API backend infrastructure
. Each module represents a milestone
in development and testing. Thus, they
have different setup requirements to
successfully build and run.

Also included are [Docker](https://www.docker.com/)
files to containarise the [latest module](./api)
. Same procedure can be followed to build the older
modules as well with just minor changes.

Further information on the modules can
be found in their respective README.md
files.


## Environment

This guide provides step-by-step instructions on
setting up the required environment to run a FastAPI
backend application using `Python 3.8.10` on `Ubuntu 20.04`.

### Prerequisites

Before you begin, make sure you have the following:

* Ubuntu 20.04 installed on your system.
* Python 3.8.10 or later installed. ***Note***:
 *later python versions may require slight changes
in implementation of some modules as opposed to
what is available in this repository. To avoid 
those troubles you can doengrade or run in a python environment.*
* Basic familiarity with the command line.

### Setup

##### 1. Update System Packages

```
sudo apt update
sudo apt upgrade
```
##### 2. Install `pip` (Python Package Management)

```
sudo apt install python3-pip
```
##### 3. Create Virtual Environment

Virtual environments allow you to isolate project 
dependencies. Create and activate a virtual 
environment using the following commands:

```
sudo apt install python3.8-venv
python3.8 -m venv myenv
source myenv/bin/activate
```
##### 4. Install Dependencies

```
sudo pip install -r requirements.txt
```

##### 5. Setup Database
tbc...

## Modules

* [FastAPI + PostgreSQL](./api) (*Latest, Complete with all features*)
* [FastAPI + PostgreSQL](./app) (*No authentication, Routers available & scalable*)
* [FastAPI + PostgreSQL](./test_app) (*No authentication, No routers,  Not scalable*)
