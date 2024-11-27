import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

class NetworkProfileManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Profile Manager")
        self.interface_var = tk.StringVar()
        self.ip_var = tk.StringVar()
        self.subnet_var = tk.StringVar()
        self.gateway_var = tk.StringVar()
        self.dns_var = tk.StringVar()
        self.profiles = {}

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Select Interface:").grid(column=0, row=0, padx=10, pady=5)
        self.interface_entry = ttk.Entry(self.root, textvariable=self.interface_var)
        self.interface_entry.grid(column=1, row=0, padx=10, pady=5)

        ttk.Label(self.root, text="IP Address:").grid(column=0, row=1, padx=10, pady=5)
        self.ip_entry = ttk.Entry(self.root, textvariable=self.ip_var)
        self.ip_entry.grid(column=1, row=1, padx=10, pady=5)

        ttk.Label(self.root, text="Subnet Mask:").grid(column=0, row=2, padx=10, pady=5)
        self.subnet_entry = ttk.Entry(self.root, textvariable=self.subnet_var)
        self.subnet_entry.grid(column=1, row=2, padx=10, pady=5)

        ttk.Label(self.root, text="Default Gateway:").grid(column=0, row=3, padx=10, pady=5)
        self.gateway_entry = ttk.Entry(self.root, textvariable=self.gateway_var)
        self.gateway_entry.grid(column=1, row=3, padx=10, pady=5)

        ttk.Label(self.root, text="DNS Server:").grid(column=0, row=4, padx=10, pady=5)
        self.dns_entry = ttk.Entry(self.root, textvariable=self.dns_var)
        self.dns_entry.grid(column=1, row=4, padx=10, pady=5)

        self.save_button = ttk.Button(self.root, text="Save Profile", command=self.save_profile)
        self.save_button.grid(column=0, row=5, padx=10, pady=10)

        self.apply_button = ttk.Button(self.root, text="Apply Profile", command=self.apply_profile)
        self.apply_button.grid(column=1, row=5, padx=10, pady=10)

    def save_profile(self):
        profile_name = self.interface_var.get()
        if profile_name:
            self.profiles[profile_name] = {
                "ip": self.ip_var.get(),
                "subnet": self.subnet_var.get(),
                "gateway": self.gateway_var.get(),
                "dns": self.dns_var.get()
            }
            messagebox.showinfo("Success", f"Profile '{profile_name}' saved successfully!")
        else:
            messagebox.showerror("Error", "Please enter a profile name.")

    def apply_profile(self):
        profile_name = self.interface_var.get()
        if profile_name in self.profiles:
            profile = self.profiles[profile_name]
            self.set_ip_settings(profile)
            messagebox.showinfo("Success", f"Profile '{profile_name}' applied successfully!")
        else:
            messagebox.showerror("Error", "Profile not found.")

    def set_ip_settings(self, profile):
        interface = self.interface_var.get()
        ip = profile["ip"]
        subnet = profile["subnet"]
        gateway = profile["gateway"]
        dns = profile["dns"]

        subprocess.run(["netsh", "interface", "ip", "set", "address", interface, "static", ip, subnet, gateway])
        subprocess.run(["netsh", "interface", "ip", "set", "dns", interface, "static", dns])

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkProfileManager(root)
    root.mainloop()