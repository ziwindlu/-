import tkinter as tk
import random
import time

class FloatingText:
    def __init__(self, root, text, color, font_size):
        self.root = root
        self.text = text
        self.color = color
        self.font_size = font_size
        self.label = tk.Label(root, text=text, fg=color, font=('微软雅黑', font_size))
        self.x = random.randint(0, root.winfo_width())
        self.y = random.randint(0, root.winfo_height())
        self.speed = random.uniform(1, 3)
        self.label.place(x=self.x, y=self.y)
        self.update()

    def update(self):
        self.y -= self.speed
        if self.y < -self.font_size * 2:
            self.y = self.root.winfo_height() + self.font_size * 2
            self.x = random.randint(0, self.root.winfo_width())
        self.label.place(x=self.x, y=self.y)
        self.root.after(20, self.update)

def create_floating_texts(root, texts, colors, font_sizes, count):
    floating_texts = []
    for _ in range(count):
        text = random.choice(texts)
        color = random.choice(colors)
        font_size = random.choice(font_sizes)
        floating_text = FloatingText(root, text, color, font_size)
        floating_texts.append(floating_text)
    return floating_texts

if __name__ == "__main__":
    root = tk.Tk()
    root.title("满屏飘字")
    root.attributes('-fullscreen', True)  # 全屏显示
    root.configure(bg='black')

    # 自定义文字内容
    love_texts = [
        "好好吃饭", "好好爱自己", "多喝热水", "我想你了",
        "照顾好自己", "保持好心情", "天冷了多穿衣服", "别熬夜"
    ]
    # 自定义颜色
    colors = ['#FF6B8B', '#87CEEB', '#98FB98', '#FFD700', '#EE82EE', '#FFA07A']
    # 自定义字体大小
    font_sizes = [12, 14, 16, 18]
    # 自定义文字数量
    text_count = 30

    create_floating_texts(root, love_texts, colors, font_sizes, text_count)

    root.mainloop()
