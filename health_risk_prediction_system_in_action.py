import tkinter as tk
from tkinter import messagebox

# Medical risk logic
def predict_health_risk(age, bmi, bp, glucose):
    obesity = bmi >= 30
    hypertension = bp >= 140
    diabetes = glucose >= 126

    high_risk = obesity or hypertension or diabetes

    return obesity, hypertension, diabetes, high_risk


# Button click handler
def check_risk():
    try:
        age = int(age_entry.get())
        bmi = float(bmi_entry.get())
        bp = int(bp_entry.get())
        glucose = int(glucose_entry.get())

        obesity, hypertension, diabetes, high_risk = predict_health_risk(age, bmi, bp, glucose)

        result = f"""
        Obesity Risk: {"YES" if obesity else "NO"}
        Hypertension Risk: {"YES" if hypertension else "NO"}
        Diabetes Risk: {"YES" if diabetes else "NO"}

        Overall High Risk: {"YES" if high_risk else "NO"}
        """

        if high_risk:
            result += "\n\nRecommendation: Medical & lifestyle intervention required."
        else:
            result += "\n\nRecommendation: Patient is in healthy range."

        messagebox.showinfo("Health Risk Report", result)

    except:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")


# GUI Window
root = tk.Tk()
root.title("Health Risk Prediction System")
root.geometry("400x350")

tk.Label(root, text="Health Risk Prediction", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="BMI").pack()
bmi_entry = tk.Entry(root)
bmi_entry.pack()

tk.Label(root, text="Systolic Blood Pressure").pack()
bp_entry = tk.Entry(root)
bp_entry.pack()

tk.Label(root, text="Fasting Glucose").pack()
glucose_entry = tk.Entry(root)
glucose_entry.pack()

tk.Button(root, text="Check Health Risk", command=check_risk, bg="green", fg="white").pack(pady=20)

root.mainloop()
