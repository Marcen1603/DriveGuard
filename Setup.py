import os

def print_device_information():
    print()


def create_setup():
    print("Creating setup ...")
    os.system(r".\venv\Scripts\activate && pip freeze > requirements.txt")
    print("Finished!")
    
def load_setup():
    print("Loading setup ...")
    os.system(r".\venv\Scripts\activate && pip isntall requirements.txt")
    print("Finished!")


if __name__ == "__main__":
    
    should_create_setup = True
    should_load_setup = False
    should_print_device_information = False
    
    if should_print_device_information:
        print_device_information()
    if should_create_setup:
        create_setup()
    if should_load_setup:
        load_setup()