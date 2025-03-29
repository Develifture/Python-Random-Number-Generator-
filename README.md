# 🎯 Python Random Number Generator  

A simple and user-friendly **Random Number Generator** built with **PyQt5**. This application allows users to generate a random number between **1 and 1000** with the click of a button. Additionally, it includes a **dark mode toggle** for better usability.  

---

## ✨ Features  

✅ **Generate Random Numbers** – Click a button to generate a random number between **1 and 1000**.  
✅ **Dark Mode Support** – Toggle between light and dark themes for a better user experience.  
✅ **Minimalist UI** – A clean, easy-to-use graphical interface using **PyQt5**.  
✅ **Cross-Platform** – Works on **Windows, macOS, and Linux**.  

---

## 🛠️ Requirements  

Ensure you have the following installed before running the application:  

### ✅ System Requirements  
- **Operating System:** Windows, macOS, or Linux  
- **Python Version:** **Python 3.7+** (Recommended: **Python 3.10+**)  
- **Memory:** At least **512MB RAM** (minimal usage)  
- **Storage:** Less than **10MB**  

### ✅ Python Dependencies  
The application requires the **PyQt5** library for the graphical user interface.  

- Install dependencies using **pip**:  
  ```bash
  pip install PyQt5
  ```

---

## 🚀 Installation & Running  

Follow these steps to clone and run the project:  

### 1⃣ Clone the Repository  
```bash
git clone https://github.com/Develifture/Python-Random-Number-Generator-.git
cd Python-Random-Number-Generator
```

### 2⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

*(If you don’t have a `requirements.txt`, manually install `PyQt5` as shown in the previous step.)*  

### 3⃣ Run the Application  
```bash
python main.py
```

---

## 🖥️ Usage Instructions  

1. Open the application.  
2. Click the **"Generate Random Number"** button to get a random number.  
3. Toggle **"Dark Mode"** for a different theme.  
4. Enjoy generating numbers! 🎉  

---

## 🛠️ Customization  

### 🎨 Modify the UI Theme  
- The **default theme** is **light mode**.  
- Click the **"Toggle Dark Mode"** button to switch between themes.  
- You can edit the styles in `set_theme()` function inside `main.py`.  

---

## 🐞 Troubleshooting  

### ❓ PyQt5 Installation Issues  
If you get an error when installing PyQt5, try:  
```bash
pip install --upgrade pip
pip install PyQt5
```

### ❓ Application Not Opening  
- Ensure you are using **Python 3.7+**  
- Check if PyQt5 is installed:  
  ```bash
  python -c "import PyQt5; print(PyQt5.__version__)"
  ```

### ❓ GUI Issues (Scaling, Fonts)  
- Try running with:  
  ```bash
  python main.py --style=Fusion
  ```

---

## 🌟 License  

This project is **open-source** and free to use under the **MIT License**.  

---

## 👤 Author  

- **GitHub:** [Develifture](https://github.com/Develifture)  
- **Project Repository:** [Python-Random-Number-Generator](https://github.com/Develifture/Python-Random-Number-Generator-)  

---

### ⭐ If you found this useful, give it a **star** on GitHub! ⭐  
