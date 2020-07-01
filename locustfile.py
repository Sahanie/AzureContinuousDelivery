from locust import HttpLocust, TaskSet, task
import json
class UserBehavior(TaskSet):
    def __init__(self, parent):
        super(UserBehavior, self).__init__(parent)
    def on_start(self):
        """ on_start is called when a Locust start before 
            any task is scheduled
        """
        self.predict()
    
    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass
    
    @task(2)    
    def predict(self):
        self.client.post("/predict",
                         {  
                            "CHAS":{  
                                "0":0
                            },
                            "RM":{  
                                "0":6.575
                            },
                            "TAX":{  
                                "0":296.0
                            },
                            "PTRATIO":{  
                                "0":15.3
                            },
                            "B":{  
                                "0":396.9
                            },
                            "LSTAT":{  
                                "0":4.98
                            }
                        })
    @task(1)
    def index(self):
        self.client.get("/")
        
    @task(3)
    def results(self):
        self.client.get("/predict")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
