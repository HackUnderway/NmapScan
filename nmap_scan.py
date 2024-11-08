from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    scan_result = ""
    command_executed = ""

    if request.method == "POST":
        # Obtener los datos del formulario
        target = request.form.get("target")
        scan_type = request.form.get("scan_type")

        # Mapear el tipo de escaneo seleccionado a la opción correspondiente de Nmap
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
        
        # Obtener la opción de Nmap basada en la selección del usuario
        nmap_option = scan_options.get(scan_type, "-sP")  # Por defecto, Ping Scan

        # Si el escaneo seleccionado requiere privilegios de root, agregar "sudo" al comando
        requires_sudo = scan_type in ["OS Detection Scan (-O)", "Firewall Detection (-sA)", "SYN Scan (-sS)", "UDP Scan (-sU)", "Fragmented Packets Scan (-f)", "Traceroute (-tr)", "Intense Scan (-T4 -A -v)", "Comprehensive Scan (-p 1-65535 -T4 -A -v)", "Aggressive Scan (-A)"]
        command = (["sudo", "nmap"] if requires_sudo else ["nmap"]) + nmap_option.split() + [target]
        command_executed = " ".join(command)  # Mostrar el comando para depuración/feedback

        try:
            # Ejecutar el comando y capturar el resultado
            scan_result = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            scan_result = f"Error executing Nmap: {e.output}"

    return render_template("index.html", command_executed=command_executed, scan_result=scan_result)

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(debug=True, port=8080) Cambia el puerto aquí
