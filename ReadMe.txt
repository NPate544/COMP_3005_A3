

1. PREAMBLE:


	AUTHOR - NIRAJ PATEL - 101269614
	
	PURPOSE - Writing an App that connects a PostgreSQL database to perform specific CRUD (Create, Read, Update, Delete) operations.
	

	SOURCE FILES INCLUDED - initDB.py MyApp.py ResetApp.py   

	**NOTE: Video Demonstration Link in the END.  
	
	DATE MODIFIED: 2024/03/17 - REV A   
	  
	
2. COMPLILATION COMMAND TO USE :


  - You shall find the above source files including the ReadME file.
  
  - there are NO compilation commands to run as you will be running 3 scripts based in the need.

  - However, make sure you have python and PostgreSql (PgAdmin4) installed.

	NOTE** - install the necessary package fro the script to run `pip install psycopg2`
	
	
3. LAUNCHING INSTRUCTIONS:

	1. Download the files (3 source code and the ReadME) or clone repository.
	
	2. open terminal and change working directory to where the files are kept
	


4. OPERATING INSTRUCTIONS:


	0. Open PgAdmin4 and create a database - since you will be running the scripts locally - MAKE SURE TO CHANGE THIS: (ESPECIALLY -> database, user and password);

		conn_params = {
		    "database": "Assignment_3",
		    "user": "postgres",
		    "password": "postgres",
		    "host": "localhost",
		    "port": "5432"
		}


	A. Initialize the data schema:

		1. run `python initDB.py` - This script will create a students table and fill 3 dummy entries in it.
		2. You will see the students table in the pgAdmin4 and be able to view the values.
 
	B. Test the CRUD App:

		1. run `python MyApp.py` - This script will perform serveral operations (CRUD) on the existing students table.

		2. You will come across these options;

			1. Retrieve all students
			2. Add Student
			3. Update students email address
			4. delete student
			5. exit

			- Test these options by following the video


		3. In the software, pgAdmin4, re run the query which shows the students table. 
		
	C. Reset the students table with initial values;

		1. Run the `python ResetApp.py` - This script deletes the entries from teh students table and initializes the starting records/values we used during creation of the database.
		2. the command prompt will show the stages of the script.
		3. In the software, pgAdmin4, re run the query which shows the students table. -> you will see inital values 

		**NOTE: student_id will not be kept the same, it will increment as it is kept as SERIAL. 
	

	
VIDEO DEMONSTRATION LINK: https://youtu.be/Mkd9kSPyrq0




	   
