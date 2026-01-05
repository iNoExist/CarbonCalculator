import customtkinter as ctk

# Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Calculation function
def calculate():
    try:
        kwh = float(kwh_entry.get() or 0)
        hours = float(hours_entry.get() or 0)
        total = (kwh * 0.233) + (hours * 0.05)
        result_label.configure(text=f"Estimated CO₂: {total:.2f} kg/month", text_color="#4CAF50")
    except ValueError:
        result_label.configure(text="⚠ Please enter valid numbers.", text_color="#FF5252")

# App window
app = ctk.CTk()
app.title("Carbon Footprint Calculator")
app.geometry("500x400")
app.resizable(False, False)

# Header
header = ctk.CTkLabel(app, text="Carbon Footprint Calculator", font=("Arial", 22, "bold"))
header.pack(pady=20)

# Electricity input
ctk.CTkLabel(app, text="Electricity usage (kWh/month)", font=("Arial", 14)).pack(pady=(10,0))
kwh_entry = ctk.CTkEntry(app, placeholder_text="Enter kWh", font=("Arial", 12))
kwh_entry.pack(pady=10, ipadx=40, ipady=8)

# Hours input
ctk.CTkLabel(app, text="Computer / cloud usage (hours/month)", font=("Arial", 14)).pack(pady=(10,0))
hours_entry = ctk.CTkEntry(app, placeholder_text="Enter hours", font=("Arial", 12))
hours_entry.pack(pady=10, ipadx=40, ipady=8)

# Calculate button
ctk.CTkButton(app, text="Calculate CO₂", font=("Arial", 14, "bold"), command=calculate).pack(pady=20, ipadx=15, ipady=8)

# Results
result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
result_label.pack(pady=15)

app.mainloop()

