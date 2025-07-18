# RoastFusion 🔥

A hilarious Flask web app that randomly roasts users using public roast APIs!

## Features
- 🎲 Randomly selects from 3 different roast APIs
- 🔥 Fun, animated interface with Bootstrap styling
- ⚡ AJAX-powered "Roast Me Again" button
- 🛡️ Fallback roasts if APIs are down
- 📱 Mobile-responsive design

## APIs Used
1. **Evil Insult Generator** - Creative insults and roasts
2. **Yo Momma API** - Classic "yo momma" jokes
3. **FOAAS** - Professional-grade roasts (with mild profanity)

## Installation & Setup

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Quick Start
1. **Clone or download** this file (`roast_fusion.py`)

2. **Install dependencies:**
   ```bash
   pip install flask requests
   ```

3. **Run the app:**
   ```bash
   python roast_fusion.py
   ```

4. **Open your browser** and go to:
   ```
   http://localhost:5000
   ```

### Alternative Installation (using virtual environment)
```bash
# Create virtual environment
python -m venv roast_env

# Activate virtual environment
# On Windows:
roast_env\\Scripts\\activate
# On macOS/Linux:
source roast_env/bin/activate

# Install dependencies
pip install flask requests

# Run the app
python roast_fusion.py
```

## How It Works
1. **Homepage loads** with a random roast from one of the 3 APIs
2. **Click "Roast Me Again"** to get a new roast via AJAX
3. **APIs are tried randomly** - if one fails, it tries the others
4. **Fallback roasts** are used if all APIs are down

## Customization
- **Add new APIs:** Add new functions similar to `get_evil_insult()`
- **Modify styling:** Edit the CSS in the `HTML_TEMPLATE` string
- **Add more fallback roasts:** Expand the `fallback_roasts` list
- **Change port:** Modify the `port` parameter in `app.run()`

## Troubleshooting
- **Port already in use?** Change `port=5000` to another port like `port=5001`
- **APIs not working?** The app will use fallback roasts automatically
- **Import errors?** Make sure Flask and requests are installed: `pip install flask requests`

## Warning ⚠️
This app fetches content from roast/insult APIs. Content may include mild profanity and roasts. Use responsibly and consider your audience!

## License
Free to use and modify for personal/educational purposes.

---
**Happy Roasting! 🔥**
"""