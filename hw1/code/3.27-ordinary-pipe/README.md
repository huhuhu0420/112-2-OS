# 3.27
Design a file-copying program named filecopy using ordinary pipes.
* This program will be passed two parameters: the name of the file to be copied, and the name of the copied file
* The program will then create an ordinary pipe and write the contents of the file to be copied to the pipe
* The child process will read this file from the pipe and write it to the destination file
* For example, if we invoke the program as follows:
    * filecopy input.txt copy.txt
    * The file input.txt will be written to the pipe. The child process will read the contents of this file and write it to the destination file copy.txt.


### Compilation
```sh
gcc filecopy.c -o filecopy
```

### usage
```sh
./filecopy \<source> \<destination>
```
![](./screenshot/screenshot.png)