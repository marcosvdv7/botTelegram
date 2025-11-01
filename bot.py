from telegram import Update  # type: ignore
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes  # type: ignore
import mysql.connector

# Conexión con la base de datos
def obtener_pelis():
    conn = mysql.connector.connect(
        host="sql312.infinityfree.com",       # Host de InfinityFree
        user="if0_39471841",                  # Usuario de InfinityFree
        password="CEfSXinYJOQY",              # Contraseña
        database="if0_39471841_usuarios"      # Nombre de la base de datos
    )
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM pelis ORDER BY id DESC LIMIT 10;")
    titulos = cursor.fetchall()
    conn.close()
    return [n[0] for n in titulos]

# Comando /Ultimas_Pelis
async def Ultimas_Pelis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    titulos = obtener_pelis()
    mensaje = "👋 Hola! Aquí tienes las últimas 10 películas añadidas:\n" + "\n".join(f"• {n}" for n in titulos)
    await update.message.reply_text(mensaje)

# Configuración del bot
if __name__ == '__main__':
    app = ApplicationBuilder().token("8174851010:AAHEpX8o6vS1cuaiUj15g2XLvqnlXbfaLIA").build()
    app.add_handler(CommandHandler("Ultimas_Pelis", Ultimas_Pelis))
    app.run_polling()
