import subprocess
required_modules = [
    'module1',
    'module2',
    'module3',
]
for module in required_modules:
    try:
        subprocess.check_call(['pip', 'install', module])
        print(f"Successfully installed {module}")
    except subprocess.CalledProcessError:
        print(f"Failed to install {module}")

print("All required modules have been installed.")
