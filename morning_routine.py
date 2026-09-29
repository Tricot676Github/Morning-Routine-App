import tkinter as tk
from PIL import Image, ImageTk

# ==========================
# TASKS
# ==========================

tasks = [
    {"text": "Brush Teeth", "image": "teeth.png"},
    {"text": "Get Dressed", "image": "clothes.png"},
    {"text": "Eat Breakfast", "image": "breakfast.png"}
]

current_task = 0

# ==========================
# RESTART TASKS
# ==========================

def restart_tasks():
    global current_task

    current_task = 0

    done_button.config(state="normal")

    confetti_label.pack_forget()

    restart_button.pack_forget()

    update_task()

# ==========================
# UPDATE TASK
# ==========================

def update_task():
    global photo

    if current_task < len(tasks):

        task = tasks[current_task]

        task_label.config(text=task["text"])

        image = Image.open(task["image"])
        image = image.resize((300, 300))

        photo = ImageTk.PhotoImage(image)

        image_label.config(image=photo)
        image_label.image = photo

        progress_label.config(
            text=f"Task {current_task + 1} of {len(tasks)}"
        )

    else:

        task_label.config(text="⭐ ALL DONE! ⭐")

        image_label.config(image="")

        progress_label.config(text="Great Job!")

        done_button.config(state="disabled")

        confetti_label.pack(pady=10)

        restart_button.pack(pady=20)
            

# ==========================
# COMPLETE TASK
# ==========================

def complete_task():
    global current_task

    current_task += 1

    update_task()

# ==========================
# WINDOW
# ==========================

root = tk.Tk()

root.title("Morning Routine")

root.geometry("900x700")

root.configure(bg="#BDE0FE")

# ==========================
# TITLE
# ==========================

title_label = tk.Label(
    root,
    text="MORNING ROUTINE",
    font=("Arial", 28, "bold"),
    bg="#BDE0FE"
)

title_label.pack(pady=20)

# ==========================
# IMAGE
# ==========================

image_label = tk.Label(
    root,
    bg="#BDE0FE"
)

image_label.pack(pady=10)

# ==========================
# TASK TEXT
# ==========================

task_label = tk.Label(
    root,
    text="",
    font=("Arial", 34, "bold"),
    bg="white",
    width=20,
    height=2
)

task_label.pack(pady=20)

# ==========================
# PROGRESS
# ==========================

progress_label = tk.Label(
    root,
    text="",
    font=("Arial", 20),
    bg="#BDE0FE"
)

progress_label.pack()

# ==========================
# DONE BUTTON
# ==========================

done_button = tk.Button(
    root,
    text="DONE ✓",
    font=("Arial", 14, "bold"),
    bg="green",
    fg="white",
    width=10,
    height=2,
    command=complete_task
)

done_button.pack(pady=20)

# ==========================
# START OVER BUTTON
# ==========================

restart_button = tk.Button(
    root,
    text="START OVER",
    font=("Arial", 14, "bold"),
    bg="blue",
    fg="white",
    width=12,
    height=2,
    command=restart_tasks
)
confetti_label = tk.Label(
    root,
    text="🎉 🎊 🎉\nCONGRATULATIONS!\n🎊 🎉 🎊",
    font=("Arial", 24, "bold"),
    bg="#BDE0FE",
    fg="purple"
)


# ==========================
# START PROGRAM
# ==========================

update_task()

root.mainloop()
