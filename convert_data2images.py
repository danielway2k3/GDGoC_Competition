import os
import fitz  
import io
from PIL import Image

images_path = './data/images/'
os.makedirs(images_path + 'train', exist_ok=True)
os.makedirs(images_path + 'test', exist_ok=True)
images_train_folder = images_path + 'train'
images_test_folder = images_path + 'test'

data_path = './data'

def main():
    # Function to convert PDF to image using PyMuPDF
    def convert_pdf_to_image(pdf_path, dpi=300):
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)
        
        # Get the first page
        first_page = pdf_document[0]
        
        # Set the rendering resolution (zoom factor based on DPI)
        zoom = dpi / 72  # 72 is the base DPI for PDF
        mat = fitz.Matrix(zoom, zoom)
        
        # Get the pixmap (rendered image)
        pix = first_page.get_pixmap(matrix=mat, alpha=False)
        
        # Convert to PIL image
        img_data = pix.tobytes("jpeg")
        img = Image.open(io.BytesIO(img_data))
        
        # Close the PDF document
        pdf_document.close()
        
        return img

    # Duyệt qua các thư mục trong data_path
    for sub_names in os.listdir(data_path):
        sub_path = os.path.join(data_path, sub_names)

        # Kiểm tra nếu `sub_names` là thư mục "train"
        if sub_names == 'train' and os.path.isdir(sub_path):
            train_path = sub_path

            # Duyệt tiếp trong `train_path`
            for sub in os.listdir(train_path):
                sub_folder_path = os.path.join(train_path, sub)

                # Kiểm tra nếu `sub` là thư mục "PDF"
                if sub == 'PDF' and os.path.isdir(sub_folder_path):
                    pdf_data_path = sub_folder_path

                    # Duyệt tất cả file trong `pdf_data_path`
                    for file in os.listdir(pdf_data_path):
                        file_path = os.path.join(pdf_data_path, file)
                        image = convert_pdf_to_image(file_path, dpi=200)
                        image_filename = os.path.splitext(file)[0] + '.jpg'
                        image.save(os.path.join(images_train_folder, image_filename), "JPEG")
                        print(f"Processed train file: {file}")
        
        # Neu la tap test
        elif sub_names == 'test' and os.path.isdir(sub_path):
            test_path = sub_path

            # Duyệt tiếp trong `test_path`
            for sub in os.listdir(test_path):
                sub_folder_path = os.path.join(test_path, sub)
                
                # Check if sub is the "PDF" folder
                if sub == 'PDF' and os.path.isdir(sub_folder_path):
                    pdf_data_path = sub_folder_path
                    
                    # Duyệt tất cả file trong `pdf_data_path`
                    for file in os.listdir(pdf_data_path):
                        file_path = os.path.join(pdf_data_path, file)
                        image = convert_pdf_to_image(file_path, dpi=200)
                        image_filename = os.path.splitext(file)[0] + '.jpg'
                        image.save(os.path.join(images_test_folder, image_filename), "JPEG")
                        print(f"Processed test file: {file}")

if __name__ == '__main__':
    main()
    print('Data preprocessing completed.')