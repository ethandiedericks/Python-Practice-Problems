import csv
# read contents of the original file with our context manager
with open("names.csv", "r") as file:
    reader = csv.DictReader(file)

  # initialize a new file in write mode with our context manager
    with open("new_names.csv", "w") as f:
        # specify the new fieldnames
        fieldnames = ["fullname", "email", "domain_name"]
        # create a writer object with the new file name and fieldnames
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        # write row with the fieldnames
        writer.writeheader()
    # create a new csv file with the fullname, email and domain name
        for line in reader:
            # pull first name from original csv
            first = line["first_name"]
            # pull last name from original csv
            last = line["last_name"]
            # create a fullname with first and last names
            fullname = first + " " + last
            # find index of the @ symbol
            index_at = line["email"].index("@")
            # use that index to slice from the @ symbol to the end of the email
            domain_name = line["email"][index_at + 1:]
            # write the info to the new file
            writer.writerow({"fullname" : fullname, "email" : line["email"], "domain_name" : domain_name})
