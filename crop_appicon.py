import os, sys

sizes = [20,29,40,58,60,76,80,87,120,152,167,180,1024]

if len(sys.argv) == 2:
    file = str(sys.argv[1])
else:
    print('you need to provide the root icon name!')
    exit()

print(file)

for size in sizes:
    name = f'{file}_{size}x{size}.png'
    print(f'cropping {name}')
    os.system(f'sips -z {size} {size} {file} --out {name}')

