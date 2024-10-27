import console
import config

if not config.PARENT_DIR_PATH.exists():
    import os
    cwd = os.getcwd()
    idx = cwd.find("欧拓图纸")
    if idx > -1:
        from pathlib import Path
        config.PARENT_DIR_PATH = Path(cwd[:idx+5])
        config.updaPath()
    else:
        import sys
        print('无法找到"欧拓图纸"文件夹')
        sys.exit()
else:
    config.updaPath()



import cli
import argparse

print = console.print


if __name__ == "__main__":
    print(f"[bold white]此TubePro日志分析程序由{config.AUTHOR}编写[bold white]")
    print(f"[bold white]版本号: {config.VERSION}[bold white]")
    print(f"[bold white]最后更新: {config.LASTUPDATED}[bold white]\n\n")
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-L", "--legacy", action="store_true")
    args = argParser.parse_args()
    if args.legacy:
        cli.cliStart()
        input("Press enter to proceed...")
    else:
        import gui
