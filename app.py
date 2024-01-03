import tkinter as tk
from tkinter import messagebox


class TicketSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("購票系統")

        self.ticket_label = tk.Label(master, text="請選擇座位號碼和票種，並輸入購票數量：")
        self.ticket_label.pack()

        self.seat_label = tk.Label(master, text="座位號碼：")
        self.seat_label.pack()

        self.seat_entry = tk.Entry(master)
        self.seat_entry.pack()

        self.type_label = tk.Label(master, text="票種（一般/優待）：")
        self.type_label.pack()

        self.type_var = tk.StringVar()
        self.type_regular = tk.Radiobutton(
            master, text="一般", variable=self.type_var, value="regular"
        )
        self.type_regular.pack()

        self.type_concession = tk.Radiobutton(
            master, text="優待", variable=self.type_var, value="concession"
        )
        self.type_concession.pack()

        self.ticket_entry_label = tk.Label(master, text="購票數量：")
        self.ticket_entry_label.pack()

        self.ticket_entry = tk.Entry(master)
        self.ticket_entry.pack()

        self.buy_button = tk.Button(master, text="購票", command=self.buy_tickets)
        self.buy_button.pack()

    def buy_tickets(self):
        try:
            seat_number = self.seat_entry.get()
            ticket_type = self.type_var.get()
            num_tickets = int(self.ticket_entry.get())

            price_per_ticket = (
                1990 if ticket_type == "regular" else 1690
            )  # Example prices
            total_price = num_tickets * price_per_ticket

            if num_tickets > 0:
                messagebox.showinfo(
                    "購票成功",
                    f"成功購買 {num_tickets} 張票！\n"
                    f"座位號碼：{seat_number}\n"
                    f"票種：{'一般' if ticket_type == 'regular' else '優待'}\n"
                    f"總價：{total_price}元",
                )
            else:
                messagebox.showwarning("購票失敗", "購票數量必須大於零！")

        except ValueError:
            messagebox.showerror("錯誤", "請輸入有效的數字。")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicketSystem(root)
    root.mainloop()
