import requests
from multiprocessing.pool import ThreadPool
import time
import os


def process_sequential(link):

    file_name_start = link.rfind("/") + 1
    file_name = link[file_name_start:]

    req = requests.get(link)
    if req.status_code == requests.codes.ok:
        with open(file_name, 'wb') as pdf:
            for data in req:
                pdf.write(data)

    if file_name == "proceedings.pdf":
        file_name = "file1.pdf"
    elif file_name == "A17_FlightPlan.pdf":
        file_name = "file2.pdf"
    elif file_name == "1-s2.0-S0140673617321293-mmc1.pdf":
        file_name = "file3.pdf"
    elif file_name == "Peloponnese_map.pdf":
        file_name = "file4.pdf"

    print(file_name, "-> done")


def process_parallel(link):

    file_name_start = link.rfind("/") + 1
    file_name = link[file_name_start:]

    r = requests.get(link)
    if r.status_code == requests.codes.ok:
        with open(file_name, 'wb') as pdf:
            for data in r:
                pdf.write(data)

    if file_name == "proceedings.pdf":
        file_name = "file1.pdf"
    elif file_name == "A17_FlightPlan.pdf":
        file_name = "file2.pdf"
    elif file_name == "1-s2.0-S0140673617321293-mmc1.pdf":
        file_name = "file3.pdf"
    elif file_name == "Peloponnese_map.pdf":
        file_name = "file4.pdf"

    return file_name


while True:
    try:
        thread_mode = int(input("Enter thread mode (0 or 1): "))
        if thread_mode > 1 or thread_mode < 0:
            print("Please enter the right input.")
            continue
        else:
            break
    except ValueError:
        print("Please enter the right input.")


links_list = ["http://www.ubicomp.org/ubicomp2003/adjunct_proceedings/proceedings.pdf",
            "https://www.hq.nasa.gov/alsj/a17/A17_FlightPlan.pdf",
            "https://ars.els-cdn.com/content/image/1-s2.0-S0140673617321293-mmc1.pdf",
            "http://www.visitgreece.gr/deployedFiles/StaticFiles/maps/Peloponnese_map.pdf"
            ]

if thread_mode == 0:
    start_time = time.time()
    mode = "Single-threaded"
    print("Mode:", mode)
    print("Files:")

    for links in links_list:
        process_sequential(links)

else:
    start_time = time.time()
    mode = "Multi-threaded"
    print("Mode:", mode)
    print("Files:")

    results = ThreadPool(len(links_list)).imap_unordered(process_parallel, links_list)
    for r in results:
        print(r, "-> done")

old_name1 = "proceedings.pdf"
new_name1 = "file1.pdf"
old_name2 = "A17_FlightPlan.pdf"
new_name2 = "file2.pdf"
old_name3 = "1-s2.0-S0140673617321293-mmc1.pdf"
new_name3 = "file3.pdf"
old_name4 = "Peloponnese_map.pdf"
new_name4 = "file4.pdf"

os.rename(old_name1, new_name1)
os.rename(old_name2, new_name2)
os.rename(old_name3, new_name3)
os.rename(old_name4, new_name4)

end_time = time.time()

execution_time = end_time - start_time

print("Time:", "%.2f" % round(execution_time, 2), "s")
