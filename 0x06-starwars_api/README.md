# 0x06. Star Wars API

## Description

This project involves working with the Star Wars API to fetch and display character names for a specified movie in the correct order.

---

## Requirements

- All files are interpreted on **Ubuntu 20.04 LTS** using **Node.js** (version 10.14.x).
- Code is compliant with the **semistandard** style guide.
- The script must use the `request` module to make API requests.

---

## Installation

1. Install Node.js 10.x:
   ```bash
   curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
   sudo apt-get install -y nodejs

Install required modules:
bash
sudo npm install semistandard --global
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules

Usage
Make the script executable:
bash
chmod +x 0-starwars_characters.js

Run the script with a movie ID:
bash
./0-starwars_characters.js <movie_id>

Example:
bash
./0-starwars_characters.js 3

Example Output
For movie ID 3:
mathematica

Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna

Author
Silas Edet
GitHub: BrotherSilas
Email: Silasedetsnr@gmail.com
