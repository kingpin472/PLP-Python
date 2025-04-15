def file_handler(file, output_file):
    try:
        with open(file, 'r') as infile:
            content = infile.read()

        #convert text to uppercase
        modified_content = content.upper()

        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Successfully wrote modified content to '{output_file}'.")

    except FileNotFoundError:
        print(f"File '{file}' not found.")
    except PermissionError:
        print(f"Permission denied when accessing '{file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    input_file = input("Enter the name of the file to read: ").strip()
    output_file = input("Enter the name of the file to write the modified content: ").strip()

    file_handler(input_file, output_file)


if __name__ == "__main__":
    main()
