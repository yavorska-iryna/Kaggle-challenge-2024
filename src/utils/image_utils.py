import pydicom
import pandas as pd
import os

from . import path

def get_images_for_study_id(study_id: int, train_or_test: str = 'train'):
    """
    Get all images for a given study id, return them in a dictionary
    Top level key = series_id
    Second level key = image_number (1 indexed)

    Args:
        study_id (int): study_id of interest
        train_or_test (str): whether study id is in train or test set

    Returns:
        dict
    """
    data_dir = path.get_data_dir()
    train_series_descriptions = pd.read_csv(os.path.join(data_dir, 'train_series_descriptions.csv'))
    df_this_study_id = train_series_descriptions.query('study_id == @study_id')
    series_ids = df_this_study_id['series_id'].values

    image_dict = {}
    for series_id in series_ids:
        series_path = os.path.join(path.get_data_dir(), f"{train_or_test}_images", str(study_id), str(series_id))
        image_dict[series_id] = {}
        n_images = len(os.listdir(series_path))
        for ii in range(1, n_images + 1):
            image_filename = f"{ii}.dcm"
            dicom_file = pydicom.dcmread(os.path.join(series_path, image_filename))
            image_dict[series_id][ii] = dicom_file.pixel_array
    
    return image_dict