# World Clock Web App

This project is a comprehensive solution that includes a web application displaying the current time in various locations around the world, integration with GitHub Actions for periodic automation, and the use of a PostgreSQL database hosted on Azure. It is designed to demonstrate proficiency in web development, automation, and database management.

## Goal

The primary objectives of this project are:

1. **Create a World Clock**: Display the current time in different locations across the globe.
2. **Automate with GitHub Actions**: Utilize GitHub Actions to run a script every 15 minutes.
3. **Database Management**: Set up a PostgreSQL server on Azure at no cost.

## Features

- **Location Selection**: Users can select up to four locations from a dropdown menu to display the current time.
- **Real-time Updates**: The displayed time updates every second to ensure accuracy.
- **Bonus Features**:
  - Display of UNIX timestamps alongside conventional time.
  - A dedicated page for converting UNIX timestamps to human-readable time.
  - Real-time data fetching for finance (stocks, forex, bitcoin, etc.), weather, and 911 calls.
  - Periodic ingestion of fetched data into the PostgreSQL database.

## Submission Requirements

Your submission should include the following:

1. **Azure Web App Link**: A link to your Azure-hosted web application for the world clock.
2. **GitHub Repository**: A link to your GitHub repository containing:
    - `README.md`: This file.
    - `app.py`: The main application script.
    - `hello.py`: (Optional) For those completing the bonus, include the scraper code from lab2.
3. **Screenshot**: A screenshot of the Azure webpage with the terminal showing a successful connection to PostgreSQL.

## Setup and Installation

### GitHub Action

- The `.github/workflows/main.yml` file is configured to run a script every 15 minutes. This script is responsible for fetching real-time data and updating the PostgreSQL database.

### PostgreSQL on Azure

- Instructions on how to set up a free PostgreSQL server on Azure are included. Ensure that you configure the database to accept connections from your web app and GitHub Actions.

### Running the Web App

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run `app.py` to start the web application.
4. Access the web application through your browser to view the world clock and other features.

## Contributing

Contributions to this project are welcome. Please fork the repository, make your changes, and submit a pull request for review.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
