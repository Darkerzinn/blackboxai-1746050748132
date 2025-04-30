
Built by https://www.blackbox.ai

---

```markdown
# Roxyn - Student Registration System

## Project Overview
Roxyn is a student registration application built using Python's Tkinter library for the graphical user interface (GUI) and SQLite for data storage. The application allows users to register students by their unique ID (matricula) and name, and provides a simple interface for viewing the list of registered students.

## Installation
To run the application, you need Python installed on your computer. Follow these steps to install the necessary dependencies and run the application:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/painel-matriculas.git
   cd painel-matriculas
   ```

2. **Ensure you have Python and Tkinter installed:**
   Tkinter is included with Python's standard library. If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/).

3. **Run the application:**
   Simply execute the following command in your terminal or command prompt:
   ```bash
   python painel-matriculas.py
   ```

## Usage
Upon launching the application, you will see an interface with fields to enter a student's matricula (ID) and name. Enter the required details and click the "Adicionar" button to register the student. The list of registered students will be displayed below.

### Screenshots
![Roxyn Interface](path_to_screenshot.png)   *(Replace with an actual screenshot of your application)*

## Features
- **Student Registration:** Easily register students using their matricula and name.
- **Database Integration:** Utilizes SQLite for efficient data storage and management.
- **User-Friendly Interface:** Designed with Tkinter for a clean and accessible GUI.
- **Data Validation:** Checks for filled input fields and unique matricula entries.
- **Dynamic Student List:** Displays a real-time list of registered students.

## Dependencies
No additional dependencies are required beyond Python and Tkinter, as the application uses SQLite, which is included in the Python standard library.

## Project Structure
The project consists of the following files:
- `painel-matriculas.py`: The main application file containing the implementation of the Roxyn student registration GUI.
- `students.db`: The SQLite database (created automatically by the application) that stores student records.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements
Thanks to everyone who helped support the development of this project. Contributions and suggestions are always welcome!
```