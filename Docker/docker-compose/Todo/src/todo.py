import psycopg2
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Conectar a la base de datos
def get_db_connection():
    try:
        conn = psycopg2.connect(
            database="<database_name>",
            user="<username>",
            password="<password>",  # Asegúrate de que sea la contraseña correcta
            host="<db_service>",  # Usa el nombre del servicio en docker-compose
            port="5432"
        )
        print("✅ Conexión a PostgreSQL exitosa")
        return conn
    except Exception as e:
        print(f"❌ Error al conectar con PostgreSQL: {e}")
        return None

@app.route('/')
def index():
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM shopping_list")
        items = [row[1] for row in cur.fetchall()]
        print(f"📌 Items en BD: {items}")  # Depuración
        cur.close()
        conn.close()
    else:
        items = []
    
    return render_template('index.html', items=items)


@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        conn = get_db_connection()
        if conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO shopping_list (item) VALUES (%s)", (item,))
            conn.commit()
            cur.close()
            conn.close()
            print(f"✅ Item agregado a la base de datos: {item}")
        else:
            print("❌ No se pudo conectar a la base de datos")
    
    return redirect(url_for('index'), code=303)  # Código 303 evita reenvío POST
@app.route('/remove/<int:item_index>')
def remove_item(item_index):
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM shopping_list WHERE id = %s", (item_index,))
        conn.commit()
        cur.close()
        conn.close()
        print(f"🗑️ Item eliminado con ID {item_index}")
    else:
        print("❌ No se pudo conectar a la base de datos")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

