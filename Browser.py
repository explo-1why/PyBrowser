def online():
    import urllib.request
    if (urllib.request.urlopen("https://raw.githubusercontent.com/explo-1why/PyBrowser/refs/heads/main/online.txt").read().decode())=="ping successful":
        return True
    else:
        return False
if not online():
    print("You are currently not online.")
    import time
    time.sleep(5)
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
print("This is a simple web file viewer and downloader.")
while True:
    url=input("Enter URL for website: ")
    option=input("Download or View file: ")
    if option.lower()==("download"):
        filename=input("Enter filename for download including extension: ")
        download((filename), (fetch(url)))
    elif option.lower()==("view"):
        print(fetch(url))
