from flask import Flask, render_template,request,redirect
import sqlite3

app=Flask(__name__)

def init_db():
    conn=sqlite3.connect('notes.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY, title TEXT,content TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn=sqlite3.connect('notes.db')
    c=conn.cursor()
    c.execute('SELECT * FROM notes')
    notes=c.fetchall()
    
    conn.close()
    print("db")
    return render_template('index.html', notes=notes)

@app.route('/add',methods=['POST'])
def add_note():
    title=request.form['title']
    content=request.form['content']
    conn=sqlite3.connect('notes.db')
    c=conn.cursor()
    c.execute('INSERT INTO notes(title,content) VALUES(?,?)',(title,content))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    conn=sqlite3.connect('notes.db')
    c=conn.cursor()
    c.execute('DELETE FROM notes WHERE id=?',(note_id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/edit/<int:note_id>', methods=['POST'])
def edit_note(note_id):
    t=request.form['t']
    conn=sqlite3.connect('notes.db')
    c=conn.cursor()
    c.execute('UPDATE notes SET title=? where id=?',(t,note_id))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__=='__main__':
    init_db()
    app.run(debug=True)