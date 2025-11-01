from telegram import Update  # type: ignore
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes  # type: ignore
import mysql.connector
import os
# Conexión con la base de datos
def obtener_pelis():
    import os
    conn = mysql.connector.connect(
    host=os.environ["DB_HOST"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASS"],
    database=os.environ["DB_NAME"]

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
    app = ApplicationBuilder().token("BOT_TOKEN").build()
    app.add_handler(CommandHandler("Ultimas_Pelis", Ultimas_Pelis))
    app.run_polling()
# Comando /hola
async def hola(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = (
        "📼 Bienvenido a *TheCineVerse_bot* 🎥\n"
        "Aquí puedes explorar películas, géneros y comandos temáticos.\n\n"
        "🕹️ Prueba comandos como:\n"
        "• /Ultimas_Pelis\n"
        "• /anime\n"
        "• /navidad\n"
        "• /retro\n\n"
        "✨ ¡Luces, cámara... interacción!"
    )
    await update.message.reply_markdown(mensaje)






