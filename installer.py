import os


def pause():
	print("")
	os.system("pause")
	print("")


with open("installer_resources/console_logo.txt", "r") as f:
	print(f.read())

print("Mr. Worldwide, a tool by AnonymousHacker1279 to automatically generate language files for Minecraft by using a translation API.")
print("Project Page: https://github.com/AnonymousHacker1279/MrWorldwide")
print("\nThis installer will setup Mr. Worldwide on your system.")

pause()

print("All assets (excluding the API itself), are licensed under the MIT license. You may find a summary here: https://github.com/AnonymousHacker1279/MrWorldwide/blob/master/LICENSE")
print("By continuing with the installation, you agree to the terms of the license.")

pause()

default_path = os.getenv("LOCALAPPDATA")
install_path = input("Where should this be installed? (If you don't specify, it'll automatically go to [" + default_path + "]): ")
if install_path == "":
	install_path = default_path

api_location = "Local"
while True:
	should_download_api = input("Should I download the LibreTranslate API locally? (Recommended, Y/N): ")

	if should_download_api.lower() == "y":
		should_download_api = True
		break
	elif should_download_api.lower() == "n":
		should_download_api = False
		break
	else:
		print("Please only enter Y/N.")

if should_download_api is False:
	api_location = input("Where can I access the LibreTranslate API? (Provide a URL, can be changed later): ")

print("===========================================================================================================================================\n")
print("Review the installation options below. If something isn't right, restart the script.\n")

print("Install Path: " + install_path)
print("Downloading the LibreTranslate API Locally: " + str(should_download_api))
print("LibreTranslate API Location: " + api_location)

pause()

# TODO: Here is where everything actually gets installed. Will need to clone the program resources, and the API if necessary.
# Configurations will also have to be built.
