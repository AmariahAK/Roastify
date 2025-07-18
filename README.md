# RoastFusion 🔥

> A hilarious Flask web app that serves up random roasts from multiple APIs - because sometimes you need the internet to tell you what's wrong with you!

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Fun Level](https://img.shields.io/badge/fun%20level-🔥🔥🔥🔥🔥-red.svg)

## 🎯 What is this?

RoastFusion is a fun web application that randomly roasts users by fetching content from various public roast APIs. Built with Flask and a sense of humor, it's perfect for when you need a good laugh or want to humble yourself (or your friends)!

**Made for fun, shared for free!** 🎉

## ✨ Features

- 🎲 **Multi-API Integration** - Randomly selects from 3 different roast APIs
- 🔥 **Animated Interface** - Beautiful Bootstrap styling with fire animations
- ⚡ **AJAX-Powered** - Smooth "Roast Me Again" button without page reloads
- 🛡️ **Bulletproof Fallbacks** - 20+ backup roasts if APIs are down
- 📱 **Mobile Responsive** - Looks great on all devices
- 🚀 **Zero Database** - Lightweight and easy to deploy

## 🌐 APIs Used

| API | Description | Sample |
|-----|-------------|--------|
| **Evil Insult Generator** | Creative insults and roasts | "You're not stupid, you just have bad luck thinking" |
| **Yo Momma API** | Classic "yo momma" jokes | "Yo momma is so..." |
| **FOAAS** | Professional-grade roasts | Creative professional insults |

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (comes with Python)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AmariahAK/Roastify.git
   cd Roastify
   ```

2. **Install dependencies**
   ```bash
   pip install flask requests
   ```

3. **Run the app**
   ```bash
   python roast_fusion.py
   ```

4. **Open your browser**
   ```
   http://localhost:5001
   ```

That's it! You're ready to get roasted! 🔥

### Alternative: Virtual Environment (Recommended)

```bash
# Create and activate virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install flask requests

# Run the app
python roast_fusion.py
```

## 🎮 How to Use

1. **Visit the homepage** - Get instantly roasted with a random insult
2. **Click "Roast Me Again"** - Get a new roast via smooth AJAX loading
3. **Share with friends** - Send them the link for some friendly roasting
4. **Enjoy responsibly** - Remember, it's all in good fun!

## 🛠️ Customization

Want to make it your own? Here's how:

### Add New APIs
```python
def get_your_api():
    """Get roast from Your Custom API"""
    try:
        response = requests.get('https://your-api.com/roast', timeout=5)
        data = response.json()
        return data.get('roast'), 'Your API Name'
    except:
        return None, None

# Add to the apis list in get_random_roast()
apis = [get_evil_insult, get_yo_momma, get_foaas, get_your_api]
```

### Modify Styling
Edit the CSS in the `HTML_TEMPLATE` string to change colors, animations, or layout.

### Add More Fallback Roasts
Expand the `fallback_roasts` list with your own creative insults.

### Change Port
Modify the `port` parameter in `app.run()`:
```python
app.run(debug=True, host='0.0.0.0', port=8080)
```

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| **Port already in use** | Change `port=5001` to another port like `port=8080` |
| **APIs not working** | App automatically uses fallback roasts |
| **Import errors** | Run `pip install flask requests` |
| **Permission denied** | Try running with `python3` instead of `python` |

## ⚠️ Content Warning

This app fetches content from roast/insult APIs that may include:
- Mild profanity
- Sarcastic humor
- Playful insults

**Use responsibly and consider your audience!** It's all meant to be lighthearted fun.

## 🤝 Contributing

Found a bug? Have a cool idea? Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b cool-feature`)
3. Commit your changes (`git commit -am 'Add cool feature'`)
4. Push to the branch (`git push origin cool-feature`)
5. Open a Pull Request

## 📝 License

This project is **completely free** to use, modify, and distribute! 

**MIT License** - do whatever you want with it:
- ✅ Use it commercially
- ✅ Modify it however you like
- ✅ Share it with friends
- ✅ Learn from the code
- ✅ Make it better

Just don't blame me if you get roasted too hard! 😄

## 🎉 Why I Made This

I built RoastFusion for fun during a weekend coding session. Sometimes you need a good laugh, and sometimes you need the internet to humble you. This app does both!

Feel free to use it, break it, improve it, or just enjoy getting roasted by APIs. Life's too short to take everything seriously! 🔥

## 🌟 Show Your Support

If you enjoyed this project:
- ⭐ Star this repository
- 🍴 Fork it and make it your own
- 📢 Share it with friends who need to be roasted
- 🐛 Report bugs or suggest features

---

**Made with ❤️ and a lot of ☕ by [AmariahAK](https://github.com/AmariahAK)**

*Remember: If you can't handle the heat, stay out of the RoastFusion! 🔥*
