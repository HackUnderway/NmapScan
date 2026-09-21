from flask import Flask, render_template, request, send_file, session, jsonify
import subprocess
import threading
import uuid
import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_cambiar'  # ¡Cámbiala!

progress_tasks = {}

def run_nmap_with_progress(task_id, command, target):
    try:
        progress_tasks[task_id] = {'progress': 0, 'status': 'running', 'result': ''}
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        output_lines = []
        for line in process.stdout:
            output_lines.append(line)
            # No necesitamos porcentaje real, solo mantenemos el estado
        process.wait()
        if process.returncode == 0:
            progress_tasks[task_id]['progress'] = 100
            progress_tasks[task_id]['status'] = 'complete'
            progress_tasks[task_id]['result'] = ''.join(output_lines)
        else:
            progress_tasks[task_id]['status'] = 'error'
            progress_tasks[task_id]['result'] = f"Error (código {process.returncode}):\n{''.join(output_lines)}"
    except Exception as e:
        progress_tasks[task_id]['status'] = 'error'
        progress_tasks[task_id]['result'] = f"Excepción: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        target = request.form.get("target")
        scan_type = request.form.get("scan_type")
        
        scan_options = {
            "Ping Scan (-sP)": "-sP",
            "TCP Connect Scan (-sT)": "-sT",
            "SYN Scan (-sS)": "-sS",
            "Aggressive Scan (-A)": "-A",
            "OS Detection Scan (-O)": "-O",
            "Scan without Ping (-Pn)": "-Pn",
            "UDP Scan (-sU)": "-sU",
            "Fragmented Packets Scan (-f)": "-f",
            "Traceroute (-tr)": "--traceroute",
            "Firewall Detection (-sA)": "-sA",
            "Version Detection (-sV)": "-sV",
            "Intense Scan (-T4 -A -v)": "-T4 -A -v",
            "Comprehensive Scan (-p 1-65535 -T4 -A -v)": "-p 1-65535 -T4 -A -v"
        }
        nmap_option = scan_options.get(scan_type, "-sP")
        requires_sudo = scan_type in [
            "OS Detection Scan (-O)", "Firewall Detection (-sA)",
            "SYN Scan (-sS)", "UDP Scan (-sU)", "Fragmented Packets Scan (-f)",
            "Traceroute (-tr)", "Intense Scan (-T4 -A -v)",
            "Comprehensive Scan (-p 1-65535 -T4 -A -v)", "Aggressive Scan (-A)"
        ]
        command = (["sudo", "nmap"] if requires_sudo else ["nmap"]) + nmap_option.split() + [target]
        command_str = " ".join(command)
        task_id = str(uuid.uuid4())
        progress_tasks[task_id] = {'progress': 0, 'status': 'starting', 'result': ''}
        thread = threading.Thread(target=run_nmap_with_progress, args=(task_id, command, target))
        thread.daemon = True
        thread.start()
        
        session['task_id'] = task_id
        session['target'] = target
        session['scan_type'] = scan_type
        session['command_executed'] = command_str
        
        return render_template("index.html", 
                               task_id=task_id, 
                               scan_running=True,
                               target=target,
                               scan_type=scan_type)
    # GET: limpiar estado
    return render_template("index.html", scan_running=False)

@app.route("/progress/<task_id>")
def get_progress(task_id):
    task = progress_tasks.get(task_id)
    if task:
        return jsonify({
            'progress': task['progress'],
            'status': task['status'],
            'result': task.get('result', '')
        })
    return jsonify({'progress': 0, 'status': 'not_found', 'result': ''})

@app.route("/download_pdf", methods=["POST"])
def download_pdf():
    scan_result = request.form.get("scan_result", "Sin resultados")
    target = request.form.get("target", "Desconocido")
    scan_type = request.form.get("scan_type", "No especificado")
    
    # Limpiar caracteres extraños y normalizar saltos
    scan_result_clean = scan_result.strip().replace('\r\n', '\n').replace('\r', '\n')
    
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    
    code_style = ParagraphStyle(
        'CodeSmall',
        parent=styles['Code'],
        fontSize=8,
        fontName='Courier'
    )
    
    story = []
    story.append(Paragraph("Informe de Escaneo Nmap", styles['Heading1']))
    story.append(Spacer(1, 0.1 * inch))
    story.append(Paragraph(f"<b>Objetivo:</b> {target}", styles['Normal']))
    story.append(Paragraph(f"<b>Tipo de escaneo:</b> {scan_type}", styles['Normal']))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("<b>Resultados:</b>", styles['Heading2']))
    story.append(Spacer(1, 0.1 * inch))
    result_text = Preformatted(scan_result_clean, code_style)
    story.append(result_text)
    
    doc.build(story)
    buffer.seek(0)
    return send_file(
        buffer,
        as_attachment=True,
        download_name=f"nmap_scan_{target}.pdf",
        mimetype='application/pdf'
    )

if __name__ == "__main__":
    app.run(debug=True)
