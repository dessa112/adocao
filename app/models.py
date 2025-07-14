from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Adotante(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do adotante")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    email = models.EmailField(verbose_name="Email")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade do adotante")
    preferencia_idade = models.CharField(max_length=50, verbose_name="Preferência de idade")
    aceita_grupo_irmaos = models.BooleanField(default=False, verbose_name="Aceita grupo de irmãos")
    aceita_necessidades_especiais = models.BooleanField(default=False, verbose_name="Aceita necessidades especiais")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Adotante"
        verbose_name_plural = "Adotantes"

class Adotado(models.Model):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )

    nome = models.CharField(max_length=100, verbose_name="Nome do adotado")
    idade = models.IntegerField(verbose_name="Idade")
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name="Sexo")
    data_nasc = models.DateField(verbose_name="Data de nascimento")
    situacao = models.CharField(max_length=100, verbose_name="Situação atual")
    necessidades_especiais = models.BooleanField(default=False, verbose_name="Possui necessidades especiais")
    
    # NOVO CAMPO
    foto = models.ImageField(upload_to='fotos_adotados/', null=True, blank=True, verbose_name="Foto")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Adotado"
        verbose_name_plural = "Adotados"

class Instituicao(models.Model):
    TIPO_CHOICES = (
        ('Abrigamento', 'Abrigamento'),
        ('Juizado', 'Juizado'),
        ('ONG', 'ONG'),
        ('Outro', 'Outro'),
    )

    nome = models.CharField(max_length=100, verbose_name="Nome da instituição")
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, verbose_name="Tipo de instituição")
    telefone = models.CharField(max_length=15, verbose_name="Telefone")
    endereco = models.CharField(max_length=200, verbose_name="Endereço")
    cidade = models.ForeignKey('Cidade', on_delete=models.CASCADE, verbose_name="Cidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"

class Compatibilidade(models.Model):
    adotante = models.ForeignKey('Adotante', on_delete=models.CASCADE, verbose_name="Adotante")
    adotado = models.ForeignKey('Adotado', on_delete=models.CASCADE, verbose_name="Adotado")
    grau_de_compatibilidade = models.IntegerField(verbose_name="Grau de compatibilidade (%)")

    def __str__(self):
        return f"{self.adotante} ↔ {self.adotado} ({self.grau_de_compatibilidade}%)"

    class Meta:
        verbose_name = "Compatibilidade"
        verbose_name_plural = "Compatibilidades"
        unique_together = ('adotante', 'adotado')

class ProcessoAdocao(models.Model):
    STATUS_CHOICES = (
        ('Em análise', 'Em análise'),
        ('Aprovado', 'Aprovado'),
        ('Rejeitado', 'Rejeitado'),
        ('Concluído', 'Concluído'),
        ('Cancelado', 'Cancelado'),
    )

    adotante = models.ForeignKey('Adotante', on_delete=models.CASCADE, verbose_name="Adotante")
    adotado = models.ForeignKey('Adotado', on_delete=models.CASCADE, verbose_name="Adotado")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name="Status do processo")
    data_inicio = models.DateField(verbose_name="Data de início")
    data_atualizacao = models.DateField(verbose_name="Última atualização")

    def __str__(self):
        return f"Processo {self.id} - {self.adotante} e {self.adotado}"

    class Meta:
        verbose_name = "Processo de Adoção"
        verbose_name_plural = "Processos de Adoção"

class Informativo(models.Model):
    CATEGORIA_CHOICES = (
        ('Dúvidas frequentes', 'Dúvidas frequentes'),
        ('Documentos necessários', 'Documentos necessários'),
        ('Etapas do processo', 'Etapas do processo'),
        ('Direitos e deveres', 'Direitos e deveres'),
        ('Outros', 'Outros'),
    )

    titulo = models.CharField(max_length=150, verbose_name="Título")
    conteudo = models.TextField(verbose_name="Conteúdo")
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, verbose_name="Categoria")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Informativo"
        verbose_name_plural = "Informativos"

class Administrador(models.Model):
    PERMISSOES_CHOICES = (
        ('Total', 'Acesso total'),
        ('Parcial', 'Acesso parcial'),
        ('Leitura', 'Somente leitura'),
    )

    nome = models.CharField(max_length=100, verbose_name="Nome do administrador")
    login = models.CharField(max_length=50, unique=True, verbose_name="Login")
    senha = models.CharField(max_length=128, verbose_name="Senha")  # Ideal: usar criptografia
    permissoes = models.CharField(max_length=20, choices=PERMISSOES_CHOICES, verbose_name="Permissões")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"

autorizado = models.BooleanField(default=False, verbose_name="Cadastro autorizado")

