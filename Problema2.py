def killer(suspect_info, dead):
    # Itera sobre cada suspeito e a lista de pessoas que ele viu
    for suspect, seenpeople in suspect_info.items():
        # Checa se todas as pessoas mortas estão na lista de pessoas que o suspeito viu
        if all(person in seenpeople for person in dead):
            return suspect  # Retorna o nome do suspeito se ele viu todas as pessoas mortas
        pass  # Pass é desnecessário aqui e pode ser removido

# Dicionário contendo suspeitos e as pessoas que eles foram vistos com
suspect_info = {'James': ['Jacob', 'Bill', 'Lucas'],
                'Johnny': ['David', 'Kyle', 'Lucas'],
                'Peter': ['Lucy', 'Kyle']}
    
# Lista de pessoas que foram mortas
dead = ['Lucas', 'Bill']
    
# Chamada da função killer para identificar o suspeito com base nas informações fornecidas
suspect = killer(suspect_info, dead)
    
# Verifica se um suspeito foi identificado e imprime o resultado
if suspect:
    print(f"The suspect is {suspect}")  # Imprime o nome do suspeito identificado
else:
    print("No suspect found.")  # Imprime que nenhum suspeito foi encontrado se não houver correspondência
