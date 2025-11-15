from flask import Flask, request, jsonify
import datetime
import random

app = Flask(__name__)

class SkillSwapAI:
    def __init__(self):
        self.name = "SkillSwap AI Assistant"
        self.platform = "SkillSwap"
        self.skill_id = "AI_SKILLSWAP_ASSISTANT_001"
        
    def process_skill_request(self, user_input, user_context=None):
        input_lower = user_input.lower()
        
        # SkillSwap specific responses
        skill_responses = {
            'greeting': [
                "Namaste! I'm your SkillSwap AI buddy! Ready to exchange some skills? 🚀",
                "Hello! SkillSwap AI here! Let's make learning fun and free! 💫",
                "Hi there! Ready to teach what you know and learn what you don't? 🔥"
            ],
            'help': [
                "I can help you find skill partners, schedule sessions, and manage credits!",
                "Need help? I can assist with skill matching, credit system, and video calls!",
                "I'm here to make your SkillSwap experience amazing! What do you need help with?"
            ],
            'credit': [
                "1 hour teaching = 1 credit earned! 1 hour learning = 1 credit spent! Simple! 💰",
                "The credit system lets you teach to learn! Share your skills, gain new ones! 🔄",
                "Earn credits by teaching, spend them to learn! Your knowledge is currency! 🎯"
            ],
            'matching': [
                "I'll find you perfect skill partners! Coding for design, marketing for music - anything! 🤝",
                "Smart matching finds people who want what you teach and teach what you want! 💡",
                "Finding skill partners is easy! Tell me what you know and what you want to learn! 🎯"
            ],
            'benefits': [
                "100% FREE skill learning! Save thousands on courses! 💸",
                "Learn from college seniors and peers! Personal guidance! 👥",
                "Multiple skills = Better placements! Higher salary! 📈"
            ],
            'session': [
                "Schedule video calls, share files, learn live! It's like personal tutoring! 📹",
                "Live sessions with screen sharing! Learn practically, not just theoretically! 🛠️",
                "Video calls + chat + file sharing = Complete learning experience! 📱"
            ],
            'default': [
                f"On SkillSwap, '{user_input}' sounds interesting! Want to find someone to learn this with?",
                f"Great! '{user_input}' is a valuable skill! Ready to teach or learn this on SkillSwap?",
                f"Awesome! SkillSwap can help you with '{user_input}'! Let's find you a learning partner!"
            ]
        }
        
        # Check for keywords and return appropriate response
        if any(word in input_lower for word in ['hi', 'hello', 'hey', 'namaste']):
            return random.choice(skill_responses['greeting'])
        elif any(word in input_lower for word in ['help', 'assist', 'support']):
            return random.choice(skill_responses['help'])
        elif any(word in input_lower for word in ['credit', 'point', 'earn', 'spend']):
            return random.choice(skill_responses['credit'])
        elif any(word in input_lower for word in ['match', 'partner', 'find', 'connect']):
            return random.choice(skill_responses['matching'])
        elif any(word in input_lower for word in ['benefit', 'advantage', 'why', 'free']):
            return random.choice(skill_responses['benefits'])
        elif any(word in input_lower for word in ['session', 'video', 'call', 'meet']):
            return random.choice(skill_responses['session'])
        else:
            return random.choice(skill_responses['default'])

skill_ai = SkillSwapAI()

# SkillSwap API Endpoints
@app.route('/skillswap/chat', methods=['POST'])
def skillswap_chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        user_id = data.get('user_id', 'anonymous')
        
        response = skill_ai.process_skill_request(user_message)
        
        return jsonify({
            "success": True,
            "skill_id": skill_ai.skill_id,
            "skill_name": skill_ai.name,
            "response": response,
            "user_id": user_id,
            "timestamp": datetime.datetime.now().isoformat(),
            "platform": "SkillSwap"
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400

@app.route('/skillswap/info', methods=['GET'])
def skillswap_info():
    return jsonify({
        "success": True,
        "skill_id": skill_ai.skill_id,
        "name": skill_ai.name,
        "description": "AI Assistant for SkillSwap - Peer-to-Peer Skill Exchange Platform",
        "version": "2.0",
        "author": "Team SkillSwap",
        "features": [
            "Skill matching assistance",
            "Credit system explanation", 
            "Session scheduling help",
            "Platform guidance",
            "User support"
        ],
        "endpoints": {
            "chat": "/skillswap/chat",
            "info": "/skillswap/info"
        },
        "status": "active"
    })

@app.route('/skillswap/suggest_skills', methods=['POST'])
def suggest_skills():
    data = request.json
    user_skills = data.get('user_skills', [])
    
    skill_suggestions = {
        'coding': ['web development', 'python', 'app development'],
        'design': ['graphic design', 'ui/ux', 'video editing'],
        'marketing': ['digital marketing', 'content writing', 'social media'],
        'music': ['guitar', 'piano', 'music production'],
        'language': ['english', 'spanish', 'japanese']
    }
    
    suggestions = []
    for skill in user_skills:
        if skill in skill_suggestions:
            suggestions.extend(skill_suggestions[skill])
    
    return jsonify({
        "success": True,
        "suggested_skills": suggestions[:5]  # Top 5 suggestions
    })

@app.route('/skillswap/calculate_credits', methods=['POST'])
def calculate_credits():
    data = request.json
    teaching_hours = data.get('teaching_hours', 0)
    learning_hours = data.get('learning_hours', 0)
    current_credits = data.get('current_credits', 0)
    
    new_credits = current_credits + teaching_hours - learning_hours
    
    return jsonify({
        "success": True,
        "teaching_hours": teaching_hours,
        "learning_hours": learning_hours,
        "current_credits": current_credits,
        "new_credits": new_credits,
        "message": f"After this exchange, you'll have {new_credits} credits!"
    })

if __name__ == '__main__':
    print("🚀 SkillSwap AI Assistant Started Successfully!")
    print("📍 Local: http://localhost:5002/skillswap/chat")
    print("📍 Info: http://localhost:5002/skillswap/info")
    print("🤖 AI is ready to assist SkillSwap users!")
    app.run(debug=True, host='0.0.0.0', port=5002)