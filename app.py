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

        tipo = request.form.get("tipo_registro")

        profissional = request.form.get("profissional", "")
        coren = PROFISSIONAIS_DEMO.get(profissional, "COREN-DEMO")

        texto = "********** VERSÃO DEMONSTRATIVA **********\n\n"

        # =========================
        # 🏥 EVOLUÇÃO NORMAL
        # =========================
        if tipo == "evolucao":

            h = request.form.get("horario", "")
            setor = request.form.get("setor","")
            consciente = request.form.get("consciente")
            queixa = request.form.get("queixa")
            descricao_queixa = request.form.get("descricao_queixa", "")
            dor = request.form.get("dor", "")
            puncao = request.form.get("puncao")
            abocath = request.form.get("abocath", "")
            abocath_outro = request.form.get("abocath_outro", "")
            medicacao = request.form.get("medicacao")
            desfecho = request.form.get("desfecho")

            if abocath == "outro":
                abocath = abocath_outro

            if not abocath:
                abocath = "não especificado"

            texto += f"{h} – Recebo paciente na {setor}.\n"

            # Estado neurológico
            if consciente == "Sim":
                texto += "Paciente consciente e orientado.\n"
            else:
                texto += "Paciente não consciente ou desorientado.\n"

            # Queixa
            if queixa == "Sim":
                texto += f"Paciente refere: {descricao_queixa}.\n"
                if dor:
                    texto += f"Escala de dor referida: {dor}/10.\n"
            else:
                texto += "Paciente sem queixas no momento.\n"

            # Punção venosa
            if puncao == "Sim":
                texto += f"Realizada punção venosa com abocath nº {abocath}.\n"
            else:
                texto += "Não foi necessária punção venosa.\n"

            # Medicação
            if medicacao == "Sim":
                texto += "Medicação administrada conforme prescrição médica.\n"
            else:
                texto += "Medicação não administrada.\n"

            # Desfecho
            if desfecho:
                texto += f"{desfecho}.\n"

        # =========================
        # 🩹 CURATIVO
        # =========================
        elif tipo == "curativo":

            h = request.form.get("horario_curativo", "")
            tipo_curativo = request.form.get("tipo_curativo", "")

            qtd_gaze = request.form.get("qtd_gaze")
            alcool = request.form.get("alcool")
            clorexidina = request.form.get("clorexidina")
            sf = request.form.get("sf")
            pomada = request.form.get("pomada", "")
            outros = request.form.get("outros_materiais", "")

            aspecto = request.form.get("aspecto", "")
            exsudato = request.form.get("exsudato", "")

            texto += f"{h} – Realizado curativo.\n\n"
            texto += f"Tipo de curativo: {tipo_curativo}.\n"

            materiais = []

            if qtd_gaze and int(qtd_gaze) > 0:
                materiais.append(f"{qtd_gaze} gaze(s)")

            if alcool:
                materiais.append("Álcool 70%")

            if clorexidina:
                materiais.append("Clorexidina")

            if sf:
                materiais.append("SF 0,9%")

            if pomada:
                materiais.append(f"Pomada {pomada}")

            if outros:
                materiais.append(outros)

            if materiais:
                texto += "Utilizado: " + ", ".join(materiais) + ".\n"

            if aspecto:
                texto += f"Ferida apresentando aspecto {aspecto}.\n"

            if exsudato:
                texto += f"Exsudato {exsudato}.\n"

            texto += "Procedimento realizado com técnica asséptica.\n"

        # =========================
        # PROFISSIONAL
        # =========================
        texto += f"\n{profissional} – {coren}\n"
        texto += "Técnica de Enfermagem\n"
        texto += "\n********** NÃO UTILIZAR COMO DOCUMENTO OFICIAL **********"

    return render_template(
        "index.html",
        texto=texto,
        profissionais=PROFISSIONAIS_DEMO,
        mensagem=mensagem
    )

if __name__ == "__main__":
    app.run(debug=True)