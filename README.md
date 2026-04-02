#  Zodiac Sign Calculator

##  Overview

The Zodiac Sign Calculator is a simple web-based application that allows users to enter their date of birth and instantly discover their zodiac sign.

It uses a lightweight Python HTTP server and dynamic HTML rendering to deliver results in real time.

---

##  Features

*  Date of birth input
*  Instant zodiac sign calculation
*  Clean and modern user interface
*  Fast and lightweight (no heavy frameworks required)
*  Dynamic HTML rendering using Jinja2

---

##  Technologies Used

* **Backend:** Python
* **Frontend:** HTML, CSS
* **Templating Engine:** Jinja2
* **Server:** Built-in Python HTTP Server

---

##  Project Structure

```
project-folder/
│
├── static/
│   └── index.html
│
├── templates/
│   └── horoscope.html
│
├── ZodiacCalculator.py
└── README.md
```

---

##  Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-repo-link>
cd project-folder
```

### 2. Install Dependencies

Make sure you have Python installed, then install Jinja2:

```bash
pip install jinja2
```

---

##  Running the Application

Run the Python server:

```bash
python "Zodiac Calculator.py"
```

You should see:

```
Serving HTTP on localhost port 8080...
```

Open your browser and go to:

```
http://localhost:8080
```

---

##  How It Works

1. User enters their date of birth on the homepage.
2. The app extracts the **month** and **day**.
3. A request is sent to the `/horoscope` route.
4. The Python server determines the zodiac sign using predefined date ranges.
5. The result is rendered dynamically using a Jinja2 template.

---


##  Notes

* Ensure your folder structure matches the expected layout (`static` and `templates` folders).
* The server runs locally and is intended for learning or small-scale use.

---

##  Contributing

Contributions are welcome! Feel free to fork this project and submit a pull request.

---

##  License

This project is open-source and available under the MIT License.

---

##  Author

Akorede Kareem
GitHub: https://github.com/Ricsmokey

---
