import tkinter as tk
from tkinter import scrolledtext
from transformer import transform_swiftui_colors

def transform_code(event=None):
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    input_code = input_text.get("1.0", tk.END)
    
    transformed = transform_swiftui_colors(input_code)
    
    output_text.insert(tk.END, transformed)
    output_text.config(state=tk.DISABLED)


def copy_output():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END))
    root.update()

def on_enter_button(event): event.widget.config(bg="#3a3a3a")
def on_leave_button(event): event.widget.config(bg="#2b2b2b")
def on_enter_label(event): event.widget.config(fg="#ffffff")
def on_leave_label(event): event.widget.config(fg=fg_color)
def on_enter_output(event): output_text.config(bg="#2a2a2a")
def on_leave_output(event): output_text.config(bg=bg_color)

root = tk.Tk()
root.title("Code Color Transformer")
root.geometry("1130x620")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

bg_color = "#1e1e1e"
fg_color = "#dcdcdc"
font_code = ("Courier New", 12)
font_labels = ("Arial", 14, "italic")
font_footer = ("Arial", 10, "italic")

# Parent frame
main_frame = tk.Frame(root, bg=bg_color)
main_frame.pack(fill="both", expand=True, padx=30, pady=20)

# Labels
label_input = tk.Label(main_frame, text="your code :", bg=bg_color, fg=fg_color, font=font_labels)
label_input.grid(row=0, column=0, padx=(0, 20), pady=(0, 5), sticky="w")

label_output = tk.Label(main_frame, text="your transformed code :", bg=bg_color, fg=fg_color, font=font_labels)
label_output.grid(row=0, column=1, padx=(0, 0), pady=(0, 5), sticky="w")
label_output.bind("<Enter>", on_enter_label)
label_output.bind("<Leave>", on_leave_label)

# Text fields
input_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=50, height=25, font=font_code,
                                       bg=bg_color, fg=fg_color, insertbackground=fg_color)
input_text.grid(row=1, column=0, padx=(0, 20), pady=(0, 10))

output_text = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=50, height=25, font=font_code,
                                        bg=bg_color, fg=fg_color)
output_text.grid(row=1, column=1, padx=(0, 0), pady=(0, 10))
output_text.config(state=tk.DISABLED)
output_text.bind("<Enter>", on_enter_output)
output_text.bind("<Leave>", on_leave_output)

# Buttons frame (aligned bottom-right)
button_frame = tk.Frame(main_frame, bg=bg_color)
button_frame.grid(row=2, column=1, sticky="e", pady=(0, 5))

button_transform = tk.Button(button_frame, text="⚡ Transform", command=transform_code, font=("Arial", 12),
                             bg="#2b2b2b", fg=fg_color, activebackground="#3a3a3a")
button_transform.pack(side=tk.LEFT, padx=(0, 10))
button_transform.bind("<Enter>", on_enter_button)
button_transform.bind("<Leave>", on_leave_button)

button_copy = tk.Button(button_frame, text="📋 Copy", command=copy_output, font=("Arial", 12),
                        bg="#2b2b2b", fg=fg_color, activebackground="#3a3a3a")
button_copy.pack(side=tk.LEFT)
button_copy.bind("<Enter>", on_enter_button)
button_copy.bind("<Leave>", on_leave_button)

# Footer label
footer_label = tk.Label(main_frame, text="made by github.com/PierreHugo", bg=bg_color, fg=fg_color, font=font_footer)
footer_label.grid(row=3, column=0, columnspan=2, pady=(10, 0))

root.bind('<Control-Return>', transform_code)
root.bind('<Command-Return>', transform_code)

root.mainloop()