from src.utils.image_utils import get_images_for_study_id
from src.utils import path
import os
import pandas as pd
import matplotlib.pyplot as plt


def display_images_for_study_id(study_id, train_or_test='train', n_cols=4, figwidth=15, height_per_row=4):
    """
    Plot all images for a given study_id
    Creates one figure per series_id showing all images

    Args:
        study_id (int): study_id of interest
        train_or_test (str): whether study id is in train or test set
        n_cols (int): number of columns in figure
        figwidth (float): width of figure
        height_per_row (float): height per row in figure

    Returns:
        None
    """
    data_dir = path.get_data_dir()
    train_series_descriptions = pd.read_csv(os.path.join(data_dir, 'train_series_descriptions.csv'))
    df_this_study_id = train_series_descriptions.query('study_id == @study_id')
    series_ids = df_this_study_id['series_id'].values

    image_dict = get_images_for_study_id(study_id, train_or_test=train_or_test)
    for series_id in series_ids:
        series_path = os.path.join(path.get_data_dir(), f"{train_or_test}_images", str(study_id), str(series_id))
        image_filenames = [im for im in os.listdir(series_path)]
        n_images = len(image_filenames)
        n_rows = (n_images + n_cols - 1) // n_cols

        fig, axs = plt.subplots(n_rows, n_cols, figsize=(figwidth, n_rows * height_per_row))
        axs = axs.flatten()  # Flatten the 2D array of axes to 1D for easier iteration

        for i in range(n_images):
            image = image_dict[series_id][i + 1]
            axs[i].imshow(image, cmap=plt.cm.gray)
            axs[i].axis('off')

        # Remove unused axes
        for i in range(n_images, len(axs)):
            fig.delaxes(axs[i])

        description = train_series_descriptions.query('study_id == @study_id and series_id == @series_id')['series_description'].iloc[0]
        fig.suptitle(f"study_id = {study_id}, description = {description}")
        fig.tight_layout()
        plt.subplots_adjust(wspace=0.01, hspace=0.01, top=0.95)