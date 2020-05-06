----------Required Packages--------
	cv2
	os
	io
	re
	argparser
	datefinder
	pandas
	datetime

First need to create account with Vision API
download the credentials and use it here

Here I have used cv to preprocess the images
and created different regex expressions to extract the patterns

Finally to execute the program run the below command in the terminal
  python main.py 'folder_path which having the images '
and here i am assuming the images are RGB images

And it results the text file which having list of dictionaries having details 


----------------
Here I am not able to complete the Name extraction

I was tried by using nltk
But it works only the names which in the form like 'Vijay Anand' and not for 'VIJAY ANAND'

for this i am thinking to train a neural network on new data

