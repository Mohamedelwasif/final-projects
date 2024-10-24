1. Class Diagram
A class diagram shows the structure of the system by modeling its classes, attributes, methods, and relationships.

Classes and Attributes:
Person

name: String
age: int
Patient (inherits from Person)

medical_record: String
Methods: view_record()
Staff (inherits from Person)

position: String
Methods: view_info()
Department

name: String
patients: List<Patient>
staff: List<Staff>
Methods: add_patient(patient: Patient), add_staff(staff_member: Staff)
Hospital

name: String
location: String
departments: List<Department>
Methods: add_department(department: Department)

#Class Diagram Representation
+----------------+
|    Person      |
+----------------+
| - name: String |
| - age: int     |
+----------------+
| + view_info()  |
+----------------+

       ▲
       |
+-------------------+        +-------------------+
|     Patient       |        |      Staff         |
+-------------------+        +-------------------+
| - medical_record: String   | - position: String|
+-------------------+        +-------------------+
| + view_record()   |        | + view_info()     |
+-------------------+        +-------------------+

+----------------------------+
|        Department          |
+----------------------------+
| - name: String             |
| - patients: List<Patient>  |
| - staff: List<Staff>       |
+----------------------------+
| + add_patient(patient: Patient) |
| + add_staff(staff_member: Staff)|
+----------------------------+

+-----------------------------+
|         Hospital            |
+-----------------------------+
| - name: String              |
| - location: String          |
| - departments: List<Department> |
+-----------------------------+
| + add_department(department: Department) |
+-----------------------------+


2. Sequence Diagram
The sequence diagram will show how a patient is added to a department and how staff is assigned to a department. It represents the interaction between objects over time.

Scenario: Add Patient and Staff to Department
Actors/Objects involved:

Hospital
Department
Patient
Staff

Patient          Department       Hospital         Staff
   |                   |               |               |
   |-- create()        |               |               |
   |------------------>|               |               |
   |                   |-- add_patient()              |
   |                   |----------------------------->|
   |                   |               |-- confirm -->|
   |                   |               |              |
   |                   |-- add_staff()                |
   |                   |----------------------------->|
   |                   |               |-- confirm -->|


3. Use Case Diagram
A use case diagram depicts how different users interact with the system. In the hospital system, the actors and actions include:

Actors:
Administrator (manages departments, patients, and staff)
Doctor/Staff (view and manage patient data)
Patient (view their medical record)
Use Cases:
Manage Departments (add department to hospital)
Add Patient (assign a patient to a department)
Add Staff (assign staff to a department)
View Patient Record
View Staff Information


+--------------------------------------+
|              Hospital                |
+--------------------------------------+
| Manage Departments                   |
| Add Patient                          |
| Add Staff                            |
| View Patient Record                  |
| View Staff Information               |
+--------------------------------------+

Administrator ---------------> Manage Departments
Doctor/Staff ---------------> View Patient Record
Administrator ---------------> Add Staff
Patient ---------------------> View Patient Record
