library(circlepackeR)
library(htmlwidgets)

url <- "https://gist.githubusercontent.com/mbostock/1093025/raw/05621a578a66fba4d2cbf5a77e2d1bb3a27ac3d4/flare.json"
x <- circlepackeR(url
                 , size = "size"
                 , color_min = "hsl(300, 82%, 85%)"
                 , color_max = "hsl(300, 43%, 33%)")

saveWidget(x, 'test.html')