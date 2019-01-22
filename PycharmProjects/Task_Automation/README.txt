------------------------
------------------------

Project Explanation :

As per the task assignment there are three tasks to complete :
1. ClearTrip Flow
2. Amazon Flow
3. Excel Expense Calculation

----------------------------------------------------------------------
----------------------------------------------------------------------

Flow of the project :

1. Created a POM [Page Object model] for the project where web-elements, Methods and TestCase are segregated in seperate files.

A. ClearTrip Flow :
   a. locators are created in path {RootPath}\PycharmProjects\Task_Automation\Locators
   b. Test Methods are created in path {RootPath}\PycharmProjects\Task_Automation\Pages_ClearTrip
   c. Test Case Flows are created in path {RootPath}\PycharmProjects\Task_Automation\Test\task_one_flow.py

User has to run the file mentioned in point "c" - Right click open with idle and click on F5 file will run
After completion of run report will be generated in 
file_path : \PycharmProjects\Task_Automation\reports folder in an HTML format.

How it Automated :::

 Used python inbuilt framework Unittest to create a TestFlow and HtmlRunner to generate a simple report.


B. AmazonFlow :
   a. locators are created in path {RootPath}\PycharmProjects\Task_Automation\Locators_Amazon
   b. Test Methods are created in path {RootPath}\PycharmProjects\Task_Automation\Pages_Amazon
   c. Test Case Flows are created in path {RootPath}\PycharmProjects\Task_Automation\Test\task_two_flow.py

User has to run the file mentioned in point "c" , Right click open with idle and click on F5 file will run
After completion of run report will be generated in 
file_path : \PycharmProjects\Task_Automation\reports folder in an HTML format.

C. Expense Calculation :
   a. Run the file in {root_path)\PycharmProjects\Task_Automation\Test\excel_automate.py Right click open with idle and click on F5 file will run.
   b. Excel will get create in path {root_path}\PycharmProjects\Task_Automation\datahouse.

-------------------------------------------------------------------------------------------------------------------------------------


Pre-Requesites needed to run the files :

1. Install Python
2. Install unitest framework
3. Install HtmlRunner
4. Install OpenPyxl.
5. Install Selenium.

-------------------------------------------------------------------------------------------------------------------------------------

Installing Python :

Step 1: 
	a. Download the Python 3 Installer
	b. Open a browser window and navigate to the Download page for Windows at python.org.
	c. Underneath the heading at the top that says Python Releases for Windows, click on the link for the Latest Python 3 Release 	    Python 3.x.x. (As of this writing, the latest is Python 3.6.5.)
	    Scroll to the bottom and select either Windows x86-64 executable installer for 64-bit or Windows x86 executable installer 

Step 2: 
       a. Run the Installer

Step 3:
       a. Open command prompt and change directory to Python               \Scripts folder using command :  cd {file_path} 
       b. Check pip validation using pip --version
       
Install selenium :

a. Continuation of Step 3 in Run command  pip install -U selenium
b. Install Html Test Runner using command pip install html-testRunner
c. Install Html OpenPyxl using command pip install openpyxl

After all these set an environment variable for python path.



 










  


