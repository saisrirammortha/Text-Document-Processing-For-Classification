TXT2GMLv1.0

Author - Karan Bajaj
Email  - karanbajaj23@gmail.com
WEB    - www.karanbajaj.tk

Steps for running the .txt to .gml converter -

1. Unzip the tar ball
2. Open terminal and make the folder as current directory
3. Type 'make' and press Enter
4. Now type './conversion' to run the executible file and read the introduction
5. For converting a .txt file, type the following command -
	$ ./conversion <filename>

For example, running the 'sample.txt' file for conversion -

	$ ./conversion sample

Remember to NOT use .txt extension with the filename while passing as parameter.
Any illegal file name sent would result in a Segmentatio Fault by the machine.
