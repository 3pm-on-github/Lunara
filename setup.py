import os
print("Welcome to the Lunara Setup Program!")
print("To setup Lunara, you will first need to fill some settings.")
st1 = input("Do you want to run only .ln files? (Y/N)\n>>> ")
if st1 != "Y" and st1 != "N":
    print(f"Error: '{st1}' is an invalid response.")
    exit()
print("Creating settings.lnst file...")
if os.path.exists("settings.lnst"):
    print("settings.lnst file already exists, re-using it...")
with open("settings.lnst", "w") as f:
    f.write("RunOnlyLNFiles: " + st1.upper())
    f.close()
print("Done!")
print("You can now use Lunara!")