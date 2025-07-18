from flask import Flask, render_template_string, jsonify
import requests
import random
import json

app = Flask(__name__)

# HTML template with embedded CSS
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RoastFusion 🔥</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            font-family: 'Arial', sans-serif;
        }
        .roast-container {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
            padding: 40px;
            margin-top: 50px;
            backdrop-filter: blur(10px);
        }
        .roast-text {
            font-size: 1.4rem;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
            margin: 30px 0;
            padding: 20px;
            background: #f8f9fa;
            border-left: 5px solid #e74c3c;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }
        .fire-emoji {
            font-size: 3rem;
            animation: bounce 2s infinite;
        }
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-10px); }
            60% { transform: translateY(-5px); }
        }
        .roast-btn {
            background: linear-gradient(45deg, #e74c3c, #c0392b);
            border: none;
            color: white;
            padding: 15px 30px;
            font-size: 1.1rem;
            font-weight: bold;
            border-radius: 50px;
            transition: all 0.3s ease;
            box-shadow: 0 5px 15px rgba(231, 76, 60, 0.3);
        }
        .roast-btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(231, 76, 60, 0.4);
            background: linear-gradient(45deg, #c0392b, #a93226);
        }
        .api-source {
            font-size: 0.9rem;
            color: #6c757d;
            font-style: italic;
        }
        .loading {
            display: none;
        }
        .spinner-border {
            color: #e74c3c;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="roast-container">
                    <div class="text-center">
                        <h1 class="display-4 text-danger mb-4">
                            <span class="fire-emoji">🔥</span> RoastFusion <span class="fire-emoji">🔥</span>
                        </h1>
                        <p class="lead text-muted">Prepare to get roasted by the internet's finest insult APIs!</p>
                    </div>
                    
                    <div id="roast-content">
                        {% if roast %}
                            <div class="roast-text">
                                "{{ roast }}"
                            </div>
                            <div class="text-center api-source">
                                Source: {{ api_source }}
                            </div>
                        {% else %}
                            <div class="roast-text">
                                Click the button below to get roasted! 🔥
                            </div>
                        {% endif %}
                    </div>
                    
                    <div class="text-center mt-4">
                        <div class="loading">
                            <div class="spinner-border" role="status">
                                <span class="visually-hidden">Loading...</span>
                            </div>
                            <p class="mt-2">Getting your roast ready...</p>
                        </div>
                        <button id="roast-btn" class="btn roast-btn" onclick="getRoast()">
                            🔥 Roast Me Again! 🔥
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        function getRoast() {
            const loadingDiv = document.querySelector('.loading');
            const roastBtn = document.getElementById('roast-btn');
            const roastContent = document.getElementById('roast-content');
            
            // Show loading state
            loadingDiv.style.display = 'block';
            roastBtn.style.display = 'none';
            
            fetch('/api/roast')
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        roastContent.innerHTML = `
                            <div class="roast-text">
                                "${data.roast}"
                            </div>
                            <div class="text-center api-source">
                                Source: ${data.api_source}
                            </div>
                        `;
                    } else {
                        roastContent.innerHTML = `
                            <div class="roast-text text-danger">
                                Oops! Something went wrong. Even our roast APIs are having a bad day! 😅
                            </div>
                        `;
                    }
                })
                .catch(error => {
                    roastContent.innerHTML = `
                        <div class="roast-text text-danger">
                            Error loading roast. Try again! 🤔
                        </div>
                    `;
                })
                .finally(() => {
                    // Hide loading state
                    loadingDiv.style.display = 'none';
                    roastBtn.style.display = 'inline-block';
                });
        }
    </script>
</body>
</html>
"""

def get_evil_insult():
    """Get roast from Evil Insult Generator API"""
    try:
        response = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json', timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get('insult', 'You are magnificently average!'), 'Evil Insult Generator'
    except Exception as e:
        return None, None

def get_yo_momma():
    """Get roast from Yo Momma API"""
    try:
        response = requests.get('https://api.yomomma.info/', timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get('joke', 'Yo momma is so nice, she probably baked cookies for everyone!'), 'Yo Momma API'
    except Exception as e:
        return None, None

def get_foaas():
    """Get roast from FOAAS API"""
    try:
        headers = {'Accept': 'application/json'}
        response = requests.get('https://www.foaas.com/off/You/RoastFusion', headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get('message', 'Off with you, in the nicest way possible!'), 'FOAAS'
    except Exception as e:
        return None, None

def get_random_roast():
    """Get a random roast from one of the APIs"""
    apis = [get_evil_insult, get_yo_momma, get_foaas]
    
    # Shuffle the APIs to try them in random order
    random.shuffle(apis)
    
    for api_func in apis:
        roast, api_source = api_func()
        if roast:
            return roast, api_source
    
    # Fallback roast if all APIs fail
    fallback_roasts = [
    "You're like a cloud—when you disappear, it's a beautiful day.",
    "If I had a dollar for every smart thing you said, I'd be broke.",
    "Your code has more bugs than a rainforest.",
    "You bring everyone so much joy… when you leave the room.",
    "You have something on your chin... no, the third one down.",
    "You're like a try-except block—always catching feelings.",
    "You have the emotional range of a calculator.",
    "You're the human version of a 404 error.",
    "You're not stupid—you just have bad luck thinking.",
    "You're like a while loop with no exit condition: exhausting.",
    "If personality were a skill, you'd still be level 0.",
    "You're the reason they put instructions on shampoo.",
    "You debug like you live—hopeless and in denial.",
    "You have something on your mind? Must be lonely up there.",
    "You're proof that evolution can go in reverse.",
    "You're slower than a Python script running on a potato.",
    "Your roast immunity has expired. Proceed at your own risk.",
    "You're like a semicolon in Python—useless.",
    "You're not the dumbest person alive, but you better hope they don't die.",
    "Your ideas are like expired milk—bad and unsettling.",
    ]
 
    return random.choice(fallback_roasts), "RoastFusion Backup Collection"

@app.route('/')
def home():
    """Homepage - show initial roast"""
    roast, api_source = get_random_roast()
    return render_template_string(HTML_TEMPLATE, roast=roast, api_source=api_source)

@app.route('/api/roast')
def api_roast():
    """API endpoint for getting new roasts via AJAX"""
    roast, api_source = get_random_roast()
    return jsonify({
        'success': True,
        'roast': roast,
        'api_source': api_source
    })

if __name__ == '__main__':
    print("🔥 Starting RoastFusion...")
    print("🌐 Open your browser and go to: http://localhost:5001")
    print("⚠️  WARNING: This app contains roasts and insults - use responsibly!")
    app.run(debug=True, host='0.0.0.0', port=5001)
