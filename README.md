# MagmaTermial
Magma terminal is lightweight, customizable and open-source to allow You to create.

To create a command, You need:
1. Some time
2. Installed terminal
3. Python

Creating a command step by step:
1. Find this folder in terminal location. ![image](https://user-images.githubusercontent.com/84672664/158354820-ca1e4e2c-1f00-4467-b4f5-0cbeda31781d.png)
2. Go to configs.
3. Copy example.json.
4. Now You can change the name and description. ![image](https://user-images.githubusercontent.com/84672664/158355062-fd50bb33-6a33-4f2b-932b-b3a113ea4c69.png)
5. Configure arguments. This is gonna be important if You want to create a command that does operation that requires input. If you are creating a simple command, leave it like that

![image](https://user-images.githubusercontent.com/84672664/158355328-bb2be403-6836-49b6-923a-6c3c2c2ae191.png)

6. Next, go to commands/scripts and create python file, then write code.  
7. This program will ask a user for 3 arguments and then print "Example" and these arguments. ![image](https://user-images.githubusercontent.com/84672664/158355512-4f175873-c2c2-4608-92fb-70a10cf3b41e.png)
8. Then, go back to commands/configs and edit Your .json file.
9. Change the "script" value to .py script filename (with extension), and You're done!
