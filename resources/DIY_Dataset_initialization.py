
import numpy as np
import os, shutil
from IPython.display import clear_output

class DIY_Dataset: 
    
    def __init__(self, setup): 
        
        self.name = ""
        self.path = ""
        self.root = setup.path
        
        new_name = ""
        while (new_name == ""): 
            
            clear_output(wait=True)
            all_dataset = [f.name for f in os.scandir(f"{self.root}/datasets" ) if f.is_dir()  and f.name != '__pycache__' and f.name != '.ipynb_checkpoints']
            print (f"Current datasets: {all_dataset}")
            
            n = input("Input a name for the copy of Oxford 17 flowers dataset. ")
            for i in range(len(n)): 
                if ((n[i] >= '0' and n[i] <= '9') or (n[i] >= 'a' and n[i] <= 'z') or (n[i] >= 'A' and n[i] <= 'Z') or (n[i] == '_')):
                    new_name += n[i]
            if (new_name == ""): continue
            all_dataset = [f.name for f in os.scandir(f"{self.root}/datasets") if f.is_dir()]
            # print(all_dataset)
            
            if (new_name in all_dataset): 
                print (f"The dataset {new_name} already exists. ")
                new_name = ""
                input ("(enter anything to give another name)")
            else: 
                confirm = ""
                print (f"Preferred name of the copy: {new_name}. ")
                confirm = input(f"Press Enter to confirm. Enter anything to discard.")
                if (confirm != ""): new_name = ""
                
        new_path = self.root + f"/datasets/{new_name}"
        print (f"The new dataset {new_name} is created. ")
        print (f"Dataset path: {new_path}")
        self.name = new_name
        self.path = new_path

        if (os.path.exists(self.path)): shutil.rmtree(self.path, ignore_errors=True)
        if (os.path.exists(self.path + "/train")): shutil.rmtree(self.path + "/train", ignore_errors=True)
        if (os.path.exists(self.path + "/val")): shutil.rmtree(self.path + "/val", ignore_errors=True)
        if (os.path.exists(self.path + "/test")): shutil.rmtree(self.path + "/test", ignore_errors=True)

        clear_output(wait=True)
        num_classes, train, val, test, dataset_ratio = self.diy_configure()
        
        clear_output(wait=True)
        # print (f"Generating {self.name} dataset ... (folder structure)")
        os.makedirs(self.path + "/train", exist_ok = True)
        os.makedirs(self.path + "/val", exist_ok = True)
        os.makedirs(self.path + "/test", exist_ok = True)
        
        for i in range(num_classes):
            class_name = "class_" + str(i + 1)
            os.makedirs(self.path + f"/train/{class_name}", exist_ok=True)
            os.makedirs(self.path + f"/val/{class_name}", exist_ok=True)
            os.makedirs(self.path + f"/test/{class_name}", exist_ok=True)
        
        clear_output(wait=True)
        print (f"Successfully generated the {self.name} dataset (empty folder structure). ")
        print (f"You still need to put images for each class under the train, val and test datasets in {self.path}")

    def diy_configure(self): 
        clear_output(wait=True)
        import resources.setup_dataset as S
        setup = S.setup_dataset(self.name)
        return setup.return_setup()

