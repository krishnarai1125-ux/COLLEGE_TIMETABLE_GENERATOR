import tkinter as tk
from tkinter import ttk, messagebox
import random
import csv
from tkinter import filedialog

# Global lists for days and times
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
times = [
    "09:00-10:00", "10:00-11:00", "11:00-11:15", 
    "11:15-12:15", "12:15-01:15", "01:15-02:00", 
    "02:00-03:00", "03:00-04:00"
]

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Timetable Generator")
        self.root.geometry("1000x700")

        # variables
        self.courses = [] # list to store course details
        self.labels = {} # to store grid labels
        
        # Main layout
        self.pane = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
        self.pane.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Left side for inputs
        self.frame_in = ttk.Frame(self.pane, width=250)
        self.pane.add(self.frame_in, weight=1)
        
        # inputs
        ttk.Label(self.frame_in, text="Subject Name:").pack(pady=5)
        self.ent_sub = ttk.Entry(self.frame_in)
        self.ent_sub.pack(fill=tk.X, padx=5)
        
        ttk.Label(self.frame_in, text="Teacher Name:").pack(pady=5)
        self.ent_prof = ttk.Entry(self.frame_in)
        self.ent_prof.pack(fill=tk.X, padx=5)
        
        ttk.Label(self.frame_in, text="Room No:").pack(pady=5)
        self.ent_room = ttk.Entry(self.frame_in)
        self.ent_room.pack(fill=tk.X, padx=5)
        
        ttk.Label(self.frame_in, text="Lectures per Week:").pack(pady=5)
        self.ent_count = ttk.Entry(self.frame_in)
        self.ent_count.insert(0, "3")
        self.ent_count.pack(fill=tk.X, padx=5)
        
        # buttons
        self.btn_add = ttk.Button(self.frame_in, text="Add Subject", command=self.add_sub)
        self.btn_add.pack(pady=10, fill=tk.X, padx=5)
        
        self.lst_box = tk.Listbox(self.frame_in, height=15)
        self.lst_box.pack(pady=5, fill=tk.BOTH, padx=5)
        
        self.btn_gen = ttk.Button(self.frame_in, text="Generate Table", command=self.process)
        self.btn_gen.pack(pady=10, fill=tk.X, padx=5)
        
        # Right side for output
        self.frame_out = ttk.Frame(self.pane)
        self.pane.add(self.frame_out, weight=4)
        
        # container for grid with black background for lines
        self.grid_frame = tk.Frame(self.frame_out, bg="black")
        self.grid_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # export button at bottom
        ttk.Button(self.frame_out, text="Save as CSV", command=self.save_csv).pack(pady=5)

        # color list
        self.clrs = ['#FFC0C0', '#C0FFC0', '#C0C0FF', '#FFFFC0', '#C0FFFF', '#FFC0FF']

    def add_sub(self):
        s = self.ent_sub.get()
        p = self.ent_prof.get()
        r = self.ent_room.get()
        c = self.ent_count.get()
        
        if s == "" or p == "" or r == "" or c == "":
            messagebox.showerror("Error", "Fill all fields please")
            return
            
        # add to list
        self.courses.append({
            'sub': s,
            'prof': p,
            'room': r,
            'cnt': int(c),
            'clr': self.clrs[len(self.courses) % 6]
        })
        self.lst_box.insert(tk.END, f"{s} ({p}) - {c}/wk")
        
        # clear fields
        self.ent_sub.delete(0, tk.END)
        self.ent_prof.delete(0, tk.END)

    def process(self):
        # main logic to generate timetable
        self.final_sched = {} 
        
        all_blocks = []
        for c in self.courses:
            for i in range(c['cnt']):
                all_blocks.append(c)
                
        random.shuffle(all_blocks)
        
        solved = False
        for attempt in range(50):
            if self.try_fit(all_blocks):
                solved = True
                break
            random.shuffle(all_blocks)
            
        if not solved:
            messagebox.showwarning("Failed", "Could not fit everything perfectly. Try removing some classes.")
        
        self.draw_grid()

    def try_fit(self, blocks):
        self.final_sched = {}
        occupied = {} 
        
        for d in range(len(days)):
            for t in range(len(times)):
                occupied[(d,t)] = []

        for blk in blocks:
            assigned = False
            
            options = []
            for d in range(len(days)):
                for t in range(len(times)):
                    if "11:00" in times[t] or "01:15" in times[t]:
                        continue
                    options.append((d,t))
            
            random.shuffle(options)
            
            for (d, t) in options:
                if (d, t) in self.final_sched:
                    continue
                    
                self.final_sched[(d,t)] = blk
                assigned = True
                break
            
            if not assigned:
                return False
                
        return True

    def draw_grid(self):
        # clear old grid
        for w in self.grid_frame.winfo_children():
            w.destroy()
            
        # config columns
        self.grid_frame.columnconfigure(0, weight=1)
        for i in range(len(times)):
            self.grid_frame.columnconfigure(i+1, weight=1)
            
        # FIX: Config rows so they stretch to fill the page
        # Row 0 is header, Rows 1-5 are Days
        for r in range(len(days) + 1):
            self.grid_frame.rowconfigure(r, weight=1)

        # Headers
        tk.Label(self.grid_frame, text="Time/Day", bg="lightgray", width=10, height=2).grid(row=0, column=0, padx=1, pady=1, sticky="nsew")
        
        for i in range(len(times)):
            t_str = times[i].replace("-", "\n")
            tk.Label(self.grid_frame, text=t_str, bg="lightgray", font=("Arial", 8)).grid(row=0, column=i+1, padx=1, pady=1, sticky="nsew")
            
        # Rows
        for r in range(len(days)):
            # Day label
            tk.Label(self.grid_frame, text=days[r], bg="lightgray", font=("Arial", 9, "bold")).grid(row=r+1, column=0, padx=1, pady=1, sticky="nsew")
            
            for c in range(len(times)):
                # check for break
                if "11:00" in times[c]:
                    lbl = tk.Label(self.grid_frame, text="BREAK", bg="gray")
                    lbl.grid(row=r+1, column=c+1, padx=1, pady=1, sticky="nsew")
                    continue
                if "01:15" in times[c]:
                    lbl = tk.Label(self.grid_frame, text="LUNCH", bg="gray")
                    lbl.grid(row=r+1, column=c+1, padx=1, pady=1, sticky="nsew")
                    continue
                    
                # get data
                if (r, c) in self.final_sched:
                    data = self.final_sched[(r,c)]
                    txt = f"{data['sub']}\n{data['prof']}\n(R-{data['room']})"
                    color = data['clr']
                    
                    lbl = tk.Label(self.grid_frame, text=txt, bg=color, font=("Arial", 8), wraplength=80)
                    lbl.grid(row=r+1, column=c+1, padx=1, pady=1, sticky="nsew")
                else:
                    # empty slot
                    tk.Label(self.grid_frame, text="-", bg="white").grid(row=r+1, column=c+1, padx=1, pady=1, sticky="nsew")

    def save_csv(self):
        f = filedialog.asksaveasfilename(defaultextension=".csv")
        if f:
            with open(f, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Day"] + times)
                for r in range(len(days)):
                    row = [days[r]]
                    for c in range(len(times)):
                        if (r,c) in self.final_sched:
                            d = self.final_sched[(r,c)]
                            row.append(f"{d['sub']} ({d['room']})")
                        else:
                            row.append("--")
                    writer.writerow(row)
            messagebox.showinfo("Done", "Saved!")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()