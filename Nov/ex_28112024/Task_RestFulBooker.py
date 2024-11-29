class RestFullBooker:
    name=None
    list_of_apis=[]
    links={}
    def __init__(self,name,list_of_apis,links):
        self.name=name
        self.list_of_apis=list_of_apis
        self.links=links

    """def print_name(self):
        print(self.name)"""

    def print_apis(self):
        print(self.list_of_apis)

    def print_links(self):
        print(self.links)

restfullbooker=RestFullBooker("Name1",["api1","api2","api3"],{"www.link1.com","www.link2.com","www.link3.com"})
restfullbooker.print_apis()
restfullbooker.print_links()
