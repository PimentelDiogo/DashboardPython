[https://pimenteldiogo.github.io/](https://dashboardpython-vhggn7drsqckyamr6oaikf.streamlit.app/)

Este README fornece instruções completas sobre como configurar e usar o dashboard, incluindo os requisitos de bibliotecas, como executar o aplicativo e quais tipos de visualizações estão disponíveis. As instruções estão em português e inglês para maior acessibilidade.

# Dashboard Suporte WorkSpaceMobile

Um dashboard interativo para visualização de dados de tickets de suporte, construído com Streamlit e Plotly.

## Português

### Requisitos

Para executar este dashboard, você precisará das seguintes bibliotecas Python:

- pandas: Para manipulação e análise de dados
- streamlit: Para criação da interface web interativa
- plotly: Para visualização de dados com gráficos interativos
- openpyxl: Para leitura de arquivos Excel (.xlsx)

### Instalação

```bash
pip install pandas streamlit plotly openpyxl

### Como Executar
1. Clone este repositório
2. Ative o ambiente virtual (se estiver usando):
   - Linux/macOS: source .venv/bin/activate
   - Windows: venv\Scripts\activate
3. Execute o dashboard:
   ```bash
   cd app
   streamlit run app.py
    ```
### Como Usar
1. Carregue um arquivo XLSX usando o botão de upload
2. O dashboard processará automaticamente os dados e exibirá as visualizações
### Requisitos do Arquivo XLSX
O arquivo XLSX deve conter as seguintes colunas:

- "Analista Atual"
- "Cliente Solicitante"
- "Estado"
- "Última Fila"
### Visualizações Disponíveis
O dashboard gera os seguintes tipos de gráficos:

1. Gráfico de Barras :
   
   - Tickets por Analista
   - Tickets por Cliente
   - Tickets por Fila
2. Gráfico de Pizza :
   
   - Distribuição de Tickets por Estado
3. Tabela de Dados :
   
   - Resumo dos dados carregados

   ## English
### Requirements
To run this dashboard, you'll need the following Python libraries:

- pandas: For data manipulation and analysis
- streamlit: For creating interactive web interface
- plotly: For interactive data visualization
- openpyxl: For reading Excel (.xlsx) files
### Installation
```bash
pip install pandas streamlit plotly openpyxl
 ```

### How to Run
1. Clone this repository
2. Activate the virtual environment (if using one):
   - Linux/macOS: source .venv/bin/activate
   - Windows: venv\Scripts\activate
3. Run the dashboard:
   ```bash
   cd app
   streamlit run app.py
    ```
### How to Use
1. Upload an XLSX file using the upload button
2. The dashboard will automatically process the data and display visualizations
### XLSX File Requirements
The XLSX file must contain the following columns:

- "Analista Atual" (Current Analyst)
- "Cliente Solicitante" (Requesting Client)
- "Estado" (Status)
- "Última Fila" (Last Queue)
### Available Visualizations
The dashboard generates the following types of charts:

1. Bar Charts :
   
   - Tickets by Analyst
   - Tickets by Client
   - Tickets by Queue
2. Pie Chart :
   
   - Ticket Distribution by Status
3. Data Table :
   
   - Summary of loaded data
