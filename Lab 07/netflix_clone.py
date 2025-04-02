import time

class Netflix:
    def __init__(self, user_id, name, device_config):
        self.user_id = user_id
        self.name = name
        self.device_config = device_config
        self.max_screens = 5
        self.active_devices = set()
        self.is_premium_active = False
        self.account_frozen = False
        self.freeze_time = None

    def freeze_account(self):
        self.account_frozen = True
        self.freeze_time = time.time()
        print(f"Account {self.user_id} is frozen for 48 hours due to excessive login attempts.")

    def check_unfreeze(self):
        if self.account_frozen and (time.time() - self.freeze_time) >= 48 * 3600:
            self.account_frozen = False
            self.active_devices.clear()
            print(f"Account {self.user_id} is now unfrozen.")

class NetflixLite(Netflix):
    def __init__(self, user_id, name, device_config):
        super().__init__(user_id, name, device_config)  
        
    def login(self, device):
        self.check_unfreeze()
        if self.account_frozen:
            print(f"Login failed: Account {self.user_id} is frozen.")
            return False
        if self.is_premium_active:
            print(f"{self.name} is watching premium content. No other device can log in.")
            return False
        if len(self.active_devices) >= self.max_screens:
            self.freeze_account()
            return False
        if device in self.active_devices:
            print(f"Device {device} is already logged in.")
            return False
        self.active_devices.add(device)
        print(f"Device {device} logged in. Active devices: {len(self.active_devices)}")
        return True

    def start_premium_show(self, device):
        if self.is_premium_active or device not in self.active_devices:
            print("Cannot start premium content.")
            return False
        self.is_premium_active = True
        print(f"{self.name} is watching premium content on {device}.")

    def stop_premium_show(self):
        if self.is_premium_active:
            self.is_premium_active = False
            print(f"{self.name} stopped watching premium content. Premium access is now available again.")

    def watch_normal_content(self, device):
        if self.is_premium_active or device not in self.active_devices:
            print(f"{device} cannot watch normal content right now.")
            return False
        print(f"{device} is watching normal content.")

# Testing the class
user = NetflixLite("user123", "Sachin", "Mobile-Laptop")
user.login("Laptop")
user.start_premium_show("Laptop")
user.stop_premium_show()

print()
for i in range(3):
    user.login(f"Friend{i+1}")
    user.watch_normal_content(f"Friend{i+1}")

print()
user.login("Friend4")
user.login("Friend5")
user.login("Friend6")
user.login("Friend7")
