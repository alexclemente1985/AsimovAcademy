from pathlib import Path
from sqlalchemy import create_engine, String, Boolean, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

pasta_atual = Path(__file__).parent
PATH_TO_BD = Path.joinpath(pasta_atual,'bd_usuarios.sqlite')

class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))
    senha: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    acesso_gestor: Mapped[str] = mapped_column(Boolean(), default=False)

    def __repr__(self):
        return f"Usuario({self.id=}, {self.nome=})"

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
            senha=senha,
            email=email,
            **kwargs #Permite usar o valor default False quando não se adicionar acesso_gestor
            #acesso_gestor=acesso_gestor
        )

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
        usuario = session.execute(comando_sql).fetchall()
        return usuario[0][0] #tem que ser assim pq retorna uma tupla (pegar primeira posição)

def modificar_usuario(id, nome=None, senha=None, email=None, acesso_gestor=None):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuario = session.execute(comando_sql).fetchone()[0] #tem que ser assim pq retorna uma tupla (pegar primeira posição)
        usuario[0]

if __name__ == '__main__':
    '''
    cria_usuarios(
        'Priscilla Souza de Sá',
        senha='123456',
        email='teste@teste.com',
        acesso_gestor = True
    )
    '''

    #print(leitura_todos_usuarios())

    '''
    usuarios = leitura_todos_usuarios()
    usuario_0 = usuarios[0]
    print(usuario_0.nome, usuario_0.senha, usuario_0.email, usuario_0.acesso_gestor)
    '''


    print('########')
    print('')

    usuario_alex = leitura_usuario_por_id(1)
    print(usuario_alex.nome, usuario_alex.senha, usuario_alex.email, usuario_alex.acesso_gestor)
