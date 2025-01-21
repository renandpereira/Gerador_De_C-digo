

html <!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Automação de Logística para Rebipagem de Carga</title>
</head>
<body>
  <h1>Automação de Logística para Rebipagem de Carga</h1>
  <p>Este projeto de automação tem como objetivo otimizar o processo de rebipagem de carga, gerando códigos de barras diretamente a partir de uma planilha Excel. Com isso, é possível realizar a bipagem da carga dentro do caminhão, sem a necessidade de retirar toda a carga para a conferência. Os códigos de barras gerados são organizados para impressão eficiente, aproveitando o máximo de espaço disponível na folha de papel.</p>

  <h2>Funcionalidades</h2>

  <h3>📋 Leitura de Planilhas Excel</h3>
  <p>O sistema permite que você insira uma planilha Excel com os códigos necessários para a rebipagem.</p>

  <h3>📦 Geração Automática de Códigos de Barras</h3>
  <p>A partir dos dados fornecidos na planilha, o programa gera os códigos de barras correspondentes.</p>

  <h3>📄 Conversão para PDF</h3>
  <p>Os códigos de barras gerados são organizados em um arquivo PDF pronto para impressão.</p>

  <h3>🖨️ Otimização na Impressão</h3>
  <p>A impressão é organizada para que o maior número possível de códigos de barras caiba em uma única folha.</p>

  <h3>🚛 Bipagem no Caminhão</h3>
  <p>Após a impressão, a equipe logística pode realizar a bipagem da carga dentro do caminhão, economizando tempo e aumentando a precisão.</p>

  <h2>Tecnologias Utilizadas</h2>
  <ul>
    <li><strong>Python 3.x</strong>: Linguagem principal utilizada no desenvolvimento.</li>
    <li><strong>Pandas</strong>: Para manipulação de dados e leitura da planilha Excel.</li>
    <li><strong>openpyxl</strong>: Para trabalhar com arquivos Excel (.xlsx).</li>
    <li><strong>reportlab</strong>: Para criação e formatação de PDFs com os códigos de barras.</li>
    <li><strong>python-barcode</strong>: Para gerar os códigos de barras em diversos formatos.</li>
  </ul>

  <h2>Como Usar</h2>

  <h3>Pré-requisitos</h3>
  <p>Antes de rodar o programa, você precisará ter o <strong>Python 3.x</strong> instalado no seu ambiente, além das bibliotecas necessárias. Você pode instalar as dependências usando o <code>pip</code>:</p>

  <pre><code>pip install pandas openpyxl reportlab python-barcode</code></pre>

  <h3>Passo a Passo</h3>

  <h4>1. Prepare a Planilha Excel</h4>
  <p>Crie uma planilha <code>.xlsx</code> contendo os códigos de barras que você deseja gerar. Cada código de barra deve estar em uma célula de uma coluna específica.</p>
  <p>Exemplo de como a planilha pode ser organizada:</p>
  <pre><code>
Código de Barra
1234567890
0987654321
1122334455
  </code></pre>

  <h4>2. Execute o Programa</h4>
  <p>Após instalar as dependências, execute o script Python principal. O programa vai ler a planilha <code>.xlsx</code> que você preparou e gerar os códigos de barras correspondentes. O arquivo gerado será um PDF contendo os códigos de barras formatados para impressão.</p>

  <h4>3. Imprima o PDF</h4>
  <p>O arquivo PDF gerado será otimizado para impressão. Ele estará organizado para garantir o máximo aproveitamento do espaço da folha, imprimindo o maior número possível de códigos de barras.</p>

  <h4>4. Realize a Bipagem</h4>
  <p>Após a impressão, utilize os códigos de barras impressos para realizar a bipagem da carga diretamente dentro do caminhão. Isso facilita o processo de conferência sem a necessidade de retirar toda a carga.</p>

  <h2>Exemplo de Uso</h2>
  <p>Após executar o código, o programa irá gerar um arquivo PDF com os códigos de barras organizados.</p>

  <h3>Arquivos de Exemplo</h3>
  <ul>
    <li><a href="#">Planilha de Exemplo</a></li>
    <li><a href="#">PDF Gerado</a></li>
  </ul>

  <h2>Como Contribuir</h2>
  <p>Contribuições são bem-vindas! Se você encontrou algum problema ou deseja melhorar este projeto, sinta-se à vontade para fazer um <strong>fork</strong> do repositório, realizar suas modificações e enviar um <strong>pull request</strong>.</p>

  <h3>Passos para Contribuir</h3>
  <ol>
    <li>Faça um <strong

