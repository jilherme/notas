#!/usr/bin/python3
'''
index.html

Autor: Pedro H A Konzen - 05/2018
Modificado: 03/2023
'''

import os

class Index:
    
    def __init__(self,odir):
        self.odir = odir
        self.page = ''
        
    def empty_page(self):
        self.page += '<!DOCTYPE html>'
        self.page += '<html lang="pt">'
        self.page += '</html>'

    def add_head(self):
        head = '<head>'
        
        head += '<meta charset="utf-8">'
        head += '<title>Notas de Aula</title>'
        head += '<meta name="author" content="Pedro H A Konzen">'
        head += '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">'

        # # bootstrap 5.1.3
        # head += '<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">'
        # head += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">'
        # head += '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>'

        # bootstrap 5.3.0
        head += '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">'
        head += '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>'

        # jquery 3.6.0
        head += '<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>'
        

        # FontAwesome
        head += '<link href="./fontawesome/css/all.min.css" rel="stylesheet">'
        
        #google tracking
        f = open('gtag.js','r')
        head += f.read()
        f.close()
        
        head += '<!-- Computer Modern Serif-->'
        head += '<link rel="stylesheet" href="fonts/cmun-serif.css">'
        head += '<link rel="stylesheet" href="index.css" type="text/css">'
        
        head += '</head>'

        #add at bottom
        self.page = self.page.replace('</html>',head)
        self.page += '</html>'

    def new_card(self, header, title, text, badges, link, color, status=""):
        card = ""
        card += f'<div class="card border-{color} mb-3" style="width: 20rem;">'
        card += f'<div class="card-header text-bg-{color} d-flex justify-content-between">{header} '
        if (status != ""):
            card += f'<span class="badge bg-secondary">{status}</span>'
        card += '</div>'
        card += '<div class="card-body">'
        card += f'<h4 class="card-title">{title}</h4>'
        card += f'<p class="card-text" style="color: gray">{text}'
        for i,b in enumerate(badges):
            card += f'<span class="badge bg-secondary m-1">{b}</span>'
        card += '</p>'
        card += '<div class="d-flex justify-content-end">'
        card += f'<a href="{link}" class="btn btn-{color} stretched-link d-flex align-items-end">'
        card += 'Abrir'
        card += '</a>'
        card += '</div>'
        card += '</div>'
        card += '</div>'
        return card

    def add_anuncio(self, text, link, status):
        obj = ""
        obj += f'<div class="card border-{status}" role="alert" style="height: 4em">'
        obj += f'<div class="card-body d-flex justify-content-center text-{status}">'
        obj += f'<a href={link} class="stretched-link"></a>'
        obj += f'<div class="spinner-grow spinner-grow-sm text-{status} m-1" role="status"></div>'
        obj += text
        obj += '</div>'
        obj += '</div>'
        return obj


    def add_body(self):
        body = '<body>'
        
        body += '<div class="container-fluid mb-0">'
        body += '<div class="row">'
        body += '<div class="col-xxl-1">'
        body += '</div>'
        body += '<div class="col-xxl-10">'

        # colab alert (id=colabAlert)
        f = open('colab_alert.html','r')
        body += f.read()
        f.close()

        # general alert
        f = open('general_alert.html','r')
        body += f.read()
        f.close()
        
        # Navbar
        body += '<!-- begin: navbar -->'
        body += '<nav class="navbar navbar-dark bg-primary mb-1">'
        body += '<div class="container-fluid">'
        body += '<a class="navbar-brand" href="main.html">Notas de Aula<br/><small>Início</small></a>'
        body += '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">'
        body += '<span class="navbar-toggler-icon"></span>'
        body += '</button>'
        body += '<div class="collapse navbar-collapse" id="navbarNav">'
        body += '<ul class="navbar-nav">'
        body += '<li class="nav-item"><a class="nav-link active" href="index.html"><i class="fas fa-home"></i> Início</a></li>'
        body += '<li class="nav=item"><a class="nav-link" href="https://colab.research.google.com/github/phkonzen/notas/blob/master/notas.ipynb">Google Colab</a></li>'
        body += '<li class="nav-item dropdown">'
        body += '<a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown">'
        body += 'Contato'
        body += '</a>'
        body += '<div class="dropdown-menu" aria-labelledby="navbarDropdown">'
        body += '<a class="dropdown-item" href="./contato.html"><i class="fas fa-envelope"></i> Mensagem</a>'
        body += '<a class="dropdown-item" href="https://www.instagram.com/notas.pedrok/"><i class="fab fa-instagram"></i> notas.pedrok</a>'
        body += '</div><!-- div class="dropdown-menu" aria-labelledby="navbarDropdown" -->'
        body += '</li> <!-- li class="nav-item dropdown" -->'
        body += '<li class="nav-item"><a class="nav-link" href="https://github.com/phkonzen/notas"><i class="fab fa-github" aria-hidden="true"></i> Repo</a></li>'
        body += '<li class="nav-item"><a class="nav-link" href="./politica.html">Política de dados</a></li>'
        body += '</ul>'
        body += '</div><!-- /.navbar-collapse -->'
        body += '</div><!-- /.container-fluid -->'
        body += '</nav>'
        body += '<!-- end: navbar -->'

        # redes sociais
        body += '<p class="text-left mb-0"><a href="./contato.html"><i class="fas fa-envelope"></i></a> | <a href="https://www.instagram.com/notas.pedrok/"><i class="fab fa-instagram"></i></a> | <a href="https://archive.org/details/notas-de-aula"><i class="fas fa-building-columns"></i></a> | <a href="https://www.youtube.com/channel/UCwutHKlKLgVj6IkFSUFBqoA"><i class="fab fa-youtube"></i></a> | <a href="https://github.com/phkonzen/notas"><i class="fab fa-github" aria-hidden="true"></i></a></p>'

        # jumbotron
        body += '<div class="myjumbotron">'
        body += '<div class="jumbotron text-center">'
        body += '<div class="row">'
        body += '<div class="col-lg-3 col-md-2">'
        body += '</div>'
        body += '<div class="col-lg-6 col-md-8 ">'
        body += '<h1 class="display-4 bg-white text-dark mb-0" style="opacity:75%;">Notas de Aula</h1>'
        body += '<p class="lead bg-white text-dark mt-0" style="opacity:75%;">Pedro H A Konzen</p>'
        body += '</div>'
        body += '</div>'
        body += '</div> <!-- div class="jumbotron text-center" -->'
        body += '<p class="mb-0" style="text-align: right; font-size: x-small;">Imagem: <a href="https://flic.kr/p/4krYcm">Eli Duke</a></p>'
        body += '</div> <!-- class="myjumbotron" -->'

        
        
        #miolo

        # Área de anúncios
        body += '<div id="demo" class="carousel slide mt-2 mb-2" data-bs-ride="carousel" style="height: 4em;">'
        
        body += '<!-- The slideshow -->'
        body += '<div class="carousel-inner">'
        
        body += '<div class="carousel-item active">'
        body += self.add_anuncio(text = 'XI ERMAC-RS 2023 - Submissão de trabalhos: até 15/Abr',
                                 link = 'https://wp.ufpel.edu.br/ermacrs23/',
                                 status = 'danger')
        # body += '<div class="spinner-grow spinner-grow-sm text-danger mb-1" role="status"></div>'
        # body += '<a href="https://wp.ufpel.edu.br/ermacrs23/"> <strong></strong></a>'
        body += '</div>'

        body += '<div class="carousel-item">'
        body += self.add_anuncio(text = 'XLII CNMAC 2023 - Submissão de trabalhos: até 10/Abr',
                                 link = 'http://www.cnmac.org.br/novo/',
                                 status = 'danger')
        # body += '<div class="spinner-grow spinner-grow-sm text-danger mb-1" role="status"></div>'
        # body += '<a href="http://www.cnmac.org.br/novo/"> XLII CNMAC 2023 - Submissão de trabalhos: até 10/Abr</a>'
        body += '</div>'

        body += '<div class="carousel-item">'
        body += self.add_anuncio(text = 'PPGMAp - UFRGS: Processo Seletivo para Aluna(o) Especial',
                                 link = 'https://www.ufrgs.br/ppgmap/?p=1422',
                                 status = 'danger')
        # body += '<div class="spinner-grow spinner-grow-sm text-danger mb-1" role="status"></div>'
        # body += '<a href="https://www.ufrgs.br/ppgmap/?p=1422"> PPGMAp - UFRGS: Processo Seletivo para Aluna(o) Especial</a>'
        body += '</div>'

        body += '<div class="carousel-item">'
        body += self.add_anuncio(text = 'IME - UFRGS: Instituto de Matemática e Estatística',
                                 link = 'http://www.ufrgs.br/ime',
                                 status = 'primary')
        # body += '<div class="spinner-grow spinner-grow-sm text-primary mb-1" role="status"></div>'
        # body += '<a href="http://www.ufrgs.br/ime"> IME - UFRGS: Instituto de Matemática e Estatística</a>'
        body += '</div>'
  
        body += '</div>'
        body += '</div>'

        body += '<h3 class="">Notas de Aula</h3>'
        body += '<hr>'

        body += '<div class="row row-cols-auto justify-content-around">'
        
        # card: notas de aula de Cálculo I
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Cálculo I",
                              text = "Cálculo diferencial e integral de funções de uma variável real",
                              badges = ["Python", "Sympy"],
                              link = "CalculoI/main.html",
                              color = "warning", status = "Ativo")
        body += '</div>'

        # card: notas de aula de EaD
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Equações a Diferenças",
                              text = "Introdução a equações a diferenças",
                              badges = ["Python", "Sympy"],
                              link = "EaD/main.html",
                              color = "primary", status = "Estável")
        body += '</div> '

        # card: notas de aula de EDO
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Equações Diferenciais Ordinárias",
                              text = "Introdução a equações diferenciais ordinárias",
                              badges = ["Python", "Sympy"],
                              link = "EDO/main.html",
                              color = "primary", status = "Estável")
        body += '</div>'

        # card: Geometria analítica
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Geometria Analítica",
                              text = "Introdução a geometria analítica",
                              badges = [],
                              link = "GeometriaAnalitica/main.html",
                              color = "primary", status = "Estável")
        body += '</div>'

        # card: notas de aula de Matemática numérica
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Matemática Numérica",
                              text = "Métodos e técnicas de cálculo numérico",
                              badges = ["Octave"],
                              link = "MatematicaNumerica/main.html",
                              color = "danger", status = "Antigo")
        body += '</div>'

        # card: notas de aula de Matemática Numérica I
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Matemática Numérica I",
                              text = "Introdução ao cálculo numérico na resolução de equações e sistemas de equações",
                              badges = ["Python", "NumPy"],
                              link = "MatematicaNumericaI/main.html",
                              color = "warning", status = "Ativo")
        body += '</div>'

        # card: notas de aula de Matemática Numérica Avançada
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Matemática Numérica Avançada",
                              text = "Tópicos de métodos numéricos avançados",
                              badges = ["Python", "NumPy", "SciPy", "Matplotlib"],
                              link = "MatematicaNumericaAvancada/main.html",
                              color = "warning", status = "Ativo")
        body += '</div>'

        # card: notas de aula de Matemática Numérica Paralela
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Matemática Numérica Paralela",
                              text = "Introdução à computação paralela a métodos numéricos",
                              badges = ["C/C++", "OpenMP", "OpenMPI"],
                              link = "MatematicaNumericaParalela/main.html",
                              color = "primary", status = "Estável")
        body += '</div>'

        # card: Método de elementos finitos
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Método dos Elementos Finitos",
                              text = "Introdução ao método dos elementos finitos",
                              badges = ["Python", "FEniCS"],
                              link = "MetodoElementosFinitos/main.html",
                              color = "primary", status = "Estável")
        body += '</div>'

        # card: Pré-Cálculo
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Pré-Cálculo",
                              text = "Matemáticas essencial para um curso de cálculo",
                              badges = ["Python", "SymPy"],
                              link = "PreCalculo/main.html",
                              color = "warning", status = "Ativo")
        body += '</div>'

        # card: Vetores
        body += '<div class="col">'
        body += self.new_card(header = "Notas de Aula",
                              title = "Vetores",
                              text = "Vetores no espaço euclidiano tridimensional",
                              badges = [],
                              link = "Vetores/main.html",
                              color = "primary", status = "Estável")
        body += '</div>'

        body += '</div> <!-- div class=row-->'

        # Minicursos
        body += '<h3>Minicursos</h3>'
        body += '<hr>'
        
        body += '<div class="row row-cols-auto justify-content-around">'

        # card: notas do Minicurso de Python para Matemática
        body += '<div class="col">'
        body += self.new_card(header = "Minicursos",
                              title = "Python para Matemática",
                              text = "Introdução à Python para matemática",
                              badges = ["Python", "NumPy", "Matplotlib"],
                              link = "MiniPython/main.html",
                              color = "primary", status = "Estável")
        body += '</div>'

        # card: Mini Cálculo com Python
        body += '<div class="col">'

        body += '<!-- card: Mini Cálculo com Python -->'
        body += '<div class="card border-primary mb-3" style="width: 20rem;">'

        body += '<div class="card-header bg-primary text-white">Minicurso <span class="badge bg-secondary">Python</span></div>'

        body += '<div class="card-body">'
        body += '<h4 class="card-title">Cálculo com Python</h4>'
        body += '<p class="card-text" style="color: gray">Introdução à Python na resolução de problemas de Cálculo I.</p>'
        body += '<ul>'
        body += '<li><a href="https://colab.research.google.com/github/phkonzen/notas/blob/master/docs/MiniCalcPy/1-funcoes.ipynb">Parte 1 - Funções de uma variável</a></li>'
        body += '<li><a href="https://colab.research.google.com/github/phkonzen/notas/blob/master/docs/MiniCalcPy/2-limites.ipynb">Parte 2 - Limites</a></li>'
        body += '<li><a href="https://colab.research.google.com/github/phkonzen/notas/blob/master/docs/MiniCalcPy/3-derivada.ipynb">Parte 3 - Derivadas</a></li>'
        body += '<li><a href="https://colab.research.google.com/github/phkonzen/notas/blob/master/docs/MiniCalcPy/4-integracao.ipynb">Parte 4 - Integrais</a></li>'
        body += '</ul>'
        body += '</div>'

        body += '</div>'
        body += '</div>'

        body += '</div> <!-- div class="row" -->'

        
        body += '<h3>Vídeos & Áudios</h3>'
        body += '<hr>'

        body += '<div class="row row-cols-auto justify-content-around">'

        # card: Internet Archive
        body += '<!-- card: Internet Archive -->'
        body += '<div class="col">'
        body += self.new_card(header = "Vídeos & Áudios",
                              title = '<i class="fas fa-building-columns"></i> Internet Archive',
                              text = "Coleção de vídeos e áudios das Notas de Aula no archive.org",
                              badges = [],
                              link = "https://archive.org/details/notas-de-aula",
                              color = "primary")
        body += '</div>'

        # card: YouTube
        body += '<!-- card: YouTube -->'
        body += '<div class="col">'
        body += self.new_card(header = "Vídeos & Áudios",
                              title = '<i class="fab fa-youtube"></i> YouTube',
                              text = "Coleção de vídeos das Notas de Aula no YouTube",
                              badges = [],
                              link = "https://www.youtube.com/channel/UCwutHKlKLgVj6IkFSUFBqoA",
                              color = "primary")
        body += '</div>'

        
        body += '</div><!-- div class="row" -->'

        
        body += '<div class="row">'

        body += '<div class="col-md-6">'

        body += '<h3>Sobre</h3>'
        body += '<hr>'
        body += '<p>Neste <i>site</i> publico minhas notas de aula. '
        body += 'O material está escrito predominante em linguagem de marcação '
        body += '<a href="https://www.latex-project.org/">LaTeX</a>. '
        body += 'Disponíveis sob licença '
        body += '<a href="http://creativecommons.org/licenses/by-sa/4.0/deed.pt_BR">CC-BY-SA 4.0</a>, '
        body += 'os códigos-fonte podem ser obtidos no '
        body += 'repositório GitHub '
        body += '<a href="https://github.com/phkonzen/notas">https://github.com/phkonzen/notas</a>.</p>'
        body += '<p>Aproveito para agradecer a todos e todas que de forma assídua ou esporádica '
        body += 'contribuem com correções, sugestões e críticas! '
        body += '<i class="far fa-smile"></i>'
        body += '</p>'

        body += '</div><!-- div class="col-md-6" -->'

        body += '<div class="col-md-6">'

        body += '<h3>Sobre mim?</h3>'
        body += '<hr>'
        body += '<ul>'
        body += '<li><a href="http://lattes.cnpq.br/2565213716047382">Currículo Lattes</a></li>'
        body += '<li><a href="http://professor.ufrgs.br/pedro/">Página de professor na UFRGS</a></li>'
        body += '</ul>'

        body += '<h3>Ligações Recomendadas</h3>'
        body += '<ul>'
        body += '<li><a href="https://archive.org/">Internet Archive</a>: biblioteca de milhões de livros, filmes, <i>softwares</i>, música, <i>websites</i> e mais</li>'
        body += '<li><a href="https://www.geogebra.org/">Geogebra</a>: aplicativos abertos de matemática</li>'
        body += '<li><a href="https://www.ufrgs.br/reamat">REAMAT</a>: projeto de recursos educacionais abertos de matemática</li>'
        body += '</ul>'

        body += '</div><!-- div class="col-md-6" -->'

        body += '</div><!-- div class="row" -->'

        # rodapé (id=rodape)
        f = open('rodape.html','r')
        body += f.read()
        f.close()

        body += '</div> <!-- div class=col-xxl-10 -->'
        # body += '<div class=col-xl-1>'
        # body += '</div>'
        body += '</div><!-- div row -->'
        body += '</div> <!-- div class=container-fluid -->'

        body += '</body>'


        #add at bottom
        self.page = self.page.replace('</html>',body)
        self.page += '</html>'

    def build(self):
        self.empty_page()
        self.add_head()
        self.add_body()
        f = open(self.odir + '/index.html','w')
        f.write(self.page)
        f.close()

        os.system('cp index.css '+self.odir+'/')
