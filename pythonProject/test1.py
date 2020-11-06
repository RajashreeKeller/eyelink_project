# moving one files to another
import shutil

source = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\images\pic2.png"
destination = r"C:\Users\rajashreesa\PycharmProjects\pythonProject\venv\test"

new_path = shutil.copy(source, destination)

print(new_path)



