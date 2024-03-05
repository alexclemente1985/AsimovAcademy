# This is a sample Python script.
from first_steps import first_steps
from streamlit_exec.top_100 import top_100


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def masterclass_python():
    print("aula masterclass python")
    index = int(input("Informe a aula escolhida: (1) Primeiros passos | (2) Primeiro app\n"))

    match(index):
        case 1:
            first_steps()
        case 2:
            top_100()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    masterclass_python()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
