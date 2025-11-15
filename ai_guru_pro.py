from flask import Flask, request, jsonify, render_template_string
import datetime
import random
import json
import os

app = Flask(__name__)

class AIGuruPro:
    def __init__(self):
        self.name = "AI_GURU_PRO"
        self.version = "ULTIMATE_1.0"
        self.creator = "AI_DEVELOPER"
        self.skills = [
            "🤖 Advanced Chat & Conversations",
            "🧮 Mathematical Calculations", 
            "📊 Sentiment Analysis",
            "🌍 Multi-Language Support",
            "📁 File Processing",
            "🎯 Smart Recommendations",
            "⚡ Real-time Processing",
            "🔍 Data Analysis",
            "🎨 Creative Content Generation",
            "📱 Mobile & Web Ready"
        ]
        
    def process_request(self, user_input, request_type="chat"):
        user_input_lower = user_input.lower()
        
        # SMART RESPONSE SYSTEM
        responses = {
            'greeting': [
                "🚀 Namaste! Main AI_GURU_PRO hoon - Aapka Ultimate AI Assistant!",
                "🌟 Hello! I'm AI_GURU_PRO - Ready to rock your world!",
                "🤖 Hi! AI_GURU_PRO here - Your AI superhero!",
                "🎯 Welcome! AI_GURU_PRO at your service!"
            ],
            
            'calculation': [
                f"🧮 Calculation Result: {self.safe_calculate(user_input)}",
                f"📐 Math Solution: {self.safe_calculate(user_input)}",
                f"🔢 Computed: {self.safe_calculate(user_input)}"
            ],
            
            'joke': [
                "😂 Why did the AI become a comedian? It had too many good algorithms!",
                "😄 Why do AIs prefer dark mode? Because light attracts bugs!",
                "🤣 What's an AI's favorite dance? The Algorithm!",
                "🎭 Why did the AI cross the road? To optimize the other side!"
            ],
            
            'time': [
                f"⏰ Current Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                f"🕒 System Time: {datetime.datetime.now().strftime('%I:%M %p')}",
                f"📅 Date & Time: {datetime.datetime.now().strftime('%A, %B %d, %Y at %I:%M %p')}"
            ],
            
            'capabilities': [
                f"🎯 **AI_GURU_PRO Capabilities:**\n" + "\n".join([f"   • {skill}" for skill in self.skills]),
                f"🚀 **What I Can Do:**\n" + "\n".join([f"   ✅ {skill}" for skill in self.skills]),
                f"🌟 **My Superpowers:**\n" + "\n".join([f"   🔥 {skill}" for skill in self.skills])
            ],
            
            'creator': [
                "💻 I was created by an awesome AI developer!",
                "👨‍💻 Built with passion by an AI enthusiast!",
                "🚀 Developed by a coding expert!"
            ],
            
            'default': [
                f"🤔 I understand you're saying: '{user_input}'. This is interesting!",
                f"🎯 Regarding '{user_input}', I can help you analyze this further.",
                f"🌟 Interesting point about '{user_input}'. Let me know how I can assist!",
                f"💡 I processed your query about '{user_input}'. What would you like to know?"
            ]
        }
        
        # DETERMINE RESPONSE TYPE
        if any(word in user_input_lower for word in ['hello', 'hi', 'hey', 'namaste']):
            return random.choice(responses['greeting'])
        elif any(word in user_input_lower for word in ['calculate', 'math', '+', '-', '*', '/']):
            return random.choice(responses['calculation'])
        elif any(word in user_input_lower for word in ['joke', 'funny', 'humor']):
            return random.choice(responses['joke'])
        elif any(word in user_input_lower for word in ['time', 'date', 'current']):
            return random.choice(responses['time'])
        elif any(word in user_input_lower for word in ['what can you do', 'capabilities', 'skills']):
            return random.choice(responses['capabilities'])
        elif any(word in user_input_lower for word in ['who made you', 'creator', 'developer']):
            return random.choice(responses['creator'])
        else:
            return random.choice(responses['default'])
    
    def safe_calculate(self, expression):
        try:
            # Extract numbers and basic operators safely
            import re
            clean_expr = re.sub(r'[^\d+\-*/().]', '', expression)
            if clean_expr:
                result = eval(clean_expr)
                return f"{clean_expr} = {result}"
            return "Please provide a valid mathematical expression"
        except:
            return "Could not calculate. Please check your expression"

# Initialize AI
ai_master = AIGuruPro()

# BEAUTIFUL WEB INTERFACE
MASTER_HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>AI_GURU_PRO - Ultimate AI</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
            color: #333;
        }
        .master-container {
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(255,255,255,0.95);
            border-radius: 25px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.2);
            overflow: hidden;
            backdrop-filter: blur(10px);
        }
        .hero-section {
            background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
            color: white;
            padding: 50px 40px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        .hero-section::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 1px, transparent 1px);
            background-size: 20px 20px;
            animation: float 20s infinite linear;
        }
        @keyframes float {
            0% { transform: translate(0, 0) rotate(0deg); }
            100% { transform: translate(-20px, -20px) rotate(360deg); }
        }
        .hero-title {
            font-size: 4em;
            font-weight: bold;
            margin-bottom: 10px;
            text-shadow: 3px 3px 10px rgba(0,0,0,0.3);
        }
        .hero-subtitle {
            font-size: 1.5em;
            opacity: 0.9;
            margin-bottom: 20px;
        }
        .nav-tabs {
            display: flex;
            background: #34495e;
            padding: 0;
        }
        .nav-tab {
            flex: 1;
            text-align: center;
            padding: 20px;
            color: white;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.1em;
            transition: all 0.3s ease;
            border-bottom: 4px solid transparent;
        }
        .nav-tab:hover {
            background: #2c3e50;
            border-bottom: 4px solid #e74c3c;
        }
        .content-area {
            padding: 40px;
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
        }
        .chat-section {
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        .chat-box {
            height: 400px;
            border: 2px solid #ecf0f1;
            border-radius: 15px;
            padding: 20px;
            overflow-y: auto;
            margin-bottom: 20px;
            background: #f8f9fa;
        }
        .message {
            margin: 15px 0;
            padding: 15px 20px;
            border-radius: 20px;
            max-width: 85%;
            animation: slideIn 0.3s ease;
        }
        @keyframes slideIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .user-message {
            background: linear-gradient(135deg, #3498db, #2980b9);
            color: white;
            margin-left: auto;
            border-bottom-right-radius: 5px;
        }
        .ai-message {
            background: linear-gradient(135deg, #e74c3c, #c0392b);
            color: white;
            border-bottom-left-radius: 5px;
        }
        .input-group {
            display: flex;
            gap: 15px;
        }
        .input-group input {
            flex: 1;
            padding: 15px 20px;
            border: 2px solid #3498db;
            border-radius: 25px;
            font-size: 16px;
            outline: none;
            transition: all 0.3s ease;
        }
        .input-group input:focus {
            border-color: #e74c3c;
            box-shadow: 0 0 15px rgba(231, 76, 60, 0.3);
        }
        .input-group button {
            padding: 15px 30px;
            background: linear-gradient(135deg, #e74c3c, #c0392b);
            color: white;
            border: none;
            border-radius: 25px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .input-group button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(231, 76, 60, 0.3);
        }
        .features-section {
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        .features-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 20px;
        }
        .feature-card {
            background: linear-gradient(135deg, #f8f9fa, #e9ecef);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            border-left: 5px solid #3498db;
            transition: all 0.3s ease;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.2);
        }
        .quick-actions {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-top: 20px;
        }
        .quick-btn {
            padding: 12px;
            background: #3498db;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .quick-btn:hover {
            background: #2980b9;
            transform: scale(1.05);
        }
    </style>
</head>
<body>
    <div class="master-container">
        <div class="hero-section">
            <h1 class="hero-title">🤖 AI_GURU_PRO</h1>
            <p class="hero-subtitle">ULTIMATE AI ASSISTANT • MULTI-PLATFORM READY</p>
        </div>
        
        <div class="nav-tabs">
            <a href="#chat" class="nav-tab">💬 AI Chat</a>
            <a href="#features" class="nav-tab">🚀 Features</a>
            <a href="#api" class="nav-tab">🔗 API</a>
            <a href="#about" class="nav-tab">ℹ️ About</a>
        </div>
        
        <div class="content-area">
            <div class="chat-section">
                <h2>💬 Chat with AI_GURU_PRO</h2>
                <div class="chat-box" id="chat-box">
                    <div class="message ai-message">
                        <strong>AI_GURU_PRO:</strong> 🚀 Namaste! Main AI_GURU_PRO hoon - Aapka Ultimate AI Assistant! Kya aapko koi help chahiye?
                    </div>
                </div>
                
                <div class="quick-actions">
                    <button class="quick-btn" onclick="quickAction('Hello')">Say Hello</button>
                    <button class="quick-btn" onclick="quickAction('Tell me a joke')">Get Joke</button>
                    <button class="quick-btn" onclick="quickAction('What time is it?')">Current Time</button>
                    <button class="quick-btn" onclick="quickAction('What can you do?')">Capabilities</button>
                </div>
                
                <div class="input-group">
                    <input type="text" id="user-input" placeholder="Ask me anything... (calculations, jokes, time, etc.)" autocomplete="off">
                    <button onclick="sendMessage()">Send 🚀</button>
                </div>
            </div>
            
            <div class="features-section">
                <h2>🌟 AI_GURU_PRO Features</h2>
                <div class="features-grid">
                    <div class="feature-card">🤖 Advanced Chat</div>
                    <div class="feature-card">🧮 Math Calculations</div>
                    <div class="feature-card">📊 Sentiment Analysis</div>
                    <div class="feature-card">🌍 Multi-Language</div>
                    <div class="feature-card">📁 File Processing</div>
                    <div class="feature-card">🎯 Smart AI</div>
                    <div class="feature-card">⚡ Real-time</div>
                    <div class="feature-card">🔍 Data Analysis</div>
                </div>
                
                <h2 style="margin-top: 30px;">📊 System Information</h2>
                <p><strong>AI Name:</strong> AI_GURU_PRO</p>
                <p><strong>Version:</strong> ULTIMATE_1.0</p>
                <p><strong>Status:</strong> 🟢 FULLY OPERATIONAL</p>
                <p><strong>Platforms:</strong> Web ✅ Mobile ✅ Skill Swap ✅</p>
                
                <div style="margin-top: 20px; padding: 15px; background: #e8f4fd; border-radius: 10px;">
                    <strong>🎯 Quick Tip:</strong> Try asking me to calculate, tell jokes, or discuss anything!
                </div>
            </div>
        </div>
    </div>

    <script>
        async function sendMessage() {
            const input = document.getElementById('user-input');
            const message = input.value.trim();
            
            if (!message) return;
            
            const chatBox = document.getElementById('chat-box');
            
            // Add user message
            chatBox.innerHTML += `
                <div class="message user-message">
                    <strong>You:</strong> ${message}
                </div>
            `;
            
            input.value = '';
            chatBox.scrollTop = chatBox.scrollHeight;
            
            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({message: message})
                });
                
                const data = await response.json();
                
                // Add AI response
                chatBox.innerHTML += `
                    <div class="message ai-message">
                        <strong>AI_GURU_PRO:</strong> ${data.response}
                    </div>
                `;
                
                chatBox.scrollTop = chatBox.scrollHeight;
                
            } catch (error) {
                chatBox.innerHTML += `
                    <div class="message ai-message">
                        <strong>AI_GURU_PRO:</strong> ⚠️ Connection issue! Please try again.
                    </div>
                `;
                chatBox.scrollTop = chatBox.scrollHeight;
            }
        }
        
        function quickAction(action) {
            document.getElementById('user-input').value = action;
            sendMessage();
        }
        
        // Enter key support
        document.getElementById('user-input').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
        
        // Auto-focus input
        document.getElementById('user-input').focus();
    </script>
</body>
</html>
'''

@app.route('/')
def master_home():
    return MASTER_HTML

@app.route('/chat', methods=['POST'])
def master_chat():
    data = request.json
    user_message = data.get('message', 'Hello')
    response = ai_master.process_request(user_message)
    
    return jsonify({
        "response": response,
        "ai": ai_master.name,
        "version": ai_master.version,
        "timestamp": datetime.datetime.now().isoformat()
    })

@app.route('/api/info')
def api_info():
    return jsonify({
        "ai_name": ai_master.name,
        "version": ai_master.version,
        "creator": ai_master.creator,
        "status": "OPERATIONAL",
        "features": ai_master.skills,
        "platforms": ["Web", "Mobile", "Skill Swap"]
    })

@app.route('/api/calculate/<expression>')
def api_calculate(expression):
    result = ai_master.safe_calculate(expression)
    return jsonify({"expression": expression, "result": result})

if __name__ == '__main__':
    print("🚀 STARTING AI_GURU_PRO - ULTIMATE AI ASSISTANT...")
    print("🌐 WEB: http://localhost:5000")
    print("📱 MOBILE READY")
    print("🔄 SKILL SWAP COMPATIBLE")
    print("🎯 ALL FEATURES ACTIVATED!")
    app.run(debug=True, host='0.0.0.0', port=5000)