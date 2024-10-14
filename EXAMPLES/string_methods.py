# use this;
file_path = "c:/Projects/alpha/src/utils/pdfstuff.py"
# not this:
file_path = r"c:\Projects\alpha\src\new\tau\utils\pdfstuff.py"




print(f"{file_path = }")
print(f"{file_path.find('/') = }")
print(f"{file_path.rfind('/') = }")


print(f"{len(file_path) = }")

print(f"{file_path.upper() = }")
print(f"{file_path.count('/') = }")
print(f"{file_path.count('p') = }")
print(f"{file_path.lower().count('p') = }")
print(f"{file_path.startswith('Projects') = }")
print(f"{file_path.endswith('.py') = }")
print(f"{file_path.removesuffix('.py') = }")
print(f"{'alpha' in file_path = }")
print(f"{'beta' in file_path = }")
print(f"{file_path.find('alpha') = }")
print(f"{file_path.find('beta') = }")
print(f"{file_path.replace('alpha', 'beta') = }")
parts = file_path.split('/')
print(f"{parts = }")
print(f"{':'.join(parts) = }")
print()

title = "   Why I love Python    "
print(f"title = [{title}]")
print(f"title.strip() = [{title.strip()}]")
print(f"title.lstrip() = [{title.lstrip()}]")
print(f"title.rstrip() = [{title.rstrip()}]")












