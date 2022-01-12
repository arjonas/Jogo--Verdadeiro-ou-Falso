from question_model import Questao
from data import question_data
from quiz_brain import QuizBrain

listaperguntas =[]
for valor in question_data:
    enunciado =valor['texto']
    resposta = valor['resposta']
    novapergunta = Questao(enunciado,resposta)
    listaperguntas.append(novapergunta)


quiz = QuizBrain(listaperguntas)

quiz.nextquestion()
