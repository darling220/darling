import streamlit as st
import streamlit.components.v1 as components

# Set page configuration for a clean, full-screen look
st.set_page_config(
    page_title="Be My Valentine?",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject CSS to hide Streamlit's default header, footer, and margins
st.markdown("""
    <style>
        [data-testid="stHeader"] {display: none;}
        [data-testid="stAppViewBlockContainer"] {
            padding: 0rem;
            max-width: 100vw;
            height: 100vh;
        }
        footer {display: none;}
        #root > div:nth-child(1) > div > div > div > div > section > div {padding: 0;}
    </style>
""", unsafe_allow_html=True)

def main():
    # The complete HTML, CSS, and JS bundle
    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Grand+Hotel&family=Inter:wght@400;600;700&display=swap');

            :root {
                --primary: #ff4d6d;
                --primary-hover: #ff758f;
                --bg-gradient: linear-gradient(135deg, #fff5f7 0%, #fee2e2 100%);
                --card-bg: rgba(255, 255, 255, 0.75);
                --text-main: #2d3436;
            }

            body {
                background: var(--bg-gradient);
                height: 100vh;
                width: 100vw;
                margin: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                font-family: 'Inter', sans-serif;
                overflow: hidden;
                text-align: center;
            }

            .bg-heart {
                position: fixed;
                color: rgba(255, 77, 109, 0.1);
                user-select: none;
                z-index: -1;
            }

            .container {
                background: var(--card-bg);
                padding: 3rem 2rem;
                border-radius: 40px;
                box-shadow: 0 20px 50px rgba(0,0,0,0.05);
                backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.5);
                width: 500px;
                max-width: 90%;
                min-height: 450px;
                position: relative;
                z-index: 10;
                display: flex;
                flex-direction: column;
                justify-content: center;
                transition: all 0.5s ease;
            }

            h1 {
                font-family: 'Grand Hotel', cursive;
                font-size: 3.5rem;
                color: var(--primary);
                margin-top: 0;
                margin-bottom: 2rem;
                line-height: 1.2;
            }

            # .name-highlight {
            #     font-family: 'Inter', sans-serif;
            #     font-weight: 700;
            #     font-size: 2.2rem;
            #     display: block;
            #     margin-bottom: 0.5rem;
            #     letter-spacing: -0.5px;
            #     # color: var(--text-main);
            # }

            .buttons {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 10px;
                min-height: 80px;
                width: 100%;
            }

            .btn-wrapper {
                flex: 1;
                display: flex;
                justify-content: center;
                align-items: center;
            }

            .btn {
                padding: 14px 40px;
                font-size: 1.15rem;
                border: none;
                border-radius: 100px;
                cursor: pointer;
                transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275), background-color 0.3s, box-shadow 0.3s;
                font-weight: 600;
                letter-spacing: 0.5px;
                display: inline-block;
                white-space: nowrap;
            }

            #yesBtn {
                background-color: var(--primary);
                color: white;
                box-shadow: 0 10px 20px rgba(255, 77, 109, 0.3);
                z-index: 11;
                animation: pulse 2s infinite;
            }

            @keyframes pulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.05); box-shadow: 0 15px 30px rgba(255, 77, 109, 0.4); }
                100% { transform: scale(1); }
            }

            #noBtn {
                background-color: #f1f2f6;
                color: #57606f;
                position: relative;
                z-index: 1000;
                border: 1px solid rgba(0,0,0,0.05);
            }

            .success-message {
                display: none;
                flex-direction: column;
                align-items: center;
                animation: scaleUp 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
                position: relative;
                height: 100%;
            }

            @keyframes scaleUp {
                from { opacity: 0; transform: scale(0.8); }
                to { opacity: 1; transform: scale(1); }
            }

            .message-bubble {
                position: absolute;
                background: white;
                color: var(--primary);
                padding: 10px 20px;
                border-radius: 50px;
                font-weight: 600;
                font-size: 0.9rem;
                box-shadow: 0 10px 15px rgba(0,0,0,0.05);
                border: 1px solid #fee2e2;
                pointer-events: none;
                animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
                z-index: 5;
                white-space: nowrap;
            }

            @keyframes popIn {
                0% { transform: scale(0) rotate(-10deg); opacity: 0; }
                100% { transform: scale(1) rotate(0deg); opacity: 1; }
            }

            .falling-heart {
                position: fixed;
                top: -10vh;
                z-index: 1;
                animation: fall 3s linear forwards;
                color: var(--primary);
                pointer-events: none;
            }

            @keyframes fall {
                to { transform: translateY(110vh) rotate(360deg); }
            }

            #resetBtn {
                margin-top: 30px;
                background-color: transparent;
                border: 2px solid #ffb3c1;
                color: #ff758f;
                font-size: 0.85rem;
                padding: 10px 25px;
                opacity: 0.7;
                cursor: pointer;
                border-radius: 50px;
                transition: all 0.3s;
            }
        </style>
    </head>
    <body>
        <div class="bg-heart" style="top:10%; left:10%; font-size: 5rem;">❤️</div>
        <div class="bg-heart" style="bottom:20%; right:15%; font-size: 3rem;">💖</div>
        <div class="bg-heart" style="top:40%; right:5%; font-size: 4rem;">🌹</div>

        <div class="container" id="mainCard">
            <div id="content">
                <h1 id="question">
                    <span class="name-highlight">Nirma Yigam Maro</span>
                    will you be my valentine?
                </h1>
                <div class="buttons">
                    <div class="btn-wrapper">
                        <button class="btn" id="yesBtn" onclick="celebrate()">Yes!</button>
                    </div>
                    <div class="btn-wrapper">
                        <button class="btn" id="noBtn">No</button>
                    </div>
                </div>
            </div>

            <div id="success" class="success-message">
                <h1 style="margin-bottom: 0.5rem;">I knew it! 💖</h1>
                <p style="font-size: 1.1rem; color: #636e72; margin-bottom: 1.5rem;">You've made me the happiest person! 🌹</p>
                <div style="font-size: 4.5rem; margin-bottom: 10px;">🥰</div>
                <div id="messageContainer" style="position: relative; width: 100%; height: 120px;"></div>
                <button id="resetBtn" onclick="resetPage()">← Go back?</button>
            </div>
        </div>

        <script>
            const noBtn = document.getElementById('noBtn');
            const mainCard = document.getElementById('mainCard');
            const content = document.getElementById('content');
            const success = document.getElementById('success');
            const messageContainer = document.getElementById('messageContainer');
            
            let heartInterval, messageInterval;
            
            const messages = [
                        "Darling, are you down, down down down down...",
                        "You're amazing! ✨",
                        "Can't wait! 🥂",
                        "🎈",
                        "My favorite person 💖",
                        "Love you! ❤️",
                        "Darling, You're the best! 🌸",
                        "Forever & Always ♾️",
                        "My world! 🌍",
                        "Darling, I love you 💘",
                        "My Love, Study Hard 📚",
                        "Darling, Take care of yourself 🤍",
                        "Eat well 🍽️",
                        "Sleep well 😴",
                        "I miss you 💭",
                        "Washing Powder Nirma 🧺",
                        "Dood se safedi Nirma se aayi ✨",
                        "Rangin kapda bhi khil-khil jaye 🌈",
                        "Sabki pasand Nirma 💙",
                        "Washing Powder Nirma, Nirma! 🎵", "Darling, are you down, down down down down...",
                        "Darling, are you down, down down down down...",
            ];

            function moveButton() {
                noBtn.style.position = 'absolute';
                const cardRect = mainCard.getBoundingClientRect();
                const padding = 20;
                const maxX = cardRect.width - noBtn.offsetWidth - padding;
                const maxY = cardRect.height - noBtn.offsetHeight - padding;
                noBtn.style.left = (Math.random() * (maxX - padding) + padding) + 'px';
                noBtn.style.top = (Math.random() * (maxY - padding) + padding) + 'px';
            }

            noBtn.addEventListener('mouseover', moveButton);
            noBtn.addEventListener('touchstart', (e) => { e.preventDefault(); moveButton(); });

            function celebrate() {
                content.style.display = 'none';
                success.style.display = 'flex';
                heartInterval = setInterval(createHeart, 300);
                let msgIndex = 0;
                messageInterval = setInterval(() => {
                    spawnMessage(messages[msgIndex % messages.length]);
                    msgIndex++;
                }, 1200);
                spawnMessage(messages[0]);
            }

            function spawnMessage(text) {
                const bubble = document.createElement('div');
                bubble.className = 'message-bubble';
                bubble.innerText = text;
                bubble.style.left = (Math.random() * (messageContainer.offsetWidth - 150)) + 'px';
                bubble.style.top = (Math.random() * (messageContainer.offsetHeight - 40)) + 'px';
                messageContainer.appendChild(bubble);
                setTimeout(() => {
                    bubble.style.opacity = '0';
                    setTimeout(() => bubble.remove(), 500);
                }, 3000);
            }

            function resetPage() {
                clearInterval(heartInterval);
                clearInterval(messageInterval);
                location.reload(); 
            }

            function createHeart() {
                const heart = document.createElement('div');
                heart.classList.add('falling-heart');
                heart.innerHTML = ['❤️', '💖', '💕', '🌹'][Math.floor(Math.random() * 4)];
                heart.style.left = Math.random() * 100 + 'vw';
                heart.style.fontSize = Math.random() * 20 + 20 + 'px';
                document.body.appendChild(heart);
                setTimeout(() => heart.remove(), 4000);
            }
        </script>
    </body>
    </html>
    """
    
    # Render the HTML in Streamlit
    components.html(html_code, height=800, scrolling=False)

if __name__ == "__main__":
    main()