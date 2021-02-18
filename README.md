# Fake Accounts: Theory and Practice 

## CogSec 2021 Workshop

### Devin Gaffney, International Persuasion Machines ([@dgaff_](http://twitter.com/dgaff_))

### Slides

Slides are available as a PDF in this directory or are available in their latest version [here](https://docs.google.com/presentation/d/1jn0y0abV3dMkztHlQjifaqBq0BVPY_fVuOEcmwTqKE0/edit?usp=sharing).
### Installation Instructions

#### Selenium

Unfortunately, there is no single good Selenium installation instruction set - the versions of chrome constantly change, as do chromedriver, as do Firefox versions. In lieu of a single authoritative version, I offer several links that have worked for me historically. Additionally, I provide a link to a `Dockerfile` that sufficiently bootstraps a Python Selenium environment. If you need specific help going forwards, do not hesitate to reach out.

https://blog.testproject.io/2019/07/16/installing-selenium-webdriver-using-python-chrome/
https://www.geeksforgeeks.org/how-to-install-selenium-in-python/
https://alexsl.medium.com/installing-selenium-webdriver-with-python-and-pycharm-from-scratch-on-windows-e4c713043882

As for a Dockerized container for Selenium: https://github.com/joyzoursky/docker-python-chromedriver

#### Everything Else 
```
pip install -r requirements.txt
```
