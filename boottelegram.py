import telebot

CHAVE_API = "5905470096:AAHZQrJenb8CcSFn0rqbsqrC9EnKp5JrCG8"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id, """Maior que o universo, mais intenso que as poeiras das galaxias e mais lindo que o nascimento de uma estrela""")

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id, "https://www.youtube.com/watch?v=0CEkbD3nepI")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id, "QUE BEIJINHO GOTOSO, QUERO MAIS")


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Olá! esse bot foi feito especialmente pro amor da minha vida HELOISA BITU! 
    
    ESCOLHA UMA DAS OPÇÕES ABAIXO(só funciona com a Heloisa, CLIQUE EM UMA DAS OPÇÕES)
    
    /opcao1 O tamanho do meu Amor pela Heloisa
    
    /opcao2 Música que me lembra ela
    
    /opcao3 Mandar um beijinho pra ela
    
    Responder qualquer outra coisa/nome não vai funcionar, clique em uma das opções acima"""
    bot.reply_to(mensagem, texto)

bot.polling()