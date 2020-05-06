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
download the credentials in json file and use it here

Here I have used cv to preprocess the images
and created different regex expressions to extract the patterns

Finally to execute the program run the below command in the terminal
  python main.py 'folder_path which having the images '
and here i am assuming the images are RGB images

And it results the text file which having list of dictionaries having details 


