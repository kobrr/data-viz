# image
![modified.html](https://user-images.githubusercontent.com/58103830/94028049-79795b80-fdf6-11ea-93d3-4aa076ffc205.gif)

---
- Required:
    - R
        - circlepackeR
        - htmlwidgets
    - Python
        - beautifulsoup4         
※ Also fine with only R
---
# 1. Install R on Ubuntu
It also works on the EC2 Ubuntu.
```shell
$ echo -e "\n## For R package"  | sudo tee -a /etc/apt/sources.list
$ echo "deb https://cran.rstudio.com/bin/linux/ubuntu $(lsb_release -cs)-cran35/" | sudo tee -a /etc/apt/sources.list
$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
$ gpg -a --export E298A3A825C0D65DFD57CBB651716619E084DAB9 | sudo apt-key add -
$ sudo apt update
$ sudo apt install r-base
```

# 2. Run the R script
After intalling libs into R, run the R script.
We can get a simple "circlepackeR" figure.
```shell
ubuntu@ip-172-**:~$ sudo apt-get install libcurl4-openssl-dev
ubuntu@ip-172-**:~$ R
> install.packages('remotes')
> remotes::install_github("jeromefroe/circlepackeR")
> install.packages('htmlwidgets')
> install.packages('curl')
```

```vi drawing.R``` 

```shell
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install pandoc
$ Rscript test.R
```

# 3. Run the Python script
After installing bs4, let's run the python script and get modified html file.  
And then we can jump to the certain webpages when we click the leaf button.
```shell
$ vi mod.py
$ sudo apt install python3-pip
$ alias pip=pip3
$ pip install beautifulsoup4
$ python3 mod.py
```
---
# About ERROR
You should install pandoc if you get the error below.
```shell
ubuntu@ip-172-**:~$ Rscript test.R 
Error in saveWidget(x, "test.html") : 
  Saving a widget with selfcontained = TRUE requires pandoc. For details see:
https://github.com/rstudio/rmarkdown/blob/master/PANDOC.md
Execution halted
```
