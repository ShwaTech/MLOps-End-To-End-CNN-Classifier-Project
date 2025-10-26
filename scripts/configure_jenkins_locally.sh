#!bin/bash

## After The Installed Jenkins Locally:
sudo systemctl start jenkins

sudo systemctl status jenkins

## We Need To Make Tunnel To Allow Jenkins To Be Used Everywhere
## So I have used ngrok to make a tunnel to make jenkins accessable everywhere
## So I Cloud Run Pipelines and Do A lot With It

# Install ngrok
sudo snap install ngrok

# Configure ngrok and authentake it
ngrok config add-authtoken <YOUR_NGROK_AUTH_TOKEN>

# Get Token from after login
https://dashboard.ngrok.com/get-started/your-authtoken

# Make The Tunnel on Top of Jenkins Running Port (8080)
ngrok http 8080

# it Will Give you something like this:
## Forwarding                    https://7d91552adb12.ngrok-free.app -> http://localhost:8080
## Take ---> https://7d91552adb12.ngrok-free.app  <--- and use it as the URL Secret on GitHub