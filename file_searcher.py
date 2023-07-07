import os
import time
#watch dog is the module that sees for file changes made during whe the program is running . if there is it stores them in the list
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#this stores all the files in the list
def build_cache(root_dir):
    cache = []
    for root, dirs, files in os.walk(root_dir):
        # Add files
        cache.extend([os.path.join(root, file) for file in files])
        # Add directories
        cache.extend([os.path.join(root, directory) for directory in dirs])
    return cache

def search_cache(query, cache):
    matches = []
    for item in cache:
        last_backslash_index = item.rfind("\\")
        #reduces the string you entered into a lowercase string
        if last_backslash_index != -1 and query.lower() in item[last_backslash_index + 1:].lower():
            matches.append(item)
    return matches

class MyHandler(FileSystemEventHandler):
    def __init__(self, cache):
        self.cache = cache

    def on_created(self, event):
        if not event.is_directory:
            self.cache.append(event.src_path)

#for now we are searching the full c directory . if you want you can also search only some specific parts of your root system
root_directory = 'C:\\'

# Build the initial cache
cache = build_cache(root_directory)

# Create an observer and event handler
event_handler = MyHandler(cache)
observer = Observer()
observer.schedule(event_handler, root_directory, recursive=True)
observer.start()

try:
    while True:
        search_query = input("Enter a search query (or 'quit' to exit): ")

        if search_query.lower() == 'quit':
            break

        results = search_cache(search_query, cache)

        if results:
            print(f"Found {len(results)} matches:")
            for result in results:
                print(result)

            print(f"Total number of results: {len(results)}")
        else:
            print("No matches found.")

except KeyboardInterrupt:
    observer.stop()

observer.join()

