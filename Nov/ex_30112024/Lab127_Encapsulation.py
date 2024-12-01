class car:
    def __init__(self,name,model,make):
        self.Name=name
        self.Model=model
        self.Make=make


    def start_engine(self):
        print("Name of car:"+self.Name)
        print("Model number:"+self.Model)
        print("make:"+self.Make)
        print("\n")


lambo=car("Lamborgini","2023","V6")
lambo.start_engine()


mg_hector=car("Mg_Hector","2024","1.5Turbo+")
mg_hector.start_engine()


