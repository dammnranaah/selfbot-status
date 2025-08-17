# 🎛️ SelfBot Status Changer

A simple Discord selfbot script that allows you to **change your Discord status** dynamically.
Supports **Playing, Streaming, Listening, and Watching** activity types.

> ⚠️ **Warning:** Selfbots violate Discord’s Terms of Service. Use at your own risk. This script is for educational purposes only.

---

## ✨ Features

* Change your Discord status on the fly.
* Supports multiple activity types:

  * `playing` → Shows "Playing \<text>"
  * `streaming` → Shows "Streaming \<text>" with Twitch URL
  * `listening` → Shows "Listening to \<text>"
  * `watching` → Shows "Watching \<text>"
* Alias command: `mode` works the same as `status`.
* Simple authorization check to restrict usage.

---

## 📦 Commands

### `e!status <activity_type> <text>`

* Updates your Discord status.
* Example usage:

```
e!status playing Minecraft
e!mode streaming Live Coding Session
e!status listening Lo-fi Beats
e!status watching YouTube Tutorials
```

---

## ⚙️ Setup

1. **Clone or download the script**

```bash
git clone https://github.com/dammnranaah/selfbot-status.git
cd selfbot-status
```

2. **Install dependencies**

```bash
pip install discord.py
```

3. **Add your token** in the code:

```python
bot.run('YOUR_TOKEN_BABY')
```

4. **Run the script**

```bash
python selfbot_status.py
```

---

## ⚡ How it Works

* The bot logs in with your Discord token.
* When you use `e!status` or `e!mode`, it checks the activity type and updates your Discord presence.
* Includes a basic authorization function (`is_authorized`) to control who can run the command.

---
