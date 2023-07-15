import win32com.client
import os

def get_pending_updates():
    update_session = win32com.client.Dispatch("Microsoft.Update.Session")
    searcher = update_session.CreateUpdateSearcher()
    search_result = searcher.Search("IsInstalled=0")
    updates = search_result.Updates

    pending_updates = []
    missing_updates = []

    for update in updates:
        update_properties = {
            'Title': update.Title,
            'Description': update.Description,
            'KBArticleIDs': update.KBArticleIDs,
            'Categories': [category.Name for category in update.Categories]
        }
        pending_updates.append(update_properties)
        missing_updates.append(update.Title)

    return pending_updates, missing_updates

if __name__ == '__main__':
    pending_updates, missing_updates = get_pending_updates()

    if pending_updates:
        print("Pending Windows Updates:")
        for update in pending_updates:
            print(f"Title: {update['Title']}")
            print(f"Description: {update['Description']}")
            print(f"KB Article IDs: {', '.join(update['KBArticleIDs'])}")
            print(f"Categories: {', '.join(update['Categories'])}")
            print("-----")
    else:
        print("No pending updates.")

    if missing_updates:
        output = "The following updates are missing:\n"
        for update in missing_updates:
            output += f"{update}\n"
    else:
        output = "Windows is up to date!"

    output_dir = r"C:\Temp\XDR"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, "windows_update_status.txt")
    with open(output_path, "w") as f:
        f.write(output)
