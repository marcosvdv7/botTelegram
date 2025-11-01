from telegram import Update  # type: ignore
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes  # type: ignore
import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Comando /Ultimas_Pelis
async def Ultimas_Pelis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get("https://tusitio.infinityfreeapp.com/bot.php")
        titulos = response.json()
        mensaje = "👋 Hola! Aquí tienes las últimas 10 películas añadidas:\n" + "\n".join(f"• {n}" for n in titulos)
    except Exception as e:
        mensaje = f"⚠️ Error al obtener las películas:\n{e}"
    await update.message.reply_text(mensaje)

# Comando /hola
async def hola(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = (
        "📼 Bienvenido a *TheCineVerse\\_bot* 🎥\\n"
        "Aquí puedes explorar películas, géneros y comandos temáticos.\\n\\n"
        "🕹️ Prueba comandos como:\\n"
        "• /Ultimas\\_Pelis\\n"
        "• /anime\\n"
        "• /navidad\\n"
        "• /retro\\n\\n"
        "✨ ¡Luces, cámara... interacción!"
    )
    await update.message.reply_markdown_v2(mensaje)

# Configuración del bot
if __name__ == '__main__':
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        raise ValueError("❌ BOT_TOKEN no está definido en el archivo .env")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("Ultimas_Pelis", Ultimas_Pelis))
    app.add_handler(CommandHandler("hola", hola))
    app.run_polling()
