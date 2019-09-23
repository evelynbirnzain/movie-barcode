# movie-barcode

`barcode_resized.py`is a short python script that compresses movies into a barcode-like image frame by frame using [OpenCV](https://opencv.org/).
In the raw numpy array, each frame is represented by a 1px-wide slice of the frame's average color. You can also choose to go for
only averaging in horizontal direction for a more sophisticated representation as well as only taking every nth frame into consideration 
for slightly improved performance.

`barcode_split` opts for slicing the (very long) sequence of frames and stacking the slices on top of one another instead of resizing
the numpy array in order to include every single frame in the output image.

Examples:
Avatar (2009)
![avatar1](https://github.com/evelynbirnzain/movie-barcode/blob/master/images/0.jpg)
![avatar2](https://github.com/evelynbirnzain/movie-barcode/blob/master/images/0s.jpg)

Blade Runner 2049
![br1](https://github.com/evelynbirnzain/movie-barcode/blob/master/images/1.jpg)
![br2](https://github.com/evelynbirnzain/movie-barcode/blob/master/images/1s.jpg)

Interstellar
![is1](https://github.com/evelynbirnzain/movie-barcode/blob/master/images/2.jpg)
![is2](https://github.com/evelynbirnzain/movie-barcode/blob/master/images/2s.jpg)

It (2017)
![it1](https://github.com/evelynbirnzain/movie-barcode/blob/master/images/3.jpg)
![it2](https://github.com/evelynbirnzain/movie-barcode/blob/master/images/3s.jpg)

Mad Max: Fury Road
![mm1](https://github.com/evelynbirnzain/movie-barcode/blob/master/images/4.jpg)
![mm2](https://github.com/evelynbirnzain/movie-barcode/blob/master/images/4s.jpg)

Up (2009)
![up1](https://github.com/evelynbirnzain/movie-barcode/blob/master/images/5.jpg)
![up2](https://github.com/evelynbirnzain/movie-barcode/blob/master/images/5s.jpg)

A selection of split images:
![avatar3](https://github.com/evelynbirnzain/movie-barcode/blob/master/images/0_split.jpg)
![br3](https://github.com/evelynbirnzain/movie-barcode/blob/master/images/1_split.jpg)
