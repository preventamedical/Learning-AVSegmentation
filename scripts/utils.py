# Copyright (c) Yukun Zhou.
# All rights reserved.

def define_image_size(uniform, dataset):
    img_size = (0, 0)
    if uniform == 'True':
        img_size = (800, 800)
    else:
        if dataset == 'HRF-AV':
            img_size = (880, 592)
        elif dataset == 'DRIVE_AV':
            img_size = (592, 592)
        elif dataset == 'LES-AV':
            img_size = (800, 720)

    return img_size
