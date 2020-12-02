import keyboard
import MyThread

potok1 = MyThread.MyThread('accept')
potok1.start()
keyboard.add_hotkey('Enter + plus', potok1.swich_flag)
keyboard.add_hotkey('Enter + -', potok1.deth_Thread)

print("Оно живое и хочет принимать игры!!!\n")
print("Коротко обо мне:")
print("\t (Enter и +) - временно приостановить/включить принятие игр. При звапуске принятие в режиме вкл")
print("\t (Enter и -) - завершить выполнение программы\n")

keyboard.wait('Enter + -')
potok1.join()
if not potok1.is_alive():
    print("СМЭрТь")
