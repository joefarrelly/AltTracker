# Alt Tracker for WoW

## Overview

Alt Tracker is an app that tracks all of a players characters in World of Warcraft. As Blizzard uses OAuth 2.0 to secure their APIs, I can use OAuth for authentication of a user which is handled through their website. I created this app due to wanting to be able to see all of my own characters data in one place, however as a few friends were interested in it as well I adapted it to include OAuth in order for others to be able to use it for the same purpose.

## Technologies

- Python 3.8.6
- Django 3.1.5
- MySQL 8.0.21
- Bootstrap 4.4.1
- jQuery 3.5.1
- Redis 5.0.7
- Apache 2.4.41
- Ubuntu 20.04

## Feature List

### Alts Page

- Accessible by clicking the 'Alt Tracker' button on the home page
- All characters linked to the account are shown in a table with the following columns:
    - Faction
    - Level
    - Name
    - Realm
    - Class
    - Profession 1 and 2 (name of the profession with an embedded link to a page of all recipes the character has learnt)
    - Gear (average item level of the characters equipped gear with an embedded link to a page showing the characters appearance)
    - Last Updated (how long ago the character was updated)
    - Update character button (to update individual characters rather than them all)
- Table is sortable by clicking column headers (by default it will be sorted by character level then item level)
- Clicking the 'Sync Characters' button will redirect to Battle.net to request access to your World of Warcraft data
- Clicking the 'Refresh All' button will update each character's data in the table one-by-one

### Alts Checker Page

- Accessible by clicking the 'Alt Checker' button on the 'Alts' page
- All characters linked to the account are shown in a table with the following columns:
    - Faction
    - Level
    - Name
    - Realm
    - Class
    - Mount (represents the highest level of mount training the character has)
    - Garrison (the level of the characters garrison)
    - MT (whether or not the mage tower building has been constructed)
    - SM (whether the character has completed the shadowmourne quest line, only warriors, paladins and death knights are eligible)
- Table is sortable by clicking column headers (by default it will be sorted by character level then item level)

### Alt Profession Page

- Accesible by clicking the profession of a character on the 'Alts' page
- There are several tables of profession data with the following columns:
    - ID
    - Name
    - Link (link to the wowhead page of the recipe)
- Breaks down profession data into separate tables for each tier (Battle for Azeroth, Legion, Warlords of Draenor, etc)

### Alt Details Page

- Accessible by clicking the item level of a character on the 'Alts' page
- You can see the appearance and equipped gear of the character in the same style as in-game and on the offical WoW Armory site
- Hovering over an item will show a tooltip with more info on the item


## TO:DO

- Export table data to CSV
- Allow for storage of in-game keybinds for each character, potentially per spec on each character