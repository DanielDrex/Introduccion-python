# Inciar proyecto de git
git init

# Prepara archivos que se convertiran en commit
git add .

## el punto es para agregar todos los archivos modificados

# Crear commit con su mensaje
git commit -m "Mensaje del commit"

# Agregar remoto Solo la primera vez
git remote add origin 'url'

# Enviar commits al servidor de Github
git push -u origin (branch)

# Creacion de nueva branch y  movernos a ella
git checkout -b (nombrenuevo)

# Mostrar los branch
git branch

# mezclar cambios entre branch
git merge (branch que quiero fusionar los cambios)

# Mostrar los cambios entre branch
git diff (branch1) (branch2)

# Ejemplo