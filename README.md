# Phase-3-project-market-place-cli

# Flatiron Market Place

Welcome to Flatiron Market Place! This project is a command-line application that simulates an online marketplace where users can buy and sell items.

## Introduction

Flatiron Market Place is a command-line application built using Python and SQLAlchemy that allows users to interact with an online marketplace. Users can log in or sign up, view items on sale, search item, add their own items for sale, buy items, and view their transaction history.

## Features

### Login and Sign Up

Users can log in with their email or sign up if they're new to the platform. The application validates user input and ensures that the email follows a valid format.

### View Items

Logged-in users can view a list of items available for sale. The list of items includes item details such as title, description, price, and the name of the seller.

### Search Item

Logged-in users can search an item to buy. The application will show all matching items if they're found.

### Add Item For Sale

Logged-in users can add items they want to sell to the marketplace. They provide details like item title, description, and price. The item is associated with the seller's account.

### Buy An Item

Logged-in users can buy items listed by other sellers. They enter the item ID of the item they want to buy. The transaction is recorded, and the item is removed from the marketplace.

### View Your Transactions

Logged-in users can view a list of their past transactions. This list includes the title of the item, the transaction amount, and the date of the transaction.

### Exit

Users can exit the application when they want.

## Getting Started

### Requirement

- Python 3.8
- Pipenv 

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nnpk1007/phase-3-project-cli
   
   cd phase-3-project-cli

2. Install the required dependencies:
    ```bash
    pipenv install

3. Launching subshell in virtual environment
    ```bash
    pipenv shell

3. Create tables (because I have .gitignore file to ignore data.db file, so you have to do this step to avoid error)
    ```bash
    cd lib
    alembic upgrade head

4. Set up initial data (you can skip this step if you don't want any data in your table):
    ```bash
    python3 seeds.py
    ```
        
6. Run the applicaiton (you're already in lib folder):
    ```bash
    python3 cli.py

### Usage

Upon running the application, you'll be presented with a main menu where you can log in or sign up.
Once logged in, you can choose many options such as viewing items, adding items for sale, buying items, and viewing your transactions.
Follow the on-screen prompts to interact with the application.

### License
This project is licensed under the MIT License. 

