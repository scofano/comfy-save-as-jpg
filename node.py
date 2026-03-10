import os
import numpy as np
from PIL import Image

import folder_paths


class SaveImageJPG:
    def __init__(self):
        self.type = "output"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "filename_prefix": ("STRING", {
                    "default": "ComfyUI"
                }),
                "output_folder": ("STRING", {
                    "default": ""
                }),
                "quality": ("INT", {
                    "default": 95,
                    "min": 1,
                    "max": 100,
                    "step": 1
                }),
                "optimize": ("BOOLEAN", {
                    "default": True
                }),
            },
            "optional": {
                "caption": ("STRING", {
                    "forceInput": True
                }),
                "caption_file_extension": ("STRING", {
                    "default": ".txt"
                }),
            },
            "hidden": {
                "prompt": "PROMPT",
                "extra_pnginfo": "EXTRA_PNGINFO",
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("last_saved_file",)

    FUNCTION = "save_images"
    OUTPUT_NODE = True
    CATEGORY = "image/save"

    def save_images(
        self,
        images,
        filename_prefix="ComfyUI",
        output_folder="",
        quality=95,
        optimize=True,
        caption=None,
        caption_file_extension=".txt",
        prompt=None,
        extra_pnginfo=None,
    ):

        # Determine base output directory
        if output_folder:
            if os.path.isabs(output_folder):
                base_dir = output_folder
            else:
                base_dir = os.path.join(folder_paths.get_output_directory(), output_folder)
        else:
            base_dir = folder_paths.get_output_directory()

        os.makedirs(base_dir, exist_ok=True)

        full_output_folder, filename, counter, subfolder, filename_prefix = \
            folder_paths.get_save_image_path(
                filename_prefix,
                base_dir,
                images[0].shape[1],
                images[0].shape[0]
            )

        last_file = None

        for image in images:

            i = 255.0 * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))

            # JPG cannot contain alpha
            if img.mode == "RGBA":
                img = img.convert("RGB")

            file = f"{filename}_{counter:05}.jpg"
            file_path = os.path.join(full_output_folder, file)

            img.save(
                file_path,
                format="JPEG",
                quality=quality,
                optimize=optimize,
                subsampling=0
            )

            if caption:
                caption_path = os.path.join(
                    full_output_folder,
                    f"{filename}_{counter:05}{caption_file_extension}"
                )
                with open(caption_path, "w", encoding="utf-8") as f:
                    f.write(caption)

            last_file = file_path
            counter += 1

        return (last_file,)