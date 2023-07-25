# The BroadCast - Web News Application


The BroadCast is a web application developed for a leading newspaper company, designed to collect and display news articles in an organized and user-friendly manner. With "The BroadCast," users can access the latest headlines, read detailed news descriptions, and explore news across various categories. The application aims to deliver an efficient and engaging news browsing experience to its users.

## Features

- **Homepage:** A visually appealing homepage introduces users to "The BroadCast," displaying the app's name, launch date, and a brief description of its purpose.

- **Navigation Bar:** A navigation bar at the top of the page provides easy access to essential sections:
  - **Home:** Redirects users to the homepage.
  - **News:** Leads to a page displaying news headlines in a structured format (lists/bullets/grid).
  - **Contact Us:** Redirects to a page featuring contact details for the application admin.

- **News Display:** The "News" page presents news headlines categorized as General, Lifestyle, Travel, and Sports. Each news item is accompanied by a one-liner description and the author's name.

- **Add News:** Registered users can add news articles through a form that includes fields for headline, description, author name, and category.

- **User Registration & Login:** Users can register with unique usernames and passwords. Authenticated users can log in to access additional features.

- **Role-based Access:** Users are classified as Guest, Normal User, or Admin. Each role has specific access permissions:
  - Guest User: View news and contact the admin.
  - Normal User: Add news articles.
  - Admin: Update and remove news headlines.

- **Logging & Tracking:** The application logs user details, access time, and news additions/updates in a log file. The admin can access the log file to review user activities.

## Technologies Used

- Python Flask: The backend is powered by the Flask web framework to handle routing, user authentication, and database interactions.
- SQLAlchemy: Used to interact with the SQLite database for storing news articles and user information.
- Bootstrap: Provides the responsive and aesthetically pleasing frontend design.
- HTML & CSS: Used to structure and style the web pages.
- JavaScript: For interactive elements and dynamic content.

## Installation and Setup

1. Clone the repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the Flask application using `python app.py`.
5. Access the web application in your web browser at `http://localhost:5000`.

## Contributors

- [Alimiyan](https://github.com/Alimiyan)

## License

The BroadCast is open-source software licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for your own projects.

---

Thank you for checking out "The BroadCast" web news application! We hope you enjoy browsing the latest news with our user-friendly platform. If you have any suggestions or feedback, please feel free to submit an issue or contribute to the project. Happy reading!
