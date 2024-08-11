""" 1 Utilice el operador de desigualdad en compara_old_new para mostrar que la contraseÑa no son las misma
    2 Asugurar de que la new_passaword coincidad con la repita_new_passaword"""

old_passaword = "hello123"
new_passaword = "goodbye321"
compara_old_new = old_passaword != new_passaword
repita_new_passaword = "goodbye321"
compara_new_passaword = new_passaword == repita_new_passaword

print (f"Is new passaword different from old passaword {compara_old_new}")
print (f"Has new passaword been introduced correctly? {compara_new_passaword}")
