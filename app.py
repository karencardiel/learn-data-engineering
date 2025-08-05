from flask import Flask, jsonify, render_template, request, redirect, url_for
import psycopg2
import os

app = Flask(__name__)

# --- Función para conectar a la BD ---
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="catalogo_recursos",
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASS')
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"Error de conexión: {e}")
        return None

# --- RUTA PÚBLICA 1: La página principal que ve el usuario ---
@app.route('/')
def home():
    return render_template('index.html')

# --- RUTA PÚBLICA 2: La API que devuelve los datos en JSON ---
@app.route('/api/resources')
def get_resources():
    conn = get_db_connection()
    if conn is None: return jsonify({"error": "Database connection failed"}), 500
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM resources ORDER BY resource_name ASC;")
    resources_raw = cur.fetchall()
    cur.close()
    conn.close()
    
    resources_list = []
    for resource in resources_raw:
        resources_list.append({
            "id": resource[0],
            "name": resource[1],
            "description": resource[2],
            "type": resource[3],
            "link": resource[4],
            "technologies": resource[5] or [],
            "level": resource[6]
        })
    return jsonify(resources_list)

# --- RUTAS DE ADMINISTRACIÓN ---

# RUTA ADMIN 1: Vista principal del panel
@app.route('/admin')
def admin_panel():
    conn = get_db_connection()
    if conn is None: return "Error de conexión", 500
    
    cur = conn.cursor()
    cur.execute("SELECT id, resource_name, resource_type FROM resources ORDER BY id ASC;")
    resources = cur.fetchall()
    cur.close()
    conn.close()
    
    return render_template('admin/index.html', resources=resources)

# RUTA ADMIN 2: Añadir nuevo recurso
@app.route('/admin/add', methods=('GET', 'POST'))
def add_resource():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        res_type = request.form['type']
        link = request.form['link']
        technologies = [tech.strip() for tech in request.form['technologies'].split(',')]
        level = request.form['level']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO resources (resource_name, description, resource_type, link, technologies, level) VALUES (%s, %s, %s, %s, %s, %s)",
                    (name, description, res_type, link, technologies, level))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('admin_panel'))

    return render_template('admin/resource_form.html', action='Add', resource=None)

# RUTA ADMIN 3: Editar un recurso
@app.route('/admin/edit/<int:id>', methods=('GET', 'POST'))
def edit_resource(id):
    conn = get_db_connection()
    cur = conn.cursor()
    
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        res_type = request.form['type']
        link = request.form['link']
        technologies = [tech.strip() for tech in request.form['technologies'].split(',')]
        level = request.form['level']
        
        cur.execute("UPDATE resources SET resource_name = %s, description = %s, resource_type = %s, link = %s, technologies = %s, level = %s WHERE id = %s",
                    (name, description, res_type, link, technologies, level, id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('admin_panel'))
    
    cur.execute("SELECT * FROM resources WHERE id = %s", (id,))
    resource = cur.fetchone()
    cur.close()
    conn.close()
    
    return render_template('admin/resource_form.html', action='Edit', resource=resource)

# RUTA ADMIN 4: Eliminar un recurso
@app.route('/admin/delete/<int:id>', methods=('POST',))
def delete_resource(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM resources WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('admin_panel'))

if __name__ == '__main__':
    if not os.environ.get('DB_USER') or not os.environ.get('DB_PASS'):
        print("FATAL: Las variables de entorno DB_USER y DB_PASS no están definidas.")
    else:
        app.run(debug=True)