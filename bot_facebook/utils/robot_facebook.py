#coding: utf-8
__author__ = "Lário dos Santos Diniz"

from pprint import pprint

import sys
from bot_facebook.models import Jogadores
from core.models import MensagensPadrao, Aventura, Personagem, Cena, Opcao

from bot_facebook.utils import Service


class RobotFacebook:

    def __init__(self, id_usuario, mensagem_usuario):

        self._jogador = Jogadores()
        self.id_usuario = id_usuario
        self.mensagem_usuario = mensagem_usuario

        self.service = Service(id_usuario)

        if not self._MensagensPadrao():
            self._verificaJogador()


    def _BoasVindas(self):
        mensagem = "Olá, seja bem vindo a pagina Dados & Desventuras.\nGostaria de jogar uma Aventura de RPG pelo messenger?"
        mensagem += "\n\n"
        mensagem += 'Responda "Quero Jogar" para jogar.'
        self.service.EnviaMensagem(mensagem)


    def _verificaJogador(self):
        if not Jogadores.objects.filter(id=self.id_usuario).exists():
            if "quero jogar" in self.mensagem_usuario.lower():
                self._CadastraJogador()
                self._IniciaAventura()
            else:
                self._BoasVindas()
        else:
            self._jogador = Jogadores.objects.get(pk=self.id_usuario)
            self._VerificaAventura()


    def _VerificaAventura(self):
        if not self._jogador.aventura_atual:
            if self._jogador.status == 0:
                self._IniciaAventura()
            elif self._jogador.status == 1:
                self._DefineAventuraAtual()
        else:
            if self._jogador.status == 2:
                self._CriandoPersonagem()
            elif self._jogador.status == 3:
                self._personagem = Personagem.objects.get(jogadorF=self._jogador, aventura=self._jogador.aventura_atual)
                self._JogandoAventura()

    def _JogandoAventura(self):
        if self._personagem.cena_atual:
            if (
                self.mensagem_usuario.isdigit() and
                Opcao.objects.filter(cena=self._personagem.cena_atual, pk=int(self.mensagem_usuario)).exists()
            ):
                opcao = Opcao.objects.get(cena=self._personagem.cena_atual, pk=int(self.mensagem_usuario))
                if opcao.proxima_cena:
                    self._personagem.cena_atual = opcao.proxima_cena
                    self._personagem.save()
                else:
                    self._FimDeJogo();

            else:
                self._MensagemNaoEntendida()

            self._BuscaCena(self._personagem.cena_atual.numero)
        else:
            self.service.EnviaMensagem("-*-    *    -*-\n{}\n-*-    *    -*-".format(self._personagem.aventura))
            self._personagem.cena_atual = Cena.objects.get(aventura=self._personagem.aventura, numero = 1)
            self._personagem.save()
            self._BuscaCena(1)

    def _FimDeJogo(self):
        self.service.EnviaMensagem("-*-    *    -*-\n{}\n-*-    *    -*-".format("Fim de Jogo"))
        self._jogador.aventura_atual = None
        self._jogador.status = 1
        self._jogador.save()

    def _BuscaCena(self, numero):
        cena = Cena.objects.get(aventura=self._personagem.aventura, numero = numero)
        self.service.EnviaMensagem(cena.descricao)

        opcoes = Opcao.objects.filter(cena=cena)

        if not opcoes.exists():
            self._FimDeJogo()
        else:
            self.service.EnviaMensagem("Escreva o numero da sua escolha:")
            for opcao in opcoes:
                self.service.EnviaMensagem(str(opcao))


    def _CriandoPersonagem(self):

        if Personagem.objects.filter(jogadorF=self._jogador, aventura=self._jogador.aventura_atual).exists():
            self._personagem = Personagem.objects.get(jogadorF=self._jogador)
            self._personagem.cena_atual = None
        else:
            self._personagem = Personagem()
            self._personagem.jogadorF = self._jogador
            self._personagem.nome = str(self._jogador)


        self._personagem.aventura = self._jogador.aventura_atual
        self._personagem.save()

        self._jogador.status = 3
        self._jogador.save()

        self._VerificaAventura()




    def _DefineAventuraAtual(self):
        if self.mensagem_usuario.isdigit() and Aventura.objects.filter(id=self.mensagem_usuario).exists():
            aventura = Aventura.objects.get(id=self.mensagem_usuario)
            self._jogador.aventura_atual = aventura
            self._jogador.status = 2
            self._jogador.save()

            self._VerificaAventura()
        else:
            self._MensagemNaoEntendida()

    def _MensagemNaoEntendida(self):
        mensagem = "Desculpe {}, Não entendemos o que você falou.\n\nTente de novo.".format(str(self._jogador))
        self.service.EnviaMensagem(mensagem)
        self._EscolhendoAventura()

    def _IniciaAventura(self):

        self._jogador.status = 1
        self._jogador.save()

        mensagem = "Certo {}, vamos escolher a aventura!".format(str(self._jogador))
        self.service.EnviaMensagem(mensagem)
        self._EscolhendoAventura()


    def _EscolhendoAventura(self):

        mensagem = "Escreva o numero para escolher!"
        self.service.EnviaMensagem(mensagem)
        aventuras = Aventura.objects.all()
        mensagem = ""
        for aventura in aventuras:
            mensagem += str(aventura) + "\n"

        self.service.EnviaMensagem(mensagem)

    def _CadastraJogador(self):
            mensagem = "Você não é um jogador cadastrado. Estamos te cadastrando..."
            self.service.EnviaMensagem(mensagem)

            dadosUsuario = self.service.BuscaDadosUsuario()

            self._jogador.id = int(self.id_usuario)

            self._jogador.primeiro_nome = dadosUsuario['first_name'] if 'first_name' in dadosUsuario else "não definido"
            self._jogador.ultimo_nome = dadosUsuario['last_name'] if 'last_name' in dadosUsuario else "não definido"


            try:
                self._jogador.save()
            except Exception as a:
                pprint(a)
                sys.stdout.flush()

            if Jogadores.objects.filter(id=self.id_usuario).exists():

                mensagem = "Parabens {}! Você foi cadastrado com sucesso.".format(str(self._jogador))
                self.service.EnviaMensagem(mensagem)
            else:
                mensagem = "Não conseguimos te cadastrar, por favor, tente de novo mais tarde."
                self.service.EnviaMensagem(mensagem)



    def _MensagensPadrao(self):
        mensagensPadrao = MensagensPadrao.objects.all()
        for mensagempadrao in mensagensPadrao:
            if mensagempadrao.mensagem.lower() in self.mensagem_usuario.lower():
                self.service.EnviaMensagem(mensagempadrao.resposta)
                return True
        return False



