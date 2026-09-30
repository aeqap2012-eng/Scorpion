import sys
import time
import random


class ScorpionError(Exception):
    pass


class Scorpion:
    def __init__(self):
        self.vars = {}
        self.running = True

    def value(self, text):
        text = text.strip()

        if text in self.vars:
            return self.vars[text]

        if text == "true":
            return True

        if text == "false":
            return False

        if text == "nothing":
            return None

        if (text.startswith('"') and text.endswith('"')) or \
           (text.startswith("'") and text.endswith("'")):
            return text[1:-1]

        try:
            return int(text)
        except ValueError:
            pass

        try:
            return float(text)
        except ValueError:
            pass

        if "+" in text:
            parts = text.split("+")
            values = [self.value(part) for part in parts]

            if any(isinstance(v, str) for v in values):
                return "".join(str(v) for v in values)

            return sum(values)

        return text

    def condition(self, expression):
        operators = ["==", "!=", ">=", "<=", ">", "<"]

        for operator in operators:
            if operator in expression:
                left, right = expression.split(operator, 1)

                a = self.value(left)
                b = self.value(right)

                if operator == "==":
                    return a == b
                if operator == "!=":
                    return a != b
                if operator == ">":
                    return a > b
                if operator == "<":
                    return a < b
                if operator == ">=":
                    return a >= b
                if operator == "<=":
                    return a <= b

        return bool(self.value(expression))

    def execute(self, line):
        line = line.strip()

        if not line or line.startswith("#"):
            return

        if line.startswith("show "):
            print(self.value(line[5:]))
            return

        if line.startswith("set "):
            content = line[4:]

            if "=" not in content:
                raise ScorpionError("Use: set name = value")

            name, expression = content.split("=", 1)

            self.vars[name.strip()] = self.value(expression)
            return
        if line == "help":
            print("""
🦂 Scorpion Help
────────────────────────

show "text"       عرض نص
set name = value  إنشاء متغير
ask "question"   طلب إدخال
wait seconds      الانتظار
random min max    رقم عشوائي

repeat number     تكرار
when condition    شرط
otherwise         وإلا
end               نهاية كتلة

help              عرض المساعدة
exit              خروج

Example:
set name = "Hassan"
show "Hello " + name

repeat 3
    show "Scorpion!"
end
""")
            return
        if line.startswith("ask "):
            prompt = self.value(line[4:])
            return input(str(prompt))

        if line.startswith("wait "):
            seconds = self.value(line[5:])
            time.sleep(float(seconds))
            return

        if line.startswith("random "):
            parts = line[7:].split()

            if len(parts) != 2:
                raise ScorpionError(
                    "Use: random minimum maximum"
                )

            minimum = int(self.value(parts[0]))
            maximum = int(self.value(parts[1]))

            return random.randint(minimum, maximum)

        if line == "exit":
            self.running = False
            return

        raise ScorpionError(
            "Unknown command: " + line
        )

    def run(self, source):
        lines = source.splitlines()
        i = 0

        while i < len(lines) and self.running:

            line = lines[i].strip()

            if not line or line.startswith("#"):
                i += 1
                continue

            if line.startswith("repeat "):

                count = int(self.value(line[7:]))
                block = []

                i += 1

                while i < len(lines) and lines[i].strip() != "end":
                    block.append(lines[i])
                    i += 1

                for _ in range(count):
                    self.run("\n".join(block))

                i += 1
                continue

            if line.startswith("when "):

                condition = line[5:]
                true_block = []
                false_block = []

                i += 1
                otherwise = False

                while i < len(lines) and lines[i].strip() != "end":

                    current = lines[i].strip()

                    if current == "otherwise":
                        otherwise = True
                    elif otherwise:
                        false_block.append(lines[i])
                    else:
                        true_block.append(lines[i])

                    i += 1

                if self.condition(condition):
                    self.run("\n".join(true_block))
                else:
                    self.run("\n".join(false_block))

                i += 1
                continue

            try:
                result = self.execute(line)

                if result is not None:
                    print(result)

            except Exception as error:
                raise ScorpionError(
                    f"Line {i + 1}: {error}"
                )

            i += 1


def repl():
    interpreter = Scorpion()

    print("🦂 Scorpion Programming Language")
    print("Version 0.1.0")
    print('اكتب "exit" للخروج')
    print()

    while interpreter.running:
        try:
            line = input(">> ")

            if not line.strip():
                continue

            interpreter.execute(line)

        except KeyboardInterrupt:
            print("\nBye!")
            break

        except EOFError:
            print("\nBye!")
            break

        except Exception as error:
            print("Scorpion Error:", error)


def main():

    if len(sys.argv) == 2:

        filename = sys.argv[1]

        try:

            with open(
                filename,
                "r",
                encoding="utf-8"
            ) as file:

                source = file.read()

            interpreter = Scorpion()
            interpreter.run(source)

        except FileNotFoundError:

            print("Scorpion Error: file not found")

        except ScorpionError as error:

            print("Scorpion Error:", error)

        return

    repl()


if __name__ == "__main__":
    main()
