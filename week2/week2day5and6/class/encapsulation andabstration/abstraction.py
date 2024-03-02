from abc import ABC, abstractmethod
class BankingApp(ABC):
    def database(self):
        print(f"Connected to database successfully.")
    @abstractmethod
    def security(self):
        pass
class MobileApp(BankingApp):
    def login_app(self):
        print("login to Mobile App successfully")
    def security(self):
        print("security of mobile app")

if __name__=="__main__":
    mobile_app=MobileApp()
    print(mobile_app)