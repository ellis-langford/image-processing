import nibabel as nib

def load_nifti_image(fpath):
    """
    Load a NIfTI image from a filepath.
    
    Args:
        file_path (str): Path to the NIfTI file.

    Returns:
        nibabel.nifti1.Nifti1Image: NIfTI image object.
        numpy.ndarray: Image data.
    """
    try:
        im = nib.load(fpath)
        data = im.get_fdata()
        return im, data
    except Exception as e:
        print("Error loading NIfTI image:", e)
        return None, None
    
    
def save_nifti_image(data, affine, outpath):
    """
    Save a NIfTI image to a filepath.

    Args:
        data (numpy.ndarray): Image data.
        affine (numpy.ndarray): Affine transformation matrix.
        file_path (str): Path to save the NIfTI file.
    """
    try:
        im = nib.Nifti1Image(data, affine)
        nib.save(im, outpath)
        print("NIfTI image saved successfully.")
    except Exception as e:
        print("Error saving NIfTI image:", e)