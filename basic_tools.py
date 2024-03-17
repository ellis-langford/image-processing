import nibabel as nib

def load_nifti_image(fpath):
    try:
        im = nib.load(fpath)
        data = im.get_fdata()
        return im, data
    except Exception as e:
        print("Error loading NIfTI image:", e)
        return None, None