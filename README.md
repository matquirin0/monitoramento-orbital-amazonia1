# MONITORAMENTO ORBITAL AMAZONIA 1
## MATRIZ DE REQUISITOS 
| ID    | Requisito          | Descrição                                                            |
|-------|--------------------|----------------------------------------------------------------------|
| RF01  | Extração de Dados  | O sistema deve consumir a API N2YO para obter previsões de passagem. |
| RF02  | Filtro Geográfico  | Os dados devem ser restritos à localização de São José dos Campos.   |
| RF03  | Persistência SQL   | As janelas de passagem devem ser armazenadas em banco PostgreSQL.    |
| RNF01 | Controle de Versão | O código deve ser versionado utilizando Git.                         |
| RNF02 | Documentação       | O projeto deve conter um diagrama Entidade-Relacionamento (ER).      |
## DIAGRAMA ENTIDADE-RELACIONAMENTO
![Diagrama Entidade-Relacionamento](docs/assets/diagramaSatellite.jpeg)