import os
import logging

# logging.info(dir(os))
cwd = os.getcwd()
sn = input("what screen name do you want? ")
# sn = ""
if len(sn) == 0:
    sn = "testtest"
kv = open(cwd + "/internal/kv_empty.txt", "r")

exists = False
try:
    kv_new = open(cwd + "/libs/uix/kv/" + sn + "kv", "r")
    # exists = True
    logging.info("page already exists")
    kv_new.close()
except:
    logging.info("making new")
if exists == False:
    logging.info(exists)

    kv_new = open(cwd + "/libs/uix/kv/" + sn + "_screen.kv", "w")
    logging.info(kv)

    for line in kv.readlines():
        if "Screen>" in line:
            line = "<" + sn + "screen>\n"
        if 'name: "' in line:
            line = '    name: "' + sn + '"\n'
        kv_new.write(line)
    # logging.info(line)

    kv_new.close()

    "class AboutScreen(Screen):"

    py_new = open(cwd + "/libs/uix/baseclass/" + sn + "_screen.py", "w")
    py_new.write("from kivy.uix.screenmanager import Screen\n")
    py_new.write("class " + sn + "screen(Screen):\n")
    py_new.write("  pass")
    py_new.close()
    import json

    f = open("screens.json")
    data = json.load(f)
    logging.info(data)
    i = "from libs.uix.baseclass." + sn + "_screen import " + sn + "screen"
    o = sn + "screen()"
    k = "libs/uix/kv/" + sn + "_screen.kv"
    dd = {"import": i, "object": o, "kv": k}
    data[sn] = dd
    with open(cwd + "/internal/screens.json", "w") as ofile:
        json.dump(data, ofile, indent=4)
