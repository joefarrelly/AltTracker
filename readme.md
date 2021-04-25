# Alt Tracker for WoW

## Overview

Alt Tracker is an app that tracks all of a players characters in World of Warcraft. As Blizzard uses OAuth 2.0 to secure their APIs, I can use OAuth for authentication of a user which is handled through their website. I created this app due to wanting to be able to see all of my own characters data in one place, however as a few friends were interested in it as well I adapted it to include OAuth in order for others to be able to use it for the same purpose.

## Technologies

- Python 3.8.6
- Django 3.1.5
- MySQL 8.0.21
- Bootstrap 4.4.1

## Feature List

- Tracks all characters on an account
- Display them all in a table with the following columns:
    - Index
    - Faction
    - Level
    - Name
    - Realm
    - Class
    - Mount (represents the highest level of mount training the character has on a scale of 1 - 4)
    - Garrison (the level of the characters garrison)
    - MT (whether or not the mage tower building has been constructed)
    - Profession 1 and 2 (name of the profession with a link to a page of all recipes the character has learnt)
    - More (link to a page showing the characters appearance [WIP])
- Table is sortable by clicking most column headers
- Provides an overview of each profession for all characters showing all known recipes with external links to the relevant WoW Head pages
- Display the characters appearance as it would be in-game along with the characters currently equipped gear [WIP]

