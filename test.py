from dataServer import MainThread
import core
if __name__ == "__main__":
    main = MainThread()
    main.start()
  
    while True:
        if main.isAlive() == False:
            break