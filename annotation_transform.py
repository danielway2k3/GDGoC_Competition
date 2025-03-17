import os
import json

def convert_json_to_annotation(
    input_folder_path,
    output_txt,
    image_folder_path,
    ext_tail='.jpg'
):
    with open(output_txt, 'w', encoding="utf-8") as f_out:
        for file_name in os.listdir(input_folder_path):
            if file_name.endswith('.json'):
                with open(os.path.join(input_folder_path, file_name), "r", encoding="utf-8") as f_in:
                    data = json.load(f_in)
                    
                    # Get metadata
                    image_name = data['metadata'].get("page_hash", "")
                    
                    image_name = image_name + ext_tail
                    image_path = os.path.join(image_folder_path, image_name)
                    
                    
                    for cell in data.get("cells", []):
                        bbox = cell.get("bbox", [])
                        text = cell.get("text", [])
                        
                        if len(bbox) != 4:
                            continue
                    x_min, y_min, width, height = bbox
                    
                    x1, y1 = x_min, y_min
                    x2, y2 = x_min + width, y_min
                    x3, y3 = x_min + width, y_min + height
                    x4, y4 = x_min, y_min + height
                    
                    if not text:
                        text = '###'
                        
                    ann_dict = {
                        "transcription": text,
                        "points": [
                            [x1, y1],
                            [x2, y2],
                            [x3, y3],
                            [x4, y4]
                        ]
                    }
                    
                    annotations = []
                    annotations.append(ann_dict)
                    
                    f_out.write(f"{image_path}\t{json.dumps(annotations)}\n")

if __name__ == "__main__":
    input_folder = "./data/train/JSON/"
    output_txt = "./data/images/train_gt.txt"
    image_folder = "./data/train/images/train/"
    
    convert_json_to_annotation(input_folder, output_txt, image_folder)
    print("Convert JSON to annotation successfully!")