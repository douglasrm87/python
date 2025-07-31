from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Lista de produtos com informações de promoção e preços
    # Exemplo de produtos
    # Cada produto é um dicionário com nome, preço e se está em promoção
    # A lista pode ser substituída por dados de um banco de dados ou outra fonte de dados
    # Aqui, estamos usando uma lista estática para fins de demonstração
    # Os produtos são passados para o template Jinja2 para renderização
    # A renderização do template Jinja2 é feita com a função render_template do Flask, que procura o arquivo index.html na pasta templates e renderiza o conteúdo com os dados fornecidos
    # A variável produtos contém uma lista de dicionários, onde cada dicionário representa um produto com nome, preço e status de promoção
    # O template Jinja2 pode usar essa lista para exibir os produtos de forma dinâmica, permitindo que o usuário veja os produtos disponíveis e suas informações de promoção e preço
    # O template pode usar estruturas de controle Jinja2, como loops e condicionais, para exibir os produtos de maneira organizada e estilizada
    produtos = [
        {"nome": "Arroz", "preco": 25.50, "promocao": False},
        {"nome": "Feijão", "preco": 10.00, "promocao": True},
        {"nome": "Azeite", "preco": 30.00, "promocao": False},
        {"nome": "Macarrão", "preco": 5.50, "promocao": True},
    ]
    return render_template("index.html", produtos=produtos)

if __name__ == "__main__":
    app.run(debug=True)
