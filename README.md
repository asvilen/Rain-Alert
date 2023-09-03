# 🌦️ Rain Alert via SMS

## Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Overview

**Rain Alert via SMS** is your personal weather guardian. It's a Python-powered sentinel that watches the skies, and when rain is in the forecast within the next 9 hours, it sends you an SMS alert to ensure you're prepared with an umbrella in hand. Powered by the OpenWeatherMap API for weather data and the Twilio API for text messaging, this project runs automatically at 5:01 UTC daily, keeping you dry when the heavens open up.

![SMS Screenshot](screenshots/sms_alert.png)

## How It Works

- **Weather Data**: The program fetches weather data from the [OpenWeatherMap API](https://openweathermap.org/api).

- **Rain Check**: It checks the weather forecast for rain within the next 9 hours.

- **SMS Alert**: If rain is on the horizon, it swiftly sends you an SMS alert via [Twilio](https://www.twilio.com/).

## Technologies Used

- Python
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Twilio API](https://www.twilio.com/)
- PythonAnywhere for hosting and scheduling.

## Installation

1. **Clone the Repository**: Clone this repository to your local machine:
   ```
   git clone https://github.com/yourusername/rain-alert-via-sms.git
   ```
2. **Install Dependencies**: Install the required Python packages using pip:

    ```
    pip install requests twilio
    ```
3. **Set Up Environment Variables**: Configure your environment variables:

   - **OpenWeatherMap API Key**:
       - Create an account on [OpenWeatherMap](https://openweathermap.org/).
       - Obtain your API key.
    
   - **Twilio Credentials**:
       - Create an account on [Twilio](https://www.twilio.com/).
       - Obtain your Account SID, Auth Token, and a Twilio phone number.
    
   - **Set Environment Variables**:
       - Set the following environment variables in your system or create a `.env` file:
    
      ```
      OWM_API_KEY=your_openweathermap_api_key
      OWN_AUTH_TOKEN=your_twilio_auth_token
      ```
## Usage

- **Manual Run**: To run the program manually, navigate to the project directory and execute:
```
python rain_alert.py
```
- **Automated Scheduling**: For automated daily execution, consider hosting the script on a platform like [PythonAnywhere](https://www.pythonanywhere.com/).

Be prepared. Stay dry. 🌂

## License

This Snake Game project is licensed under the [MIT License](LICENSE). Share, enjoy, and have fun slithering to victory!
