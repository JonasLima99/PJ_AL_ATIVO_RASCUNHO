import pandas as pd
import unittest

# Simula a função de tratamento de dados que contém a lógica de desduplicação
def contar_alunos_unicos(df_bruto):
    # 1. Filtro de Aluno Ativo
    ativos = ['MATRICULADO', 'TRANCADO']
    df_filtrado = df_bruto[df_bruto['SIT_MATRICULA'].isin(ativos)]

    # Registro da primeira evidência
    df_alunos_unicos = df_filtrado.drop_duplicates(subset=['ALUNO'], keep='first')

    return len(df_alunos_unicos)

class TesteGranularidadeBDD(unittest.TestCase):

    def test_aluno_multiplas_disciplinas_conta_apenas_uma_vez(self):
        """
        Teste BDD para o Cenário 2: Verifica se a desduplicação está correta.
        """
        # Simula: 1 aluno (ID 12345) em 4 disciplinas + 1 aluno único (ID 67890)
        dados = {
            'ALUNO': [12345, 12345, 12345, 12345, 67890],
            'NOME_DISCIPLINA': ['Disc A', 'Disc B', 'Disc C', 'Disc D', 'Disc E'],
            'SIT_MATRICULA': ['MATRICULADO'] * 5  # Todas as 5 linhas são Ativas
        }
        df_teste = pd.DataFrame(dados)

        resultado_contagem = contar_alunos_unicos(df_teste)

        contagem_esperada = 2

        self.assertEqual(resultado_contagem, contagem_esperada, 
                         "O teste de granularidade falhou: A contagem de alunos únicos não está correta.")

if __name__ == '__main__':
    unittest.main()