# Project Setup Guide

This document explains how to run python.

---

## 0. Tools you need and set up
```bash
Python 3.13+ → email sending
Laravel 10+ → backend logging
PostgreSQL or any database you want → storing click logs
Ngrok → expose local Laravel server to internet for email link (you can get this ngrok in app store)
Gmail with 2FA & App Password → secure SMTP login (you can see this in google.account)
```

## 1. fill up the Element Variable for Email
```bash
sender_email = os.getenv("MAIL_SENDER", "include_email_sender_here")
receiver_email = os.getenv("MAIL_RECEIVER", "put_email_receiver_here")
password = os.getenv("MAIL_APP_PASSWORD", "put_mail_app_pass_here")
````

## 2. in Laravel dont forget to
```bash
php artisan serve
run ngrok ex. ngerok http 8000
````

---

## 3. To run the file (in Terminal)
```bash
send_email.py
````
