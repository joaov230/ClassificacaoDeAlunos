# Classificacao De Alunos (Mini SISU)
 Este repositório é dedicado para um programa para ordenação e classificação de alunos em diferentes cursos baseados na sua nota individual e opção 1 e opção 2 de curso (como um SISU em baixíssima escala). Esta versão foi utilizada como demonstração desta tecnologia para um colégio técnico da minha cidade natal.  
O código é 100% funcional, mas a configuração dos parâmetros ainda é muito manual. Talvez com o tempo eu atualize e automatize essa seleção.  
Fiz este programa em duas tardes. Ele não é muito genérico pois foi feito para resolver um problema específico de uma escola. Caso queira modificá-lo ou incrementá-lo, fique à vontade para clonar o repositório, vou tentar descrever o funcionamento dele abaixo.  
  
**O código suporta suplência de alunos.**

# Para rodar o código
1. Organize sua tabela como a exemplo na pasta `./Programa/Tabelas Principais/DirecionamentoDasOficinasT02.xlsx`;
2. Coloque sua tabela na pasta `./Programa/Tabelas Principais/`;
3. Execute o programa `PythonGUI.exe` na pasta `./Programa/BuildFinal/dist/PythonGUI.exe`;
4. Informe os dados pedidos (nome do arquivo, nome das colunas da tabela, etc). Caso não seja informado os nomes personalizados das colunas, será mantido o padrão, representado pelo placeholder de cada coluna;
5. Clique em "Verificar e rodar programa";
6. Caso apareça algum erro, corrija e clique novamente em rodar programa;
7. Caso tenha rodado com sucesso, verifique a pasta `./Programa/Oficinas/` para os resultados (cada tabela gerada é um curso com os alunos escolhidos para cada curso).

# BuildFinal
Path: `./Programa/BuildFinal/`
Aqui está o código final do programa utilizado.
* `PythonGUI.py` possui o programa em si, com sua interface gráfica, caminhos absolutos das pastas utilizadas, mensagens de sucesso e erro e a chamada da função do script que faz a seleção.
* `script.py` possui o script que realiza a seleção e classificação (chamado no arquivo `pythonGUI.py`)
  
Todo o script é basicamente a preparação dos dados da tabela:
* Em `Run_Script()` acontece a leitura dos dados;
* Depois esses dados são inseridos num array de tuplas;
* Então o array é ordenado através da função `Sort_Tuple()` definida e explicada no topo deste arquivo;
* Por fim, os dataframes que irão gerar os arquivos Excel são montados individualmente.
  
# Oficinas  
Path: `./Programa/Oficinas`  
Aqui está contido os resultados da execução do script. Não há necessidade de alterar os dados dessa pasta, aqui é apenas a saída do programa.  
Dica: Após a execução, copie as pastas para outro local e exclua as já existentes aqui. Facilita a organização.
  
# Tabelas Principais
Path: `./Programa/Tabelas Principais/`  
Aqui é onde serão armazenadas as tabelas que serão usadas para executar o script, coloque aqui dentro a tabela que você irá utilizar. É a entrada do programa.  
Aqui também possui um exemplo de entrada, com os nomes das colunas e informações das mesmas. Esse exemplo deve ser usado como modelo exato para outras execuções.  
**ATENÇÃO: Na tabela exemplo as notas estão ordenadas, mas não precisam estar, o script é preparado para lidar com isso.**
