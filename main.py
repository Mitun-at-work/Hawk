import os
from src.check_data import DataCheck
from src.check_image_simmilarities import ImageSimilarityChecker


if __name__ == '__main__' :
    # Data Duplicates Check
    dc = DataCheck()
    dc.run()
    
    # Run   
    similarity_checker = ImageSimilarityChecker(batch_size=25)
    # Get Simmilar Images
    similar_images = similarity_checker.get_similar_images()
