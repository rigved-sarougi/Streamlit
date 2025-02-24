import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st
import pandas as pd

# Authenticate and connect to Google Sheets
def connect_to_gsheet(creds_json, spreadsheet_name, sheet_name):
    scope = ["https://spreadsheets.google.com/feeds", 
             'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", 
             "https://www.googleapis.com/auth/drive"]
    
    credentials = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scope)
    client = gspread.authorize(credentials)
    spreadsheet = client.open(spreadsheet_name)  
    return spreadsheet.worksheet(sheet_name)  # Access specific sheet by name

# Google Sheet credentials and details
SPREADSHEET_NAME = 'Streamlit'
SHEET_NAME = 'Sheet1'
CREDENTIALS_FILE = {
  "type": "service_account",
  "project_id": "orbital-stream-451911-f8",
  "private_key_id": "d2a7ecbbe191f851349b7a1b51c686941a1bd960",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCvT+SORyuuY9vp\nWPayvlfCFmVCu1McpovYkKRhlWkJrvtwdQUW2+cAQGloWohmwYZL0qMZIWko9imm\nUbct2xlgLSiZgIWucY5z/EE6WslOCIOTWh/e0/5FxvaQJFw+pVxVFU9DocC4FSZq\n+5bkGOCoWis0/smYz63W0KWgXMNAwp2FelZ9eoZzYDt3L8W1UZgh/yfU3e7xHrts\nyMPTbi/1Dy73uQX6XXTQ+KOmvARATp3G1mxuQ0dta+18Zdkd0mRiNzRPOC664MQ1\nxVwrk99cvhDZKpf042PJ5h2Hvrm/9K4N3C0tu939HCufXCm+No4Uv3/ZnYKt4CWF\ny5n3r1IhAgMBAAECggEADuQfoxk3A+NeDuJcZB7oZ+dMlyA/xUd9SfoxSEuvZh/r\noigCdGhd5QbTnUZRXz8Rd/fOnEga/Vx5ebPnthit/V4gnHdPA5wIMGBtLvZ+smbl\nPDszyVLi/ozRrTk1b6nOn7iFaNaAvvIm9v/jV4Eodgxgrqn0uErttnk3FFnEyQeK\n5xagB6CKXLiWhWqkDuUCQmUWshhep+87mayCW8APkxMhwIsU7nkR84ypIc6EkB0c\n74rVKwP+HigERhKV/pR05euaxxu3gWo9Is56OeGJDaV13f5uHpbd2Sp0CV+AXNqV\n6Jp/g0Bgovp4VihC4St+arE5/+NtXP3PyUpxqckP5QKBgQDZLFDXKYRqGKAUXFM3\ncnLy29ye1QoGgPjOwwlx271GGGqRdY11wyE3P8e69gqT7quplXKX6UHjD6Jw5ToL\n7TE9zZQKra+sAxTJDqzY0Ul+/RcerlaPBNHnd8fr4qrMXGBWdkka9owjbV6GvzpJ\n5+JNLX2iKzswvQ/lO3a9CnKtBQKBgQDOp6lEi2hJS4rmV9Jh1ff3Tuzr1zTZZdFO\nYQNqGVWjACuVpejzrB+g3BxbEt6DJ/m06zB/pTlCsl/kOAeeLusw+rqnLZlzo7k9\nJ2mWVymxqM5Mi8dlCbrZLeCnT7k9rZNRgGazFExxBdq3b+JdOZBpl/UAM23FVpBc\nqOq2/+W7bQKBgHmI92Sx80x8o3lBgcCR6ApJSFoK1yV0n8j2FR8G3hGQMHNe2d+B\nZ+FHbDsQ3jKTarXo0Mx62Uh8w2dyoN1zzA7OMX8YXCtjPgqWj9x2oy7R7FJbNk2r\nYNysh9FWdEcRm0hHwfm46AwbdL7r3W7muhp+zsQmdWV9KJwcfwKkCjERAoGBAMpu\nxosUnJWf4HJ/eODJvtuNftwPtf93k67ZrYSTSKYhlpBDM4zvARSMSWKVe06zLBKj\niKChcxP4s6JVmHDFuTIDijAVpQn4SY60OuRAgeE8YMnu6uX4wAXawQRkPitDCtp9\nkxy9N5xHhdbHTNDRgLtPVXpa5p62izeZaELXLW2JAoGAaWEsqrQGxWWYL/bMZTTt\nZ6cGtlXePB/HEruXjib1t431N7kq0+u0ZphQbktQLKVIeRFhhLPbplH+9ha1H/AQ\nvAhJiCy5b8b4nNKj1w7RHTt+/VNICxB/ArpKCJqii2HIkAERLOtcAkLSnDo4b28E\nRH8OG++A1OBujG+63wiaHwc=\n-----END PRIVATE KEY-----\n",
  "client_email": "streamlit-app@orbital-stream-451911-f8.iam.gserviceaccount.com",
  "client_id": "106921985923872598239",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/streamlit-app%40orbital-stream-451911-f8.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

# Connect to the Google Sheet
sheet_by_name = connect_to_gsheet(CREDENTIALS_FILE, SPREADSHEET_NAME, sheet_name=SHEET_NAME)

st.title("Simple Data Entry using Streamlit")

# Read Data from Google Sheets
def read_data():
    data = sheet_by_name.get_all_records()  # Get all records from Google Sheet
    return pd.DataFrame(data)

# Add Data to Google Sheets
def add_data(row):
    sheet_by_name.append_row(row)  # Append the row to the Google Sheet

# Sidebar form for data entry
with st.sidebar:
    st.header("Enter New Data")
    # Assuming the sheet has columns: 'Name', 'Age', 'Email'
    with st.form(key="data_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=120)
        email = st.text_input("Email")
        # Submit button inside the form
        submitted = st.form_submit_button("Submit")
        # Handle form submission
        if submitted:
            if name and email:  # Basic validation to check if required fields are filled
                add_data([name, age, email])  # Append the row to the sheet
                st.success("Data added successfully!")
            else:
                st.error("Please fill out the form correctly.")

# Display data in the main view
st.header("Data Table")
df = read_data()
st.dataframe(df, width=800, height=400)

