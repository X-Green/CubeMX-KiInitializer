import tomlkit


def print_help():
    help_context = """
    Put source in "profiles/"
    """
    print(help_context)


def create_template():
    config_basic = tomlkit.table()
    config_basic["ioc_dir"] = ""
    config_basic["label_type"] = "hierarchical_label"

    config_addition = tomlkit.table()
    config_addition["decoupling_cap"] = False

    template_obj = tomlkit.document()
    template_obj["config_basic"] = config_basic
    template_obj["config_addition"] = config_addition

    template_s = tomlkit.dumps(template_obj)
    template_s += "\n--KiCAD_Source-- # Paste the MCU object in lines below"
    print(template_s)
    with open("profiles/template.toml", "w") as template_file:
        template_file.write(template_s)


def generate_target():
    pass


tasks = {
    "print help": print_help,
    "create template": create_template,
    "generate": generate_target()
}

if __name__ == "__main__":
    while True:
        print("Choose the task")
        task_keys = list(tasks.keys())
        for i in range(len(tasks)):
            print("[%d]%s" % (i, task_keys[i]))
        try:
            chosen_index = int(input())
            chosen_task = tasks[task_keys[chosen_index]]
        except IndexError:
            print("Index Error!")
            continue
        except ValueError:
            print("Value Error!")
            continue
        chosen_task()
