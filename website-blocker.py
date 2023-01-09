import datetime

now = datetime.datetime.now()
end_time = now.replace(hour=18, minute=0, second=0, microsecond=0)  # block sites before 6pm
sites_to_block = ['www.facebook.com']
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"  # windows DNS file
redirect = "127.0.0.1"


def block_sites():
    if now > end_time:  # block sites
        print("block sites")
        with open(hosts_path, 'r+') as hostsfile:
            hosts_content = hostsfile.read()
            for site in sites_to_block:
                if site not in hosts_content:
                    hostsfile.write(redirect + " " + site + "\n")
    else:  # allow sites
        print("allow sites")
        with open(hosts_path, 'r+') as hostsfile:
            lines = hostsfile.readlines()
            hostsfile.seek(0)
            for line in lines:
                if not any(site in line for site in sites_to_block):
                    hostsfile.write(line)
            hostsfile.truncate()


if __name__ == "__main__":  # run method as script
    block_sites()
