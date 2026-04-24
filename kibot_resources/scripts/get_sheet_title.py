import argparse
import os
import subprocess
import xml.etree.ElementTree as ET

def ensure_xml_exists(file_path):
    if os.path.exists(file_path):
        return True

    root, _ = os.path.splitext(file_path)
    sch_path = root + ".kicad_sch"
    if not os.path.exists(sch_path):
        return False

    try:
        subprocess.run(
            ["kicad-cli", "sch", "export", "python-bom", "-o", file_path, sch_path],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

    return os.path.exists(file_path)

def get_sheet_title(file_path, page_number, dots_number):
    try:
        if not ensure_xml_exists(file_path):
            print('.'*dots_number)
            return

        tree = ET.parse(file_path)
        root = tree.getroot()
        
        page_number = str(page_number)
        titles = []

        for sheet in root.findall(".//sheet"):
            number = sheet.get("number")
            if number == page_number:
                # Get the last part of the 'name' attribute after '/'
                name = sheet.get("name")
                title_block = sheet.find("title_block")
                title = title_block.find("title").text if title_block is not None else None
                if name:
                    titles.append(name.split("/")[-2 if name.endswith("/") else -1])
        
        if not titles:
            print('.'*dots_number)

        elif len(set(titles)) > 1:
            print("Conflicting page numbers")
        else:
            print(titles[0])
    except ET.ParseError:
        print("Error: Invalid XML format")
    except FileNotFoundError:
        print("Error: XML File not found")
    except Exception as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description="Get the sheet title based on page number from a KiCad XML file")
    parser.add_argument("-p", "--page-number", type=int, required=True, help="Page number to search")
    parser.add_argument("-f", "--file", type=str, required=True, help="Path to the schematic XML file")
    parser.add_argument("-d", "--dots-number", type=int, required=True, help="Number of dots for empty lines")

    args = parser.parse_args()
    get_sheet_title(args.file, args.page_number, args.dots_number)


if __name__ == "__main__":
    main()
