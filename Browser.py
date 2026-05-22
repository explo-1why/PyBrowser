def fetch(url):
    import urllib.request
    return urllib.request.urlopen(url).read().decode()
def download(filename, content):
    open(filename, "w").write(content)
print("This is a simple web file viewer and downloader.")
import time
while True:
    url=input("Enter URL for website: ")
    option=input("Download or View file: ")
    if option.lower()==("download"):
        filename=input("Enter filename for download including extension: ")
        download((filename), (fetch(url)))
    elif option.lower()==("view"):
        print(fetch(url))
    time.sleep(2)
