# NGO Volunteer Management System

A command-line tool to manage volunteers for NGO field operations.

I built this after my internship at Bharat Vikas Parishad, Lucknow where I spent 
a month doing data management manually in Excel. Tracking who showed up, which 
activity they did, and generating end-of-month summaries was tedious. This automates that.

## What it does

- Register volunteers with name and phone number
- Mark daily attendance and assign an activity type
- View a volunteer's full profile and attendance history
- List all registered volunteers with total days present
- Generate a monthly summary report by activity
- Export monthly report to a CSV file
- Remove a volunteer from records

## Activity categories (based on real BVP programme structure)

Week 1 — Environmental (tree plantation drives)
Week 2 — Education (teaching underprivileged children)
Week 3 — Orphanage outreach
Week 4 — Old age home visits

## How to run it

No external libraries needed — runs on standard Python 3.

git clone https://github.com/mishranarayanii12-ctrl/ngo-volunteer-management
cd ngo-volunteer-management
python ngo.py

All data is saved locally in a volunteers.json file that gets created 
automatically on first run.

## What I learned building this

- Structuring a real multi-feature CLI app with a clean menu system
- JSON file handling for persistent data storage
- Preventing duplicate entries (same volunteer, same day)
- Generating filtered reports from structured data
- Exporting data to CSV for spreadsheet compatibility

## Known limitations

- No login or password protection
- Single user system — not built for multiple admins
- Data stored locally, not on a server

## Possible improvements

- Add login system for security
- Export to Excel directly instead of CSV
- Track volunteer hours instead of just days
