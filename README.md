# NIK-extractor
A somewhat functioning extractor for Indonesia ID card number. This was created with the goal to shorten the card number extraction using manual entry. Upload your ID card image (make sure to follow the format) and your card number will be printed. Special thanks to JaidedAI, the maker of easyocr, for letting me implement their work to my code. I also would like to extend my thanks to Mr.Thio Perdana for the guidance and counceling. Could not have done it without them.

## Please follow the following steps for the best performance:
- Make sure the image is clear and not blurry
- The ID card image must be in the correct position (not tilted), below is an example
- The NIK text must be readable and have high contrast (good lighting)
- The ID card background color must be a different color from the KTP background
![Ideal Image](https://github.com/Surge0Name/NIK-extractor/blob/main/place-holder.jpg)

# Using mass_extraction and stream_imp
Keeping the requirement for the best performance in mind, we can move on to two esential file. Namely the mass_extraction.ipynb and streamlit_imp.py. Do not forget to install the requirement 

## mass extraction
As the name suggest, you can use this to extract a mass image of ID card. 
- Make a folder and put all of the ID card image that you want to extract 
- Copy the folder adress in img_path
- Run all, and wait

## stream_imp
This is the file that you need to run if you wanted to run it locally. I have not deploy it because the streamlit cannot detect cv2 module. I do not know why, maybe it's a bug, not implemented, or it is because my limited experience in coding. It is however working in localhost. Another note, since streamlit cannot take multiple file (if there are, i do not know how), this program, unfortunately, must make do with only handling one image at a time
- Run stream_imp.py using streamlit run <file_name>
- Upload your image
- Wait for it to extract the ID card number

# Permission
You can use and modify my program -if this god awfull code is even worth your time to begin with- however you see fit as long as it is under law and reason. I do not condone any illegal activity so please refrain yourself from doing so. If you have suggestion to improve my code please do not hesitate to contact me. Thank you

