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
    mensagem = "⚠️ Versão Beta Demonstrativa – Dados não são armazenados e não possuem validade legal."

    if request.method == "POST":

        h = request.form.get("horario", "")
        profissional = request.form.get("profissional", "")
        coren = PROFISSIONAIS_DEMO.get(profissional, "COREN-DEMO")

        texto = "********** VERSÃO DEMONSTRATIVA **********\n\n"
        texto += f"{h} – Recebo paciente da Sala de Medicação.\n"
        texto += "Paciente consciente e orientado.\n"
        texto += "Paciente sem queixas no momento.\n"
        texto += "Medicação administrada conforme prescrição médica.\n"
        texto += "Paciente recebe alta.\n"
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