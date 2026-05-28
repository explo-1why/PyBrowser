def online():
    import urllib.request
    if (urllib.request.urlopen("https://raw.githubusercontent.com/explo-1why/PyBrowser/refs/heads/main/online.txt").read().decode().strip())=="ping":
        return True
    else:
        return False
if not online():
    print("You are currently not online.")
    import time
    time.sleep(1)
    print("Terminating Script")
    import sys
    sys.exit(1)
#Online Check ends here
def fetch(url):
    import urllib.request
    return urllib.request.urlopen(url).read().decode()
def download(filename, content):
    open(filename, "w").write(content)
#The actual process starts here
print("This is a simple web file viewer, runner and downloader.")
while True:
    url=input("Enter URL for website: ")
    option=input("Download, View or Run file: ")
    if option.lower()==("download"):
        filename=input("Enter filename for download including extension: ")
        download((filename), (fetch(url)))
    elif option.lower()==("view"):
        print(fetch(url))
    elif option.lower()==("run"):
        try:
            exec(fetch(url))
        except Exception as error:
            print("That file isn't a Python file or it has an error.")
            print("Error Code: ",error)
