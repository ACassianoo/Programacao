class Aluno:
    def __init__(self, nome, sobrenome, curso, endereco, filiacao, emailResponsavel, RA, segmento, turma, nomeUsuario, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.curso = curso
        self.endereco = endereco
        self.filiacao = filiacao
        self.emailResponsavel = emailResponsavel
        self.RA = RA
        self.segmento = segmento
        self.turma = turma
        self.nomeUsuario = nomeUsuario
        self.email = email
        self.senha = senha

    # Propriedade para 'nome'
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("Nome não pode ser vazio")
        self._nome = valor

    # Propriedade para 'RA'
    @property
    def RA(self):
        return self._RA

    @RA.setter
    def RA(self, valor):
        if not valor:
            raise ValueError("RA não pode ser vazio")
        self._RA = valor

    # Propriedade para 'segmento'
    @property
    def segmento(self):
        return self._segmento

    @segmento.setter
    def segmento(self, valor):
        if valor not in ['EM', 'Superior']:
            raise ValueError("Segmento deve ser 'EM' ou 'Superior'")
        self._segmento = valor


class Professor:
    def __init__(self, nome, sobrenome, cpf, endereco, formacao, disciplinas, segmento, turmas, nomeUsuario, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.endereco = endereco
        self.formacao = formacao
        self.disciplinas = disciplinas
        self.segmento = segmento
        self.turmas = turmas
        self.nomeUsuario = nomeUsuario
        self.email = email
        self.senha = senha

    # Propriedade para 'nome'
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("Nome não pode ser vazio")
        self._nome = valor

    # Propriedade para 'cpf'
    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        if not valor.isdigit():
            raise ValueError("CPF deve conter apenas números")
        self._cpf = valor

    # Propriedade para 'segmento'
    @property
    def segmento(self):
        return self._segmento

    @segmento.setter
    def segmento(self, valor):
        if valor not in ['EM', 'Superior']:
            raise ValueError("Segmento deve ser 'EM' ou 'Superior'")
        self._segmento = valor


class Turma:
    def __init__(self, nome, segmento, ano, alunos=None, professores=None, disciplinas=None):
        if alunos is None:
            alunos = []
        if professores is None:
            professores = []
        if disciplinas is None:
            disciplinas = []

        self.nome = nome
        self.segmento = segmento
        self.ano = ano
        self.alunos = alunos
        self.professores = professores
        self.disciplinas = disciplinas

        # Validação para turmas de EM (Ensino Médio)
        if self.segmento == 'EM' and len(self.alunos) < 20:
            raise ValueError("Uma turma de EM deve ter pelo menos 20 alunos")

    # Método para adicionar aluno
    def adicionar_aluno(self, aluno):
        if self.segmento == 'EM' and len(self.alunos) >= 20:
            raise ValueError("Número máximo de alunos atingido para esta turma de EM.")
        if len(self.alunos) >= 5:  # Para o Ensino Superior (mínimo 5 alunos)
            raise ValueError("Número máximo de alunos atingido para esta turma de Ensino Superior.")
        self.alunos.append(aluno)

    # Método para adicionar professor
    def adicionar_professor(self, professor):
        self.professores.append(professor)

    # Método para adicionar disciplina
    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError("Nome da turma não pode ser vazio")
        self._nome = valor

    @property
    def alunos(self):
        return self._alunos

    @alunos.setter
    def alunos(self, valor):
        if not isinstance(valor, list):
            raise ValueError("Alunos deve ser uma lista")
        self._alunos = valor

    @property
    def professores(self):
        return self._professores

    @professores.setter
    def professores(self, valor):
        if not isinstance(valor, list):
            raise ValueError("Professores deve ser uma lista")
        self._professores = valor

    @property
    def disciplinas(self):
        return self._disciplinas

    @disciplinas.setter
    def disciplinas(self, valor):
        if not isinstance(valor, list):
            raise ValueError("Disciplinas deve ser uma lista")
        self._disciplinas = valor


class Disciplina:
    def __init__(self, id_disciplina, descricao, segmento, professor_titular):
        self.id_disciplina = id_disciplina
        self.descricao = descricao
        self.segmento = segmento
        self.professor_titular = professor_titular

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, valor):
        if not valor:
            raise ValueError("Descrição da disciplina não pode ser vazia")
        self._descricao = valor

    @property
    def segmento(self):
        return self._segmento

    @segmento.setter
    def segmento(self, valor):
        if valor not in ['EM', 'Superior']:
            raise ValueError("Segmento deve ser 'EM' ou 'Superior'")
        self._segmento = valor



# link para o diagrama:
# https://lucid.app/lucidchart/2001c0f1-3268-4115-8ae8-d727fcbdde20/edit?viewport_loc=-2274%2C-730%2C3328%2C1562%2C0_0&invitationId=inv_3236f30d-278f-4be5-8266-4ea4a27391cd