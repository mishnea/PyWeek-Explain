def main(context):
    print(f"Hello World! ({context})")

main("run from outside if block")

if __name__ == "main":
    main("run from inside if block")