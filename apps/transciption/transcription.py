import re


def group_text(input_text: str) -> tuple[list[str], str]:
    """
    Group the input text into hours and a single paragraph.

    Parameters:
        input_text (str): The text to be processed.

    Returns:
        tuple[list[str], str]: A tuple containing two elements:
            - hours (list[str]): A list of time occurrences found in the text.
            - paragraph (str): The text with time removed, cleaned up, and grouped into a /
            single paragraph.
    """
    # Find all occurrences of time in the text
    hours = re.findall(pattern=r'\d+:\d+', string=input_text)

    # Remove time from the text
    cleaned_text = re.sub(pattern=r'\d+:\d+', repl='', string=input_text)

    # Remove extra line breaks and spaces
    cleaned_text = re.sub(pattern=r'\n+', repl=' ',
                          string=cleaned_text).strip()

    # Group all the text into a single paragraph
    paragraph = re.sub(pattern=r'\s+', repl=' ', string=cleaned_text)

    return hours, paragraph


def read_text(file_path: str) -> str:
    """
    Read text from a file.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content read from the file.
    """
    with open(file=file_path, mode='r', encoding='UTF-8') as file:
        return file.read()


def write_to_markdown(output_file: str, text: str) -> None:
    """
    Write the given `text` to a file specified by `output_file` in Markdown format.

    Args:
        output_file (str): The path to the file to write the text to.
        text (str): The text to write to the file.
    """
    # Group text into a single paragraph
    with open(file=output_file, mode='w', encoding='UTF-8') as file:
        file.write(text)


def main() -> None:
    """
    This function reads text from a file, groups the text into a single paragraph, /
    and writes the paragraph to a markdown file.

    Parameters:
        None

    Returns:
        None
    """
    try:
        # Read text from a file
        file_path = './apps/transciption/input_text.txt'
        input_text = read_text(file_path=file_path)

        # Group text into a single paragraph
        hours, paragraph = group_text(input_text=input_text)

        print("Hours found:", hours)
        print("Text grouped into a single paragraph:")
        print(paragraph)

        # Write the paragraph to a markdown file
        write_to_markdown(
            output_file='./apps/transciption/paragraph.md', text=paragraph)

        # Delete the content of the input file
        with open(file=file_path, mode='w', encoding='UTF-8') as file:
            file.truncate(0)
    except FileNotFoundError:
        print("Empty file: The input file is empty.")
    except IOError as e:
        print("IOError: ", str(object=e))


if __name__ == "__main__":
    main()
