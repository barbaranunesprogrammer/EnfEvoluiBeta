from flask import Flask, request, render_template

app = Flask(__name__)

# 👩‍⚕️ Profissionais fictícios fixos (DEMONSTRAÇÃO)
PROFISSIONAIS_DEMO = {
    "Profissional Demo A": "COREN-000000",
    "Profissional Demo B": "COREN-111111"
}

@app.route("/", methods=["GET", "POST"])
def index():

    texto = ""
    mensagem = "⚠️ Versão Demonstrativa – Dados não são armazenados e não possuem validade legal."

    if request.method == "POST":

        h = request.form.get("horario", "")
        profissional = request.form.get("profissional", "")
        coren = PROFISSIONAIS_DEMO.get(profissional, "COREN-DEMO")

        consciente = request.form.get("consciente")
        queixa = request.form.get("queixa")
        descricao_queixa = request.form.get("descricao_queixa", "")
        dor = request.form.get("dor", "")
        puncao = request.form.get("puncao")
        abocath = request.form.get("abocath", "")
        medicacao = request.form.get("medicacao")
        desfecho = request.form.get("desfecho")

        texto = "********** VERSÃO DEMONSTRATIVA **********\n\n"
        texto += f"{h} – Recebo paciente da Sala de Medicação.\n"

        # Estado neurológico
        if consciente == "1":
            texto += "Paciente consciente e orientado.\n"
        else:
            texto += "Paciente não consciente ou desorientado.\n"

        # Queixa
        if queixa == "1":
            texto += f"Paciente refere: {descricao_queixa}.\n"
            if dor:
                texto += f"Escala de dor referida: {dor}/10.\n"
        else:
            texto += "Paciente sem queixas no momento.\n"

        # Punção venosa
        if puncao == "1":
            texto += "Realizada punção venosa.\n"
            if abocath:
                texto += f"Utilizado abocath nº {abocath}.\n"
        else:
            texto += "Não foi necessária punção venosa.\n"

        # Medicação
        if medicacao == "1":
            texto += "Medicação administrada conforme prescrição médica.\n"
        else:
            texto += "Medicação não administrada.\n"

        # Desfecho
        if desfecho == "1":
            texto += "Paciente recebe alta.\n"
        elif desfecho == "2":
            texto += "Paciente retorna para avaliação médica.\n"
        elif desfecho == "3":
            texto += "Paciente evadiu-se da unidade.\n"

        texto += f"\n{profissional} – {coren}\nTécnica de Enfermagem\n"
        texto += "\n********** NÃO UTILIZAR COMO DOCUMENTO OFICIAL **********"

    return render_template(
        "index.html",
        texto=texto,
        profissionais=PROFISSIONAIS_DEMO,
        mensagem=mensagem
    )

if __name__ == "__main__":
    app.run(debug=True)