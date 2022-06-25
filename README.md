# Main information

The script is written using the **tesseract**, **ocv**, also **pymorph2** libraries. Its essence boils down to downloading the result of the iq test as an image, and then using computer vision and tesseract to recognize the necessary fields and then entering them into the sqlite database.
**sqlite3** is used as the database

## Installation

Use the package manager [**pip**](https://pip.pypa.io/en/stable/) to install requirements.txt.

```bash
pip install -r requirements.txt
```

## Example

| Name  | Result   |
| ------------ | ------------ |
|  Andrew | 95  |
|  Mark | 102  |

[![](https://cdn.discordapp.com/attachments/930134889225912323/990384704387711006/unknown.png)]

## Important
**To work properly, you need to create an &laquo;images&raquo; directory**
[![](https://cdn.discordapp.com/attachments/930134889225912323/989847320088694864/unknown.png)]

## Features

*- functionality extension*
