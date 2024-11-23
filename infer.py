import argparse
# import torch
# import segmentation_models_pytorch as smp
# import cv2
# import numpy as np
# import albumentations as A
# from albumentations.pytorch.transforms import ToTensorV2

# val_transform = A.Compose([
#     A.Normalize(mean=(0.485, 0.456, 0.406),std=(0.229, 0.224, 0.225)),
#     ToTensorV2(),
# ])

# color_dict= {0: (0, 0, 0),
#              1: (255, 0, 0),
#              2: (0, 255, 0)}

# def mask_to_rgb(mask, color_dict):
#     output = np.zeros((mask.shape[0], mask.shape[1], 3))

#     for k in color_dict.keys():
#         output[mask==k] = color_dict[k]

#     return np.uint8(output)   

train_size = 256

def infer(image_path, train_size=train_size):
    # checkpoint = torch.load('/kaggle/working/model.pth')
    # model = smp.UnetPlusPlus(
    # encoder_name="resnet34",        
    # encoder_weights="imagenet",     
    # in_channels=3,                  
    # classes=3     
    # )
    # model.load_state_dict(checkpoint['model'])
    # device = torch.device('cuda' if torch.cuda.is_available() else "cpu")
    # model.to(device)
    # model.eval()
    # ori_img = cv2.imread(image_path)
    # ori_img = cv2.cvtColor(ori_img, cv2.COLOR_BGR2RGB)
    # ori_w = ori_img.shape[0]
    # ori_h = ori_img.shape[1]
    # img = cv2.resize(ori_img, (train_size, train_size))
    # transformed = val_transform(image=img)
    # input_img = transformed["image"]
    # input_img = input_img.unsqueeze(0).to(device)
    # with torch.no_grad():
    #     output_mask = model.forward(input_img).squeeze(0).cpu().numpy().transpose(1,2,0)
    # mask = cv2.resize(output_mask, (ori_h, ori_w))
    # mask = np.argmax(mask, axis=2)
    # mask_rgb = mask_to_rgb(mask, color_dict)
    # mask_rgb = cv2.cvtColor(mask_rgb, cv2.COLOR_RGB2BGR)
    # cv2.imwrite("prediction", mask_rgb)
    with open('output.txt', 'w') as f:
        f.write(f'{image_path} + {train_size}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Infer semantic segmentation on an image")
    parser.add_argument('--image_path', type=str, required=True, help="Path to the input image")
    args = parser.parse_args()
    infer(
        image_path=args.image_path,
    )