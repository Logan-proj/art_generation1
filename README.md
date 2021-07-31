# Generative Art project 1

My first generative art project allows the user to import a .jpg file and the program will then return an image of
randomly generated squares based on the 30 most recurring colors in the image file.

## Features

First import the image as a .jpg file into the program folder. On line 10 enter the name of the .jpg file
inside the quotation marks "". This will tell the program to use that specific file.
        
    colors = colorgram.extract("name_of_file_here.jpg", 30)

The program comes with files already imported into the program folder. to test out my program you can insert the names
of these images inside the quotation marks as described above:

+ mona_lisa.jpg
+ persistence_of_memory.jpg
+ starry_night.jpg
+ the_last_supper.jpg
+ the_scream.jpg


## Motivation

I wanted to create a project that combines my interests in art and programming.

## Requirements

+ Python is required to run main.py file
+ .jpg file is needed to populate an image

## Installation

Provide code examples and explanations of how to get the project, e.g.,

	[Insert here]

## Reference

**Colorgram** is used to extract colors from images.
+ Documentation: https://pypi.org/project/colorgram.py/