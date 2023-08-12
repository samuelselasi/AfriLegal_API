#!/usr/bin/python3
import json

def extract_chapter_titles(json_path, output_file):
    with open(json_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    extracted_titles = []

    if "document" in data and "section" in data["document"]:
        for section in data["document"]["section"]:
            if "content" in section:
                section_content = section["content"]
                if isinstance(section_content, list):
                    for item in section_content:
                        if isinstance(item, str):
                            extracted_titles.append(item)

    with open(output_file, "w", encoding="utf-8") as output:
        output.write("\n".join(extracted_titles))

if __name__ == "__main__":
    json_path = "./jsons/Ghana_1996.json"
    output_file = "./chapters/Ghana_1996.txt"

    extract_chapter_titles(json_path, output_file)
    print("Chapter titles extracted and saved to", output_file)
