## Hospital Manager

On Wednesday we create a simple hospital database for patients, doctors and hospital stays.

But one hospital cannot be managed only with this information.

Our task for today is to create a working system, which can be used by both doctors and patients.

First we need a Base user, which will be inherited by the doctor and patient. Our user need to have username, password and age.

Doctors themselves need additional information, such as academic title.

For the patients we don't need more data, for now.

We have a table for the hospital stay with the information for the room, start and end date, injury and patient.

But the patients can come to the hospital on a visitation. For this reason we need new table, which will collect the data.

Each doctor can have several hours for visitations in one day. One hour is for one visitation, so we need to know the start hour of it.

Now its time to create add the new tables and try to keep the current data from database.

Once we have the whole schema done, we need to provide a good command line interface to our users.

#### Abilities of the users:

- Doctor:
  - Log into the system
  - can list all of his/hers patients
  - can add hours for visitation
  - can delete free hours of visitation
  - has the ability to see the room and the duration of hospital stays per each of his patients

- Patient:
  - Log into the system
  - can reserve hour for visitation
  - can see the free hours of his/hers doctor
  - can stay at the hospital for an injury
  - can see the academic title of his doctor
