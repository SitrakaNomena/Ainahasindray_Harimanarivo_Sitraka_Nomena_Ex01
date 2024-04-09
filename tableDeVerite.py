from itertools import product

def evaluate_expression(expression, inputs):
    # Cette fonction évalue une expression booléenne donnée avec des valeurs d'entrée données
    code = compile(expression, '<string>', 'eval')
    return eval(code, {'__builtins__': None}, inputs)

def truth_table(expression, variables):
    # Cette fonction génère la table de vérité pour une expression booléenne donnée
    table = []
    
    for values in product([0, 1], repeat=len(variables)):
        inputs = dict(zip(variables, values))
        result = evaluate_expression(expression, inputs)
        table.append((values, result))
    return table

def first_canonical_form(table):
    # Cette fonction génère la première forme canonique
    terms = []
    for inputs, result in table:
        if result:
            term = ' AND '.join([f'{var}' if val else f'NOT {var}' for var, val in zip(variables, inputs)])
            terms.append(term)
    return ' OR '.join(terms)

def second_canonical_form(table):
    # Cette fonction génère la deuxième forme canonique
    terms = []
    for inputs, result in table:
        if not result:
            term = ' OR '.join([f'{var}' if val else f'NOT {var}' for var, val in zip(variables, inputs)])
            terms.append(term)
    return ' AND '.join(terms)


variables = input("Entrez les noms des variables séparées par des espaces: ").split()
expression = input("Entrez l'expression logique (utilisez les opérateurs and, or, not et des parentheses): ")

table = truth_table(expression, variables)

print("\nTable de vérité:")
print("---------------")
print(" | ".join(variables + ['Résultat']))
print("-----------------------------")
for inputs, result in table:
    print(" | ".join(map(str, inputs + (result,))))

print("\nPremière forme canonique:")
print(first_canonical_form(table))

print("\nDeuxième forme canonique:")
print(second_canonical_form(table))
