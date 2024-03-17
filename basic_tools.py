import nibabel as nib

def load_nifti_image(fpath):
    try:
        im = nib.load(fpath)
        data = im.get_fdata()
        return im, data
    except Exception as e:
        print("Error loading NIfTI image:", e)
        return None, None
    
def save_nifti_image(data, affine, outpath):
    try:
        im = nib.Nifti1Image(data, affine)
        nib.save(im, outpath)
        print("NIfTI image saved successfully.")
    except Exception as e:
        print("Error saving NIfTI image:", e)