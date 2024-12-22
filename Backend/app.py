from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import socket
from urllib.parse import urlparse
import whois
import requests
import pandas as pd
from numpy import genfromtxt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from datetime import datetime
import ssl

app = Flask(__name__)
CORS(app)

# Define a function to check for an IP address in the URL
def having_ip_address(url):
    match = re.search(r'\d+\.\d+\.\d+\.\d+', url)
    return 1 if match else 0

# URL Length
def url_length(url):
    return 1 if len(url) < 54 else -1 if len(url) > 75 else 0

# Check if URL uses shortening service
def shortening_service(url):
    shortening_services = ["bit.ly", "tinyurl.com", "goo.gl", "shorte.st", "go2l.ink", "x.co"]
    return 1 if any(service in url for service in shortening_services) else 0

# Check for '@' symbol in URL
def having_at_symbol(url):
    return 1 if "@" in url else 0

# Check for double slash redirecting
def double_slash_redirecting(url):
    return 1 if url.count('//') > 1 else 0

# Check if URL has prefix/suffix in the domain
def prefix_suffix(url):
    return 1 if '-' in urlparse(url).netloc else 0

# Check for the number of subdomains
def having_sub_domain(url):
    if having_ip_address(url):
        return 1
    subdomains = urlparse(url).netloc.split('.')
    return 1 if len(subdomains) > 3 else 0

# Check SSL certificate (simplified approach)
def ssl_final_state(url):
    try:
        hostname = urlparse(url).netloc
        context = ssl.create_default_context()
        with context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
            s.connect((hostname, 443))
        return 1
    except:
        return 0

# Domain registration length (WHOIS lookup)
def domain_registration_length(url):
    try:
        domain = whois.whois(urlparse(url).netloc)
        expiration_date = domain.expiration_date
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]
        return 1 if (expiration_date - datetime.now()).days / 365 >= 1 else 0
    except:
        return 0

# Extract other features
def favicon(url):
    return 0 # Placeholder, requires HTML parsing to check favicon

def port(url):
    return 0 # Placeholder, not determined from URL alone

def https_token(url):
    return 1 if 'https' in urlparse(url).netloc else 0

def request_url(url):
    return 0 # Placeholder, would need HTML parsing

def url_of_anchor(url):
    return 0 # Placeholder, would need HTML parsing

def links_in_tags(url):
    return 0 # Placeholder, would need HTML parsing

def sfh(url):
    return 0 # Placeholder, would need HTML parsing

def submitting_to_email(url):
    return 1 if "mailto:" in url else 0

def abnormal_url(url):
    return 1 if re.search(r'\.co\.\w\w$', url) else 0

def redirect(url):
    return 0 # Placeholder, would need to follow redirects

def on_mouseover(url):
    return 0 # Placeholder, not determined from URL alone

def right_click(url):
    return 0 # Placeholder, would need HTML parsing

def popup_window(url):
    return 0 # Placeholder, would need HTML parsing

def iframe(url):
    return 0 # Placeholder, would need HTML parsing

def age_of_domain(url):
    try:
        domain = whois.whois(urlparse(url).netloc)
        creation_date = domain.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        age = (datetime.now() - creation_date).days / 365
        return 1 if age >= 6 else 0
    except:
        return 0

def dns_record(url):
    try:
        socket.gethostbyname(urlparse(url).netloc)
        return 1
    except:
        return 0

def web_traffic(url):
    return 0 # Placeholder, typically requires external service

def page_rank(url):
    return 0 # Placeholder, typically requires external service

def google_index(url):
    return 0 # Placeholder, typically requires Google search API

def links_pointing_to_page(url):
    return 0 # Placeholder, would need to follow links

def statistical_report(url):
    return 0 # Placeholder, would need more advanced tools

# Collect all features
def extract_url_features(url):
    return [
        having_ip_address(url),
        url_length(url),
        shortening_service(url),
        having_at_symbol(url),
        double_slash_redirecting(url),
        prefix_suffix(url),
        having_sub_domain(url),
        ssl_final_state(url),
        domain_registration_length(url),
        favicon(url),
        port(url),
        https_token(url),
        request_url(url),
        url_of_anchor(url),
        links_in_tags(url),
        sfh(url),
        submitting_to_email(url),
        abnormal_url(url),
        redirect(url),
        on_mouseover(url),
        right_click(url),
        popup_window(url),
        iframe(url),
        age_of_domain(url),
        dns_record(url),
        web_traffic(url),
        page_rank(url),
        google_index(url),
        links_pointing_to_page(url),
        statistical_report(url)
    ]

feature = genfromtxt('phishing_1.csv', delimiter=',', usecols=(i for i in range(1, 31)))
class_value = genfromtxt('phishing_1.csv', delimiter=',', usecols=(-1))
labels = LabelEncoder().fit_transform(class_value)
feature_std = StandardScaler().fit_transform(feature)
x_train, x_test, y_train, y_test = train_test_split(feature_std, labels, test_size=0.25, random_state=0)
imputer = SimpleImputer(strategy="mean")
x_train_imputed = imputer.fit_transform(x_train)
x_test_imputed = imputer.transform(x_test)
clf_rf = RandomForestClassifier()
clf_rf.fit(x_train, y_train)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data['url']
    features = extract_url_features(url)
    prediction = clf_rf.predict([features])
    result = 'spam' if prediction[0] == 1 else 'not spam'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
