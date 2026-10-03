from flask import Flask, render_template, request, jsonify, send_file
from agent import CertificateAgent
from database import init_db, save_certificate, get_certificate
from certificate_service import create_certificate_pdf

app = Flask(__name__)
agent = CertificateAgent()
init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.post("/api/generate")
def generate():
    data = request.get_json() or {}
    result = agent.run(data)
    if not result["success"]:
        return jsonify(result), 400

    save_certificate(result["certificate"])
    return jsonify(result)

@app.get("/certificate/<certificate_id>")
def certificate(certificate_id):
    item = get_certificate(certificate_id)
    if not item:
        return "Certificate not found", 404
    return render_template("certificate.html", certificate=item)

@app.get("/certificate/<certificate_id>/pdf")
def certificate_pdf(certificate_id):
    item = get_certificate(certificate_id)
    if not item:
        return "Certificate not found", 404

    path = create_certificate_pdf(item)
    return send_file(path, as_attachment=True, download_name=f"{certificate_id}.pdf")

if __name__ == "__main__":
    app.run(debug=True)
