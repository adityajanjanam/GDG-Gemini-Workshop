Here’s an updated **README.md** that folds in the live‑demo link, cleans up a few headings, and keeps your friendly workshop vibe intact. Feel free to copy‑paste it straight into your repository.

````markdown
# 🤖 Chat App with Google Gemini API — GDG Workshop Project

This repo holds the source for a simple AI‑powered chat application built during the **“Build & Deploy a Chat App with Gemini API on Google Cloud”** workshop hosted by **GDG on Campus – Conestoga College**.

---

## 🚀 Workshop Highlights

- ✅ Built a basic **Chat App** with **Streamlit**  
- ✅ Integrated the **Google Gemini API** for AI‑generated responses  

---

## 🛠️ Tech Stack

| Purpose | Tech |
|---------|------|
| **Core Lang** | Python 🐍 |
| **UI** | Streamlit 📺 |
| **AI** | Google Gemini API 🤖 |
| **Hosting** | Google Cloud Run ☁️ |
| **Container** | Docker 🐳 |

---

## 📸 Live Demo

> 🌐 **Try it here →** [gdg‑gemini‑workshop.streamlit.app](https://gdg-gemini-workshop.streamlit.app/)

---

## 📦 Local Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/adityajanjanam/GDG-Gemini-Workshop.git
   cd GDG-Gemini-Workshop
````

2. **(Optional) Create a virtual env**

   ```bash
   python -m venv venv
   # macOS/Linux
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your Gemini API key**
   Create a `.env` file in the project root:

   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

5. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

## ☁️ Deployment Notes

The app is containerized via **Docker** and can be shipped to **Google Cloud Run** in a single command. See the `Dockerfile` and `cloudrun.md` (if added) for step‑by‑step deployment instructions.

---

## 🙌 Acknowledgements

Big thanks to **GDG Conestoga** and **@Anish Reddy** for organizing and guiding this lightning workshop!

---

## 📬 Connect

|                      |                                                                                    |
| -------------------- | ---------------------------------------------------------------------------------- |
| 🔗 LinkedIn          | [https://linkedin.com/in/janjanamaditya](https://linkedin.com/in/janjanamaditya)   |
| 🌐 Portfolio / Links | [https://adityajanjanam.com/adityajanjanam](https://adityajanjanam.com/)               |
| ☕ Buy Me a Coffee    | [https://buymeacoffee.com/adityajanjanam](https://buymeacoffee.com/adityajanjanam) |

---

> 🚧 **Workshop demo project** — fork away and add new features or a snazzy UI!

```

