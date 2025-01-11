from pathlib import Path
from sqlalchemy import create_engine, String, Boolean, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

#para criptografia da senha
from werkzeug.security import generate_password_hash, check_password_hash

pasta_atual = Path(__file__).parent
PATH_TO_BD = Path.joinpath(pasta_atual,'bd_usuarios.sqlite')

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))
    senha: Mapped[str] = mapped_column(String(128))
    email: Mapped[str] = mapped_column(String(30))
    acesso_gestor: Mapped[str] = mapped_column(Boolean(), default=False)

    def __repr__(self):
        return f"Usuario({self.id=}, {self.nome=})"
    
    def define_senha(self, senha):        
        self.senha = generate_password_hash(senha)
    
    def verifica_senha(self, senha):
        return check_password_hash(self.senha, senha)

engine = create_engine(f'sqlite:///{PATH_TO_BD}')
Base.metadata.create_all(bind=engine)

## CRUD ##########################
def cria_usuarios(
        nome,
        senha, 
        email,
        **kwargs
        #acesso_gestor=False
):
    #with cria uma instância isolada da Session; uma vez encerrado, a Session é fechada
    with Session(bind=engine) as session:
        usuario = Usuario(
            nome=nome,
            #senha=senha, ##a senha agora vai ser criptografada
            email=email,
            **kwargs #Permite usar o valor default False quando não se adicionar acesso_gestor
            #acesso_gestor=acesso_gestor
        )

        usuario.define_senha(senha)
        session.add(usuario)
        session.commit()

def leitura_todos_usuarios():
    with Session(bind=engine) as session:
        comando_sql = select(Usuario)
        usuarios = session.execute(comando_sql).fetchall()
        return [user[0] for user in usuarios]

def leitura_usuario_por_id(idx):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=idx)
        usuario = session.execute(comando_sql).fetchone() #session.execute(comando_sql).fetchall()
        return usuario[0] #tem que ser assim pq retorna uma tupla (pegar primeira posição)

def modificar_usuario(
        id, 
        nome=None, 
        senha=None, 
        email=None, 
        acesso_gestor=None):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuario = session.execute(comando_sql).fetchone()[0] #tem que ser assim pq retorna uma tupla (pegar primeira posição)
        
        if nome:
            usuario.nome = nome
        if senha:
            usuario.senha = senha
        if email:
            usuario.email = email
        if not acesso_gestor is None: ##pq acesso_gestor é inserido como kwarg
            usuario.acesso_gestor = acesso_gestor
        
        session.commit()

def modificar_usuario_2(
        id,
        **kwargs):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuario = session.execute(comando_sql).fetchone()[0]
        print(kwargs.items())

        for value in kwargs.items():
            print("value: ", value)
            if value[0] == 'nome':
                usuario.nome = value[1]
            if value[0] == 'senha':
                usuario.senha = value[1]
            if value[0] == 'email':
                usuario.email = value[1]
            if value[0] == 'acesso_gestor': ##pq acesso_gestor é inserido como kwarg
                usuario.acesso_gestor = value[1]
        
        session.commit()

def modificar_usuario_3(
        id,
        **kwargs):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuario = session.execute(comando_sql).fetchone()[0]
        

        for key,value in kwargs.items():
            #setattr consegue encaixar as alterações para cada key de 'usuario'
            setattr(usuario, key, value)
                             
        session.commit()

def modificar_usuario_senha_cripto(
        id,
        **kwargs):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuario = session.execute(comando_sql).fetchone()[0]
        
        for key,value in kwargs.items():
            if key == 'senha':
                usuario.define_senha(value)
            else:
                setattr(usuario, key, value)
                             
        session.commit()
    

def deletar_usuario(id):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuario = session.execute(comando_sql).fetchone()[0]
        
        session.delete(usuario)
        
        session.commit()



if __name__ == '__main__':
    
    '''
    cria_usuarios(
        'Tester da Silva',
        senha='123456',
        email='teste@teste.com',
        acesso_gestor = True
    )
    '''
    
    
    '''
    usuarios = leitura_todos_usuarios()
    usuario_0 = usuarios[0]
    print(usuario_0.nome, usuario_0.senha, usuario_0.email, usuario_0.acesso_gestor)
    '''

    '''
    usuario_alex = leitura_usuario_por_id(1)
    print(usuario_alex.nome, usuario_alex.senha, usuario_alex.email, usuario_alex.acesso_gestor)
    '''

    #print('Modifica usuário')
        
    #modificar_usuario_2(id=5, email='teste_alt_4@gmail.com', senha='09543210')

    #modificar_usuario_3(id=5, email='teste_alt_eita@gmail.com', senha='111222333')
    #deletar_usuario(1)

    #modificar_usuario_senha_cripto(id=5, email='teste_alt_eita@gmail.com', senha='111222333')

    #usuario = leitura_usuario_por_id(idx=5)

    #print(usuario.verifica_senha('111222333')) ##Retorna True ou False se a senha não bater

