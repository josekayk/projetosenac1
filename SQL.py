import sqlite3

class ItenEstoque:
  def __init__(self, nome, marca, preco, modelo, quantidade, ):
      self.nome = nome
      self.marca = preco
      self.modelo = modelo
      self.quantidade = quantidade

  def exibir_informacoes(self):
    print(f"Nome: {self.nome}, Marca: {self.marca}, Preço: {self.preco}, Modelo: {self.modelo}, Quantidade: {self.quantidade}")

class Estoque:
  def _init_(self, db_name = 'estoque.db'):
    self.conn = sqlite3.connect(db_name)
    self.criar_tabela()

  def criar_tabela(self):
    with self.conn:
      self.conn.execute("""
        CREATE TABLE IF NOT EXISTS itens (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          nome TEXT NOT NULL,
          marca TEXT NOT NULL,
          preco REL
          modelo TEXT,
          quantidade INTEGER
        )
      """)

  def adicionar_iten(self, iten):
    with self.conn:
      self.conn.execute("""
          INSERT INTO itens (nome, marca, modelo, preco, quantidade)
          VALUES (?, ?, ?, ?, ?)""", (iten.nome, iten.modelo, iten.preco, iten.quantidade))
      print("Item adicionar ao estoque com sucesso")

  def remover_item(self, nome_item):
    with self.conn:
      cursor = self.conn.execute("DELETE FROM itens WHERE nome = ?"(nome_item,))
    if cursor.rowcount > 0:
      print("Item removido com sucesso!")
    else:
        print("Item não encontrado no estoque.")
