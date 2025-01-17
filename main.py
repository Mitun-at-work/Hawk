import os
from src.check_data import DataCheck
from src.check_image_simmilarities import ImageSimilarityChecker


if __name__ == '__main__' :
    dc = DataCheck()
    dc.run()
    
    # Run   
    similarity_checker = ImageSimilarityChecker(batch_size=25)
    # similar_images = similarity_checker.get_similar_images()