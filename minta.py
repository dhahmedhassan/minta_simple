import os, logging, json
# my_dir = "/home/ahmed/dev/minta/src/data_1_"

class Minta:
    """
    Blueprint for Minta Program
    """
    current_dir = os.getcwd()
    items = []
    def __init__(self):
        print("Program Initiated")
        logging.basicConfig(
            filename="reading.log",
            level=logging.INFO,
            format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
            datefmt="%H:%M:%S",
        )
        logging.info("Program Is running!")

    def read(self):
        for dirpath, dirnames, filenames in os.walk(self.current_dir):
            
            for f in filenames:
                if f.endswith(".dat"):
                    file_dir = os.path.join(dirpath, f)
                    lines = open(file_dir).readlines()
                    self.items.append(f)
                    logging.info(f"{f} was appended to Items list!")
                    self.items.append(lines)
                    logging.info(f"{f} data was appended to Items list!")

                    with open("items.json", "w") as fjson:
                        json.dump(self.items, fjson, indent=2)
        logging.info("Data has been saved in an items.json file!")
    
    def display(self):
        with open("items.json", "r") as f:
            print(f.read())
            # f.read()
    
# Create simple website to display the items json 

test = Minta()
test.read()
test.display()
