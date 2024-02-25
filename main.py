class HomeAutomation:
    def __init__(self):
        self.devices = {
            "lights" : {"state": "off" },
            "thermostat": {"temperature": 70},
            "security_system": {"armed": False}
        }


    def toggle_lights(self):
        if self.devices['lights']['state'] == "off":
            self.devices['lights']['state'] = "on"
            print("lights turned on")
        else:
            self.devices['lights']['state'] = "off"
            print("lights turned off")


    def adjust_temperature(self, temperature):
        self.devices['thermostat']['temperature'] = temperature
        print(f"temperature set to {temperature} degrees")

    
    def toggle_security_system(self):
        if self.devices['security_system']['armed']:
            self.devices['security_system']['armed'] = False
            print("security system disarmed")
        else:
            self.devices['security_system']['armed'] = True
            print("security system armed")



    def show_status(self):
        print("current status: ")
        for device, status in self.devices.items():
            print(f"{device}: {status}")


def main():
    home = HomeAutomation()
    print("welcome to home Automation App")

    while True:
        print("\nwhat would you like to do")
        print("1. toggle lights")
        print("2. adjust thermostat temperature")
        print("3. toggle security system")
        print("4. show current status")
        print("5. exit ")


        choice = input("enter your choice (1-5): ")

        if choice == "1":
            home.toggle_lights()
        elif choice == "2":
            temperature = int(input("enter youe desired temperature: "))
            home.adjust_temperature(temperature)
        elif choice == "3":
            home.toggle_security_system()
        elif choice == "4":
            home.show_status()
        elif choice == "5":
            print("existing the home automation app. GoodBye")
            break
        else:
            print("invalid choice. please enter a number between 1 and 5. ")


if __name__ =="__main__":
    main() 