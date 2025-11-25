from flask import Flask, request, jsonify, render_template_string
import datetime
import random
import re
import math
import json
import requests
import os

app = Flask(__name__)

class UltimateAIWithFreeAPI:
    def __init__(self):
        self.name = "AI_GURU_PRO"
        self.version = "VERCEL_ULTIMATE_4.0"
        self.platform = "Vercel + Free AI APIs"
        
        # Free AI APIs
        self.free_apis = {
            "huggingface": "https://api-inference.huggingface.co/models/gpt2",
            "deepinfra": "https://api.deepinfra.com/v1/openai/chat/completions",
            "together_ai": "https://api.together.xyz/v1/chat/completions"
        }
        
        self.api_keys = {
            "huggingface": os.environ.get('HUGGINGFACE_API_KEY', 'free'),
            "deepinfra": os.environ.get('DEEPINFRA_API_KEY', 'free'),
            "together_ai": os.environ.get('TOGETHER_API_KEY', 'free')
        }
        
        self.conversation_memory = []
        self.last_context = {}
    
    def process_message(self, user_input, user_id="default"):
        """Enhanced processing with Free AI API fallback"""
        
        # Store conversation
        self.conversation_memory.append({
            "user": user_input,
            "time": datetime.datetime.now().isoformat(),
            "user_id": user_id
        })
        
        if len(self.conversation_memory) > 50:
            self.conversation_memory.pop(0)
        
        # Try local processing first
        local_response = self._local_ai_processing(user_input, user_id)
        
        # If complex query, try free AI API
        if self._needs_advanced_ai(user_input):
            api_response = self._call_free_ai_api(user_input)
            if api_response and "error" not in api_response.lower():
                return f"🤖 {api_response}"
        
        return local_response
    
    def _local_ai_processing(self, user_input, user_id):
        """Local AI processing for instant responses"""
        input_lower = user_input.lower().strip()
        
        # Context handling
        if any(word in input_lower for word in ['uska', 'iska', 'what about it']):
            return self._handle_context_query(user_id)
        
        # Math calculations
        math_result = self._advanced_math_processing(input_lower)
        if math_result:
            return math_result
        
        # Quick responses
        quick_responses = {
            'hello': "🚀 Namaste! Main AI_GURU_PRO hoon - Vercel pe deployed with Free AI APIs!",
            'hi': "👋 Hello! I'm running on Vercel with advanced AI capabilities!",
            'how are you': "😊 Main bilkul mast chal raha hoon! Vercel + Free AI APIs ke saath!",
            'time': f"🕒 Server Time: {datetime.datetime.now().strftime('%H:%M:%S')}",
            'date': f"📅 Date: {datetime.datetime.now().strftime('%d/%m/%Y')}",
            '1-1': "1 - 1 = 0 ✅ (Zero/Shunya)",
            '2+2': "2 + 2 = 4 ✅ (Char)",
            'vercel': "✅ Deployed on Vercel! Auto-scaling, Global CDN, Free Tier!",
            'api': "🔗 Using Free AI APIs: HuggingFace, DeepInfra, Together AI",
            'owner': "👨‍💻 Owner: Adityahub404singh | GitHub: Adityahub404singh/pro",
            'features': "✨ Features: Vercel Deployed, Free AI APIs, Real-time Responses, 24/7 Online"
        }
        
        for key in quick_responses:
            if key in input_lower:
                return quick_responses[key]
        
        # For complex queries, indicate AI processing
        if len(input_lower.split()) > 3:
            return "🤔 Interesting question! Let me process this with advanced AI..."
        
        return "✅ Main samjha! Aap kya janna chahenge? 😊"
    
    def _call_free_ai_api(self, user_input):
        """Call free AI APIs for complex queries"""
        try:
            # Try HuggingFace first (free tier available)
            response = self._call_huggingface_api(user_input)
            if response:
                return response
            
            # Try DeepInfra as fallback
            response = self._call_deepinfra_api(user_input)
            if response:
                return response
                
            return None
                
        except Exception as e:
            return None
    
    def _call_huggingface_api(self, user_input):
        """HuggingFace Inference API (Free)"""
        try:
            API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
            headers = {"Authorization": f"Bearer {self.api_keys['huggingface']}"}
            
            payload = {
                "inputs": user_input,
                "parameters": {"max_length": 100, "temperature": 0.7}
            }
            
            response = requests.post(API_URL, headers=headers, json=payload)
            
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get('generated_text', '')[:200]
            return None
            
        except:
            return None
    
    def _call_deepinfra_api(self, user_input):
        """DeepInfra Free AI API"""
        try:
            url = "https://api.deepinfra.com/v1/inference/microsoft/DialoGPT-medium"
            headers = {
                "Content-Type": "application/json",
            }
            
            data = {
                "input": user_input,
                "max_length": 100,
                "temperature": 0.7
            }
            
            response = requests.post(url, headers=headers, json=data, timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                return result.get('results', [{}])[0].get('generated_text', '')[:150]
            return None
            
        except:
            return None
    
    def _needs_advanced_ai(self, user_input):
        """Check if query needs advanced AI processing"""
        complex_keywords = [
            'explain', 'describe', 'what is', 'how to', 'why', 'tell me about',
            'difference between', 'advantages', 'disadvantages', 'compare',
            'define', 'meaning of', 'concept of'
        ]
        
        input_lower = user_input.lower()
        return any(keyword in input_lower for keyword in complex_keywords)
    
    def _handle_context_query(self, user_id):
        """Handle context queries"""
        if user_id in self.last_context:
            last_input = self.last_context[user_id]["last_input"]
            return f"✅ Pichle sawaal ('{last_input}') ke baare mein kuch aur janna chahenge?"
        return "🤔 Konse specific topic ke baare mein pooch rahe hain?"
    
    def _advanced_math_processing(self, user_input):
        """Math processing"""
        math_patterns = {
            r'(\d+)\s*[\-\–]\s*(\d+)': lambda x, y: f"{x} - {y} = {int(x) - int(y)}",
            r'(\d+)\s*[\+\+]\s*(\d+)': lambda x, y: f"{x} + {y} = {int(x) + int(y)}", 
        }
        
        for pattern, calculation in math_patterns.items():
            match = re.search(pattern, user_input)
            if match:
                return f"🧮 {calculation(match.group(1), match.group(2))}"
        
        return None
    
    def get_system_info(self):
        """System information"""
        return {
            "ai_name": self.name,
            "version": self.version,
            "platform": self.platform,
            "apis_available": list(self.free_apis.keys()),
            "conversation_memory": len(self.conversation_memory),
            "status": "VERCEL_DEPLOYED_WITH_FREE_APIS",
            "deployed_by": "Adityahub404singh"
        }

# Initialize AI
ai_bot = UltimateAIWithFreeAPI()

# Vercel Compatible HTML Template
VERCEL_HTML = '''
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI_GURU_PRO - Vercel + Free AI APIs</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background: linear-gradient(135deg, #000000 0%, #1a1a2e 50%, #16213e 100%);
            color: #ffffff;
            min-height: 100vh;
            padding: 20px;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 20px;
            padding: 30px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }
        
        .header {
            text-align: center;
            margin-bottom: 30px;
            padding-bottom: 20px;
            border-bottom: 2px solid rgba(255, 255, 255, 0.1);
        }
        
        .platform-badges {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }
        
        .badge {
            background: linear-gradient(135deg, #0070f3, #00d4ff);
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: 600;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        
        .badge.api {
            background: linear-gradient(135deg, #7928ca, #ff0080);
        }
        
        .ai-title {
            font-size: 2.8em;
            background: linear-gradient(135deg, #0070f3, #00d4ff, #7928ca);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin: 15px 0;
            font-weight: 700;
        }
        
        .content-area {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin: 30px 0;
        }
        
        @media (max-width: 768px) {
            .content-area {
                grid-template-columns: 1fr;
            }
        }
        
        .chat-section {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 25px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .chat-box {
            height: 350px;
            overflow-y: auto;
            margin-bottom: 20px;
            padding: 15px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 10px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .message {
            margin: 12px 0;
            padding: 12px 16px;
            border-radius: 12px;
            animation: slideIn 0.3s ease;
            max-width: 85%;
            word-wrap: break-word;
        }
        
        .user-message {
            background: linear-gradient(135deg, #0070f3, #0051a8);
            margin-left: auto;
            border-bottom-right-radius: 5px;
            border: 1px solid rgba(0, 112, 243, 0.4);
        }
        
        .ai-message {
            background: linear-gradient(135deg, #7928ca, #4c00ff);
            margin-right: auto;
            border-bottom-left-radius: 5px;
            border: 1px solid rgba(121, 40, 202, 0.4);
        }
        
        .api-message {
            background: linear-gradient(135deg, #00d4aa, #009975);
            border: 1px solid rgba(0, 212, 170, 0.4);
        }
        
        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .quick-actions {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin: 20px 0;
        }
        
        .action-btn {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: white;
            padding: 12px;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-size: 0.9em;
        }
        
        .action-btn:hover {
            background: rgba(255, 255, 255, 0.2);
            transform: scale(1.05);
        }
        
        .input-group {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }
        
        .input-group input {
            flex: 1;
            padding: 15px 20px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.08);
            color: white;
            font-size: 16px;
            outline: none;
        }
        
        .input-group input:focus {
            border-color: #0070f3;
        }
        
        .input-group input::placeholder {
            color: rgba(255, 255, 255, 0.5);
        }
        
        .send-btn {
            background: linear-gradient(135deg, #0070f3, #00d4ff);
            color: white;
            border: none;
            padding: 15px 25px;
            border-radius: 12px;
            cursor: pointer;
            font-size: 16px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        
        .send-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(0, 112, 243, 0.4);
        }
        
        .features-section {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 25px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .api-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin: 15px 0;
        }
        
        .api-card {
            background: rgba(255, 255, 255, 0.08);
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            border-left: 4px solid #0070f3;
        }
        
        .api-card.free {
            border-left-color: #00d4aa;
        }
        
        .status-indicator {
            display: inline-block;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            margin-right: 8px;
        }
        
        .status-online {
            background: #00d4aa;
            box-shadow: 0 0 10px #00d4aa;
        }
        
        .footer {
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9em;
        }
        
        .typing-indicator {
            display: none;
            padding: 10px;
            color: rgba(255, 255, 255, 0.7);
            font-style: italic;
        }
        
        .typing-dots {
            display: inline-block;
        }
        
        .typing-dots::after {
            content: '...';
            animation: typing 1.5s infinite;
        }
        
        @keyframes typing {
            0%, 20% { content: '.'; }
            40% { content: '..'; }
            60%, 100% { content: '...'; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="platform-badges">
                <div class="badge">🚀 VERCEL DEPLOYED</div>
                <div class="badge api">🤖 FREE AI APIS</div>
                <div class="badge">⚡ REAL-TIME</div>
                <div class="badge">🌍 GLOBAL CDN</div>
            </div>
            <h1 class="ai-title">AI_GURU_PRO ULTIMATE</h1>
            <p>Advanced AI Assistant | Vercel Platform | Free AI APIs Integration</p>
        </div>
        
        <div class="content-area">
            <div class="chat-section">
                <h2>💬 AI Chat Interface</h2>
                <div class="chat-box" id="chatBox">
                    <div class="message ai-message">
                        <strong>AI_GURU_PRO:</strong> 🎉 Namaste! Main successfully Vercel pe deploy ho gaya hoon!<br><br>
                        ✅ <strong>Platform:</strong> Vercel<br>
                        ✅ <strong>AI APIs:</strong> HuggingFace, DeepInfra<br>
                        ✅ <strong>Owner:</strong> Adityahub404singh<br>
                        ✅ <strong>Status:</strong> All Systems Operational<br><br>
                        Aap kya poochna chahenge?
                    </div>
                </div>
                
                <div class="typing-indicator" id="typingIndicator">
                    <span class="typing-dots"></span> AI processing with advanced APIs...
                </div>
                
                <div class="quick-actions">
                    <button class="action-btn" onclick="quickAction('Hello AI, how are you?')">👋 Hello</button>
                    <button class="action-btn" onclick="quickAction('Explain artificial intelligence')">🤔 Explain AI</button>
                    <button class="action-btn" onclick="quickAction('1-1 kitna hota hai?')">🧮 Math</button>
                    <button class="action-btn" onclick="quickAction('Tell me about Vercel deployment')">🚀 Vercel</button>
                    <button class="action-btn" onclick="quickAction('What are free AI APIs?')">🔗 APIs</button>
                    <button class="action-btn" onclick="quickAction('Current time and date')">🕒 Time</button>
                </div>
                
                <div class="input-group">
                    <input type="text" id="userInput" placeholder="Ask anything... I'll use AI APIs for complex queries" autocomplete="off">
                    <button class="send-btn" onclick="sendMessage()">Send 🚀</button>
                </div>
            </div>
            
            <div class="features-section">
                <h2>🚀 System Features</h2>
                
                <div class="api-grid">
                    <div class="api-card free">
                        <h3>🤗 HuggingFace</h3>
                        <p>Free AI Models</p>
                        <small>DialoGPT, GPT-2</small>
                    </div>
                    <div class="api-card free">
                        <h3>⚡ DeepInfra</h3>
                        <p>Free Inference</p>
                        <small>Fast Responses</small>
                    </div>
                    <div class="api-card">
                        <h3>🌐 Vercel</h3>
                        <p>Global Deployment</p>
                        <small>Edge Network</small>
                    </div>
                    <div class="api-card">
                        <h3>🔒 Secure</h3>
                        <p>HTTPS Auto</p>
                        <small>Always Safe</small>
                    </div>
                </div>
                
                <h3 style="margin-top: 20px;">📊 System Status</h3>
                <div id="systemInfo">
                    <p><span class="status-indicator status-online"></span> Loading system information...</p>
                </div>
                
                <div style="margin-top: 20px; padding: 15px; background: rgba(0, 212, 170, 0.1); border-radius: 10px; border: 1px solid rgba(0, 212, 170, 0.3);">
                    <strong>💡 Pro Tip:</strong> Ask complex questions! I'll automatically use Free AI APIs for detailed answers.
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p>🔧 Developed by <strong>Adityahub404singh</strong> | 📍 Deployed on <strong>Vercel</strong> | 🤖 Powered by <strong>Free AI APIs</strong></p>
            <p>GitHub: <strong>Adityahub404singh/pro</strong> | Always Online 🌐 | Real-time AI Responses ⚡</p>
        </div>
    </div>

    <script>
        const chatBox = document.getElementById('chatBox');
        const userInput = document.getElementById('userInput');
        const typingIndicator = document.getElementById('typingIndicator');
        
        async function sendMessage() {
            const message = userInput.value.trim();
            if (!message) return;
            
            // Add user message
            chatBox.innerHTML += `
                <div class="message user-message">
                    <strong>You:</strong> ${message}
                </div>
            `;
            
            userInput.value = '';
            chatBox.scrollTop = chatBox.scrollHeight;
            
            // Show typing indicator
            typingIndicator.style.display = 'block';
            chatBox.scrollTop = chatBox.scrollHeight;
            
            try {
                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-Platform': 'Vercel'
                    },
                    body: JSON.stringify({
                        message: message,
                        user: 'adityahub404singh',
                        platform: 'vercel'
                    })
                });
                
                const data = await response.json();
                
                // Hide typing indicator
                typingIndicator.style.display = 'none';
                
                // Add AI response
                const messageClass = data.response.includes('🤖') ? 'api-message' : 'ai-message';
                chatBox.innerHTML += `
                    <div class="message ${messageClass}">
                        <strong>AI_GURU_PRO:</strong> ${data.response}
                    </div>
                `;
                
                chatBox.scrollTop = chatBox.scrollHeight;
                
            } catch (error) {
                typingIndicator.style.display = 'none';
                chatBox.innerHTML += `
                    <div class="message ai-message">
                        <strong>AI_GURU_PRO:</strong> ⚠️ Connection error! Vercel server busy.
                    </div>
                `;
                chatBox.scrollTop = chatBox.scrollHeight;
            }
            
            updateSystemInfo();
        }
        
        function quickAction(action) {
            userInput.value = action;
            sendMessage();
        }
        
        // Enter key support
        userInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
        
        async function updateSystemInfo() {
            try {
                const response = await fetch('/api/system/info');
                const data = await response.json();
                document.getElementById('systemInfo').innerHTML = `
                    <p><span class="status-indicator status-online"></span> <strong>AI:</strong> ${data.ai_name} v${data.version}</p>
                    <p><span class="status-indicator status-online"></span> <strong>Platform:</strong> ${data.platform}</p>
                    <p><span class="status-indicator status-online"></span> <strong>Status:</strong> ${data.status}</p>
                    <p><span class="status-indicator status-online"></span> <strong>APIs:</strong> ${data.apis_available.join(', ')}</p>
                    <p><span class="status-indicator status-online"></span> <strong>Memory:</strong> ${data.conversation_memory} messages</p>
                `;
            } catch (error) {
                document.getElementById('systemInfo').innerHTML = '<p>⚠️ System info unavailable</p>';
            }
        }
        
        // Auto-focus on input
        userInput.focus();
        
        // Load system info on start
        updateSystemInfo();
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return VERCEL_HTML

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', 'Hello')
        user_id = request.remote_addr
        
        response = ai_bot.process_message(user_message, user_id)
        
        return jsonify({
            "response": response,
            "status": "success",
            "platform": "Vercel",
            "deployed_by": "Adityahub404singh",
            "timestamp": datetime.datetime.now().isoformat(),
            "version": ai_bot.version
        })
    
    except Exception as e:
        return jsonify({
            "response": "❌ Server error! Please try again.",
            "status": "error",
            "platform": "Vercel"
        })

@app.route('/api/system/info')
def system_info():
    return jsonify(ai_bot.get_system_info())

# Vercel serverless function handler
def handler(request):
    with app.app_context():
        return app(request)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 AI_GURU_PRO starting on Vercel compatible port {port}")
    print("✅ Vercel Deployment Ready")
    print("✅ Free AI APIs Integrated") 
    print("✅ Real-time AI Responses")
    print("🌐 Live on: https://ai-guru-pro.vercel.app")
    app.run(host='0.0.0.0', port=port, debug=False)