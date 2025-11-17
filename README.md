\documentclass[12pt]{article}
\usepackage[a4paper,margin=1in]{geometry}
\usepackage{hyperref}
\usepackage{titlesec}

\titleformat{\section}{\large\bfseries}{}{0em}{}
\titleformat{\subsection}{\normalsize\bfseries}{}{0em}{}

\title{Learn Python From Zero: Roadmap and Project Structure}
\author{}
\date{}

\begin{document}

\maketitle

\section*{Overview}
This repository documents a complete journey of learning Python from the fundamentals to advanced concepts. Each chapter is organized into a dedicated folder and contains practice scripts, exercises, and mini–projects. The objective is to build a strong Python foundation supported by real, structured, and progressive hands-on work.

\section*{Goals}
\begin{itemize}
    \item Learn Python step-by-step from beginner to advanced.
    \item Build practical projects for each topic to reinforce concepts.
    \item Create a publicly visible learning portfolio.
    \item Prepare for fields such as software development, automation, data analysis, backend work, and cybersecurity scripting.
\end{itemize}

\section*{Repository Structure}
Each directory corresponds to a major Python topic.

\begin{verbatim}
01_intro_basics/
02_collections/
03_file_io/
04_comparisons/
05_conditions_loops/
06_functions/
07_oop/
08_modules_packages/
09_errors_tests/
10_decorators/
11_generators/
12_advanced_modules/
13_web_scraping/
14_images/
15_data_files/
16_web_apis_flask/
17_advanced_data_structures/
\end{verbatim}

\section*{Chapter Descriptions}

\subsection*{01\_intro\_basics}
Numbers, strings, variables, user input, and Python syntax fundamentals.

\subsection*{02\_collections}
Lists, tuples, sets, dictionaries, indexing, slicing, and nested structures.

\subsection*{03\_file\_io}
Reading and writing files, handling CSV files, simple data logging.

\subsection*{04\_comparisons}
Comparison operators: equality, inequality, greater/less than, and boolean evaluation.

\subsection*{05\_conditions\_loops}
Conditional statements, for-loops, while-loops, and loop control mechanisms.

\subsection*{06\_functions}
Function definitions, parameters, return values, scope, *args, **kwargs.

\subsection*{07\_oop}
Classes, objects, attributes, methods, encapsulation, and simple system modeling.

\subsection*{08\_modules\_packages}
Creating and importing modules, using Python's package system, understanding \texttt{\_\_name\_\_}.

\subsection*{09\_errors\_tests}
Error handling, try/except blocks, raising exceptions, basic unit testing, and linting.

\subsection*{10\_decorators}
Higher-order functions and writing custom decorators.

\subsection*{11\_generators}
Generator functions, the \texttt{yield} keyword, and lazy evaluation.

\subsection*{12\_advanced\_modules}
Working with \texttt{datetime}, \texttt{random}, \texttt{math}, regular expressions, and decimal calculations.

\subsection*{13\_web\_scraping}
Using \texttt{requests}, BeautifulSoup4, and Selenium for HTML parsing and automated scraping.

\subsection*{14\_images}
Basic image manipulation with Pillow (PIL).

\subsection*{15\_data\_files}
CSV, PDF, and Excel file handling.

\subsection*{16\_web\_apis\_flask}
JSON processing, API calls, handling HTTP responses, and introduction to Flask microframework.

\subsection*{17\_advanced\_data\_structures}
Advanced list, set, and dictionary operations, performance considerations, itertools.

\section*{Example Included Projects}
\begin{itemize}
    \item Personal Profile Card
    \item Temperature Logger
    \item Word Frequency Analyzer
    \item Password Strength Checker
    \item To-Do CLI with File Persistence
    \item Website Title Scraper
    \item Image Resizer and Compressor
    \item CSV Report Generator
    \item Simple Flask API
    \item Regex-Based Text Cleaner
    \item OOP-Based Inventory System
    \item Decorator-Based Logging Tool
\end{itemize}

\section*{Learning Outcomes}
After completing the roadmap, learners will be able to:
\begin{itemize}
    \item Understand Python syntax and core programming patterns.
    \item Build modular scripts for automation and data manipulation.
    \item Handle text, CSV, PDF, and Excel files.
    \item Work with external APIs and JSON data.
    \item Conduct web scraping with BeautifulSoup and Selenium.
    \item Build simple Flask-based backend applications.
    \item Implement decorators, generators, and object-oriented models.
    \item Write safer code using error handling and unit testing.
\end{itemize}

\section*{Career Applications}
Skills developed here apply to introductory roles such as:
\begin{itemize}
    \item Python Developer (Junior)
    \item Automation Engineer (Entry-Level)
    \item Data Analyst (Beginner Python Role)
    \item Backend Development Intern
    \item Web Scraping Specialist
    \item QA Automation Intern
    \item Cybersecurity Automation / SOC Scripting Intern
\end{itemize}

\section*{How to Run the Code}
Clone the repository:
\begin{verbatim}
git clone https://github.com/saeidptzl/learn-python-from-zero.git
cd learn-python-from-zero
\end{verbatim}

Run any Python project:
\begin{verbatim}
python3 folder_name/project_name.py
\end{verbatim}

\section*{Development Notes}
This repository will continue to grow with:
\begin{itemize}
    \item Additional hands-on projects
    \item New exercises and expansions
    \item Improved documentation
    \item Interview-preparation notes
\end{itemize}

\end{document}
