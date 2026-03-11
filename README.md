# Bincom INEC Election Test

This project is a Django implementation of the Bincom Python developer intern test.
You can do the  following:
1. View election results for an individual polling unit.
2. View the summed total result of all polling units under a particular LGA.
3. Enter results for **all parties** for a polling unit.

The project uses **Django** and **MySQL** with the provided Bincom test dataset.

---

# Project Setup Guide

---

# 1. Clone the Repository

```bash
git clone https://github.com/Oguntayo/bincom_inec_test.git
cd bincom_inec_test
```

---

# 2. Create Environment File

Copy the example environment file:

```bash
cp .env.example .env
```

Edit the `.env` file and enter your database credentials.

---

# 3. Create Virtual Environment

Create a Python virtual environment:

```bash
python3 -m venv venv
```

Activate it.

### Linux / Mac

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

# 4. Install Requirements.txt

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

# 5. Create the MySQL Database

### Login to MySQL:

```bash
mysql -u root -p
```

### Create the database and application user:

```bash
CREATE DATABASE bincom_test;

CREATE USER 'bincom_user'@'localhost' IDENTIFIED BY 'bincompasscode';

GRANT ALL PRIVILEGES ON bincom_test.* TO 'bincom_user'@'localhost';

FLUSH PRIVILEGES;

Exit MySQL:

exit;
```

---

# 6. Import the Provided SQL Dataset

Import the Bincom test dataset into the database:

```bash
mysql -u root -p bincom_test < bincom_test.sql
```
---

# 7. Fixing Party Abbreviation Issue

The database schema defines:

```
party_abbreviation CHAR(4)
```

But the dataset contains a party entry:

```
LABOUR
```

which exceeds the 4-character limit and causes the error:

```
Data too long for column 'party_abbreviation'
```

To fix this, update the party abbreviation.

Login to MySQL:

```bash
mysql -u root -p bincom_test
```

Run:

```sql
UPDATE party
SET partyid = 'LABO'
WHERE partyid = 'LABOUR';
```

Verify the change:

```sql
SELECT * FROM party;
```

Exit MySQL:

```sql
exit;
```

---

# 8. Run Migrations

```bash
python manage.py migrate
```

---

# 9. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at:

```
http://127.0.0.1:8000/
or 
localhost:8000
```

# Tech Stack

* Python
* Django
* MySQL
* HTML / CSS

#Access the public link here 
```bash
https://bincom-inec-test.onrender.com
```