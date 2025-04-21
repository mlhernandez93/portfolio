# Playwright Behave Automation Framework

This repository contains an automation framework built with Python, Playwright, and Behave for testing web applications.

## Table of Contents

* [Description](#description)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [File Structure](#file-structure)
* [Code Explanation](#code-explanation)
* [Contributing](#contributing)
* [License](#license)

## Description

This framework provides a foundation for automating web browser interactions using Playwright and defining test scenarios in a Behavior-Driven Development (BDD) style with Behave. It includes setup and teardown of the browser context and page, as well as example step definitions for navigation and login actions.

## Prerequisites

* Python 3.6 or higher
* pip (Python package installer)

## Installation

1.  Clone the repository:

    ```bash
    git clone <your_repository_url>
    cd <your_repository_directory>
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python -m venv .venv
    ```

3.  Activate the virtual environment:

    * On Windows:

        ```bash
        venv\Scripts\activate
        ```

    * On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4.  Install the required packages:

    ```bash
    pip install behave playwright
    playwright install chromium  # Install Chromium browser
    ```

## Usage

1.  Ensure your web application is running and accessible.

2.  Run the Behave tests:

    ```bash
    behave features
    ```

    This will execute the `.feature` files in the `features` directory and run the corresponding step definitions.

## File Structure
