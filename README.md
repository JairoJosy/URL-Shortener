# URL Shortener

This is a simple desktop application that allows you to shorten URLs using the Bitly URL shortening service. It is built using Python 3.9, PyQt5, and the PyShorteners library.

![Screenshot](screenshot.png)

## Features

* Shorten a URL using the Bitly API


* Copy the shortened URL to the clipboard with one click


* Animated "Copied" feedback with a green color

## Installation

To run the URL Shortener application, you will need to install the following dependencies:

* Python 3.9 or later

* PyQt5

* PyShorteners

You can install these dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

Before using the application, you will need to add your Bitly API code. Here's how to do it:

1. Sign up for a free Bitly account.

2. After you log in to your account, go to your Bitly API settings.

3. Click the "Generic Access Token" link to generate a new API code.

4. Copy the API code to your clipboard.

Now that you have your Bitly API code, open the url_shortener.py file in a text editor and find the BITLY_API_CODE variable on line 15. Replace the placeholder value with your Bitly API code.

To start the application, run the following command:

```bash
python url_shortener.py
```

Enter a URL in the input field and click the "Shorten" button to get a shortened URL. Click the "Copy" button to copy the shortened URL to the clipboard.

When you click the "Copy" button, the button will slowly disappear and show "Copied" in green. The copied text will also be green. The button will then reset to its original state after a few seconds.

## Using the application as an executable

If you want to reduce the hassle of running the application from the command line, you can use the executable application, which can be found both in the repository and the releases page. 

## Credits

This project was created by JAIRO JOSY as a demonstration of using the Bitly API with Python and PyQt5.

The code for the animated "Copied" feedback was adapted from [this Stack Overflow answer.](https://stackoverflow.com/a/54814230/)

## Contributing

Contributions are welcome ! If you find a bug or would like to add a new feature, please submit a pull request.

## Licence

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the LICENSE file for details.

