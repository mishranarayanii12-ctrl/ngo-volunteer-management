import json
import os
import csv
from datetime import date

DATA_FILE = "volunteers.json"

ACTIVITIES = {
    "1": "Environmental (Tree Plantation)",
    "2": "Education (Underprivileged Children)",
    "3": "Orphanage Outreach",
    "4": "Old Age Home Visit"
}


def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(volunteers):
    with open(DATA_FILE, "w") as f:
        json.dump(volunteers, f, indent=4)


def find_volunteer(volunteers, name):
    for v in volunteers:
        if v["name"].lower() == name.lower():
            return v
    return None


def register_volunteer():
    volunteers = load_data()
    name = input("Volunteer name: ").strip()
    if not name:
        print("Name can't be empty.")
        return
    if find_volunteer(volunteers, name):
        print(f"'{name}' is already registered.")
        return
    phone = input("Phone number: ").strip()
    volunteer = {
        "name": name,
        "phone": phone,
        "joined": str(date.today()),
        "attendance": [],
    }
    volunteers.append(volunteer)
    save_data(volunteers)
    print(f"\n✅ {name} registered successfully.")


def mark_attendance():
    volunteers = load_data()
    name = input("Volunteer name: ").strip()
    volunteer = find_volunteer(volunteers, name)
    if not volunteer:
        print(f"No volunteer found with name '{name}'. Please register first.")
        return
    print("\nSelect activity for today:")
    for key, val in ACTIVITIES.items():
        print(f"  {key}. {val}")
    choice = input("Enter option (1-4): ").strip()
    if choice not in ACTIVITIES:
        print("Invalid choice.")
        return
    today = str(date.today())
    already = [a for a in volunteer["attendance"] if a["date"] == today]
    if already:
        print(f"Attendance already marked for {name} today ({already[0]['activity']}).")
        return
    volunteer["attendance"].append({"date": today, "activity": ACTIVITIES[choice]})
    save_data(volunteers)
    print(f"\n✅ Attendance marked — {name} | {ACTIVITIES[choice]} | {today}")


def view_volunteer():
    volunteers = load_data()
    name = input("Volunteer name: ").strip()
    volunteer = find_volunteer(volunteers, name)
    if not volunteer:
        print(f"No record found for '{name}'.")
        return
    print(f"\n===== VOLUNTEER PROFILE =====")
    print(f"Name    : {volunteer['name']}")
    print(f"Phone   : {volunteer['phone']}")
    print(f"Joined  : {volunteer['joined']}")
    print(f"Total Days Present: {len(volunteer['attendance'])}")
    if volunteer["attendance"]:
        print("\nAttendance Log:")
        for entry in volunteer["attendance"]:
            print(f"  {entry['date']}  |  {entry['activity']}")


def list_all_volunteers():
    volunteers = load_data()
    if not volunteers:
        print("No volunteers registered yet.")
        return
    print(f"\n===== ALL VOLUNTEERS ({len(volunteers)} total) =====")
    for v in volunteers:
        days = len(v["attendance"])
        print(f"  {v['name']:<20} | Phone: {v['phone']:<15} | Days Present: {days}")


def monthly_report():
    volunteers = load_data()
    if not volunteers:
        print("No data to generate report.")
        return
    month = input("Enter month (YYYY-MM, e.g. 2026-06): ").strip()
    print(f"\n===== MONTHLY REPORT — {month} =====")
    activity_count = {a: 0 for a in ACTIVITIES.values()}
    total_attendance = 0
    for v in volunteers:
        monthly = [a for a in v["attendance"] if a["date"].startswith(month)]
        if monthly:
            print(f"\n  {v['name']} — {len(monthly)} day(s)")
            for entry in monthly:
                print(f"    {entry['date']}  |  {entry['activity']}")
                activity_count[entry["activity"]] += 1
                total_attendance += 1
    print(f"\n--- Activity Summary ---")
    for activity, count in activity_count.items():
        if count > 0:
            print(f"  {activity}: {count} volunteer-day(s)")
    print(f"\nTotal attendance entries this month: {total_attendance}")


def export_to_csv():
    volunteers = load_data()
    if not volunteers:
        print("No data to export.")
        return
    month = input("Enter month to export (YYYY-MM, e.g. 2026-06): ").strip()
    filename = f"report_{month}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Volunteer", "Phone", "Date", "Activity"])
        for v in volunteers:
            for entry in v["attendance"]:
                if entry["date"].startswith(month):
                    writer.writerow([v["name"], v["phone"], entry["date"], entry["activity"]])
    print(f"\n✅ Report exported to {filename}")


def delete_volunteer():
    volunteers = load_data()
    name = input("Enter name of volunteer to remove: ").strip()
    volunteer = find_volunteer(volunteers, name)
    if not volunteer:
        print(f"No volunteer found with name '{name}'.")
        return
    confirm = input(f"Are you sure you want to remove '{name}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        volunteers.remove(volunteer)
        save_data(volunteers)
        print(f"✅ {name} removed from records.")
    else:
        print("Cancelled.")


def main():
    menu = {
        "1": ("Register new volunteer", register_volunteer),
        "2": ("Mark attendance", mark_attendance),
        "3": ("View volunteer profile", view_volunteer),
        "4": ("List all volunteers", list_all_volunteers),
        "5": ("Generate monthly report", monthly_report),
        "6": ("Export report to CSV", export_to_csv),
        "7": ("Remove volunteer", delete_volunteer),
        "8": ("Exit", None),
    }

    print("=========================================")
    print("   NGO VOLUNTEER MANAGEMENT SYSTEM")
    print("   Bharat Vikas Parishad — Lucknow")
    print("=========================================")

    while True:
        print("\nWhat would you like to do?")
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")
        choice = input("\nEnter option: ").strip()
        if choice == "8":
            print("Goodbye.")
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("Invalid option. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
