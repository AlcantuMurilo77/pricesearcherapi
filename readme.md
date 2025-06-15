
# Product Price Searcher API

## Overview

This project is a FastAPI-based RESTful API that allows users to search for product prices on MercadoLivre (a popular e-commerce platform in Brazil) by providing a product name. It uses Selenium WebDriver to scrape product names and prices from the website and generates an Excel report with the results. The report is then sent via email to a specified recipient.

---

## Features

- Search for product prices on MercadoLivre by product name.
- Automatically generate an Excel spreadsheet with the search results.
- Send the Excel report as an email attachment.
- Input validation for product names and target email addresses.
- Environment variables used for email credentials.

---

## Technologies Used

- Python 3.10+
- FastAPI
- Selenium WebDriver (Chrome)
- pandas
- python-dotenv
- python-slugify
- openpyxl (for Excel export)
- SMTP (for sending emails via Gmail)
- Uvicorn (ASGI server)

---

## Project Structure

```
.
├── main.py                # FastAPI application entry point
├── services
│   ├── email_sender.py    # Email sending utility
│   └── product_searcher.py# Web scraping and data processing
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not committed)
├── .env.example           # Example environment file
├── message.txt            # Email message template
└── README.md              # This file
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository_url>
cd <repository_folder>
```

### 2. Create and activate a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup environment variables

Create a `.env` file in the project root (or copy from `.env.example`) with your Gmail credentials:

```
EMAIL=your_email@gmail.com
PASSWORD=your_app_password
```

> **Important:**  
> - For Gmail, you must create an **App Password** if using 2-Step Verification.  
> - Do not use your regular Gmail password for SMTP.  
> - Never commit your `.env` file to version control.

### 5. Install ChromeDriver

Make sure you have the ChromeDriver installed and available in your system PATH, matching your Chrome browser version.

- Download from: https://chromedriver.chromium.org/downloads

---

## Running the API

Start the FastAPI server with Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at: `http://127.0.0.1:8000`

---

## Usage

### Endpoint: Search Product Prices and Send Email

```
GET /searchproduct/{product_name}?target_email=youremail@example.com
```

- **Path Parameter:**  
  `product_name` - Product name to search (min length 2, max 100, supports letters, numbers and some accented characters).

- **Query Parameter:**  
  `target_email` - Email address where the report will be sent.

### Example Request

```
GET http://127.0.0.1:8000/searchproduct/iphone?target_email=user@example.com
```

The API will scrape MercadoLivre for the product "iphone", generate an Excel report, email it to `user@example.com`, then delete the report from the server.

### Response

```json
{
  "message": "done",
  "filename": "iphone-price-research-2025-06-15.xlsx"
}
```

---

## Notes and Considerations

- The scraping relies on MercadoLivre's website structure and may break if the site layout changes.
- The Excel file is temporarily saved locally and deleted after sending the email.
- The SMTP server used is Gmail's, requiring proper credentials and app password configuration.
- The API currently supports only one search per request and sends email immediately.
- Selenium runs in headless mode; ChromeDriver must be installed and compatible.

---

## License

This project is provided as-is without any warranty. Use it responsibly and respect website terms of service when scraping.

---
## Next steps

- Automated tests to ensure code reliability and prevent regressions

- Interactive API documentation available at /docs (FastAPI default)

- Support for sending reports to multiple email recipients

- Ability to filter products by price range or other criteria

- Add pagination support to scrape more products beyond the first page

- Improve Excel report formatting with styles and summaries

- Add logging and error monitoring for better maintainability

- Dockerize the application for easier deployment and environment consistency
---

## Contact

For questions or issues, contact Murilo Alcantu.
