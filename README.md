# Controle de Visitantes - Django Web App

## Descrição do Projeto

Este projeto é uma aplicação web desenvolvida em Python com o framework Django, utilizando HTML e CSS para a interface. A finalidade principal da aplicação é facilitar o controle de visitantes em um ambiente, permitindo que o porteiro realize o cadastro de visitantes, bem como atualize o status do cartão do visitante. Os status disponíveis são: "Aguardando Autorização", "Em Visita" e "Finalizado".

- Link do projeto na vercel: 

## Funcionalidades

- **Cadastro de Visitantes**: O porteiro pode cadastrar novos visitantes, incluindo informações como nome, cpf, data e horário de chegada, entre outras informações relevantes.

- **Atualização de Status**: O porteiro pode atualizar o status do cartão do visitante para refletir a situação atual da visita. Os status disponíveis são:
  - **Aguardando Autorização**: Quando o visitante ainda não foi autorizado a entrar.
  - **Em Visita**: Quando o visitante está atualmente nas instalações.
  - **Finalizado**: Quando a visita foi concluída.

- **Interface Intuitiva**: A interface foi projetada para ser fácil de usar, proporcionando uma experiência amigável para o porteiro.

## Pré-requisitos

- Python 3.12.1
- Django (instalável via `pip install django`)

## Instalação e Execução

1. Clone o repositório: `git clone https://github.com/Jleandrobr/Controle_visitantes`
2. Navegue até o diretório do projeto: `cd controle_visitantes`
3. Entre no ambiente virtual desejado: `workon (ambiente virtual criado)`
4. Execute as migrações do banco de dados: `python manage.py migrate`
5. Crie um superusuário para acessar o painel de administração: `python manage.py createsuperuser`
6. Inicie o servidor: `python manage.py runserver`
7. Acesse a aplicação no navegador: `http://localhost:8000/`

---
