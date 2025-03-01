#MySQL AI Assistant

Overview

MySQL AI Assistant is an intelligent SQL helper that leverages Google's Gemini AI to provide structured, step-by-step MySQL solutions. It takes user queries related to MySQL and generates executable SQL commands, making it easier for developers, students, and database administrators to quickly understand and implement MySQL operations.

Features

Understands SQL-related questions and explains them in simple terms.

Generates CREATE TABLE statements with appropriate column types.

Provides INSERT INTO statements with realistic sample data.

Writes structured SQL queries to solve the problem.

Describes expected output for better understanding.

Maintains a conversation history to provide context-aware responses.

## Sample Use Case
### **User Input:**
```sh
Enter a prompt: How do I find the highest salary in an employee table?
```

### **AI-Generated Output:**
```sql
-- Understanding the Problem
-- We need to find the highest salary from an employee table.

-- Database & Table Creation
CREATE TABLE Employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10,2)
);

-- Data Insertion
INSERT INTO Employees (id, name, salary) VALUES
(1, 'Alice', 50000.00),
(2, 'Bob', 60000.00),
(3, 'Charlie', 75000.00);

-- Query Execution
SELECT MAX(salary) AS HighestSalary FROM Employees;

-- Expected Output
+---------------+
| HighestSalary |
+---------------+
| 75000.00      |
+---------------+
```

