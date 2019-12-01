import re

coincidencias_num = re.split(
    '=\s+',
    str(
        '1224 = 687'
    )
)

print(coincidencias_num[len(coincidencias_num)-1])
