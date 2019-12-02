import re

coincidencias_num = re.split(
    '(:\s*)|(\=\s*)',
    str(
        "'121223'='R4'"
    )
)


print(coincidencias_num)
