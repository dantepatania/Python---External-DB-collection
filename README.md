# External DB collection

Author: Dante Patania

## Objective

This project consumes data from three diferent sources in order to populate a SQL database with cultural information about librarys, museums and cinemas from Argentina. 

### Deploy

1) You must first download or clone the repository locally, then create a virtual environment with venv command.

    `py -m venv <venv name>`
  
   Activate it
  
    `source <venv name>/scripts/activate`
    
2) Install all necessary modules, you may use pip tool for this step.

    `pip3 install <module>`
  
    *requirements.txt* file is provided, in which all used modules are listed. You can easily download all modules at once with the following command. 

    `pip3 install -r requirements.txt`
    
3) A PostgreSQL database creation is needed, once done you must keep the following parameters in order to set *.env* file.
  
      `host, user, password, name, port`
      
4) Complete *.env* file with previous parameters from the database created and datasets download **URL**. You must check URLs work properly. 
  
5) Create database tables with the following command. 
  
    `py create_tables.py`
  
### Running

Run the following command. 
  
    `py main.py`
  
In *file.log* file you will find execution steps.