# image
![modified.html](https://user-images.githubusercontent.com/58103830/94028049-79795b80-fdf6-11ea-93d3-4aa076ffc205.gif)

---
1. Install R  
2. Run the R script  
3. Run the Python script  
---
- Required
    - circlepackeR
    - htmlwidgets
- If you need
    - tidyverse 
    - hrbrthemes
    - data.tree
---
# 1. Install R
Refer to [THIS](https://qiita.com/JeJeNeNo/items/43fc95c4710c668e86a2)  

# 2. Run the R script
After intalling libs into R, run the R script.
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
```shell
$ vi mod.py
$ sudo apt install python3-pip
$ alias pip=pip3
$ pip install beautifulsoup4
$ python3 mod.py
```
---
# About ERROR
```shell
ubuntu@ip-172-**:~$ Rscript test.R 
Error in saveWidget(x, "test.html") : 
  Saving a widget with selfcontained = TRUE requires pandoc. For details see:
https://github.com/rstudio/rmarkdown/blob/master/PANDOC.md
Execution halted
```
you should install pandoc.

