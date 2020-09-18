import os, sys
import numpy as np
from fileutils import FileUtils
from metric import ConfusionMatrix
from sklearn.metrics import accuracy_score


utils = FileUtils()

num_classes = 9

def get_statistics(predict_folder):
    log_file = os.path.join(predict_folder, 'results.txt')

    classified_files = utils.get_files_with_ext(predict_folder, '.labels')
    cm_global = ConfusionMatrix(num_classes)



    for file in classified_files:
        ground_truth = file
        predicted = file.replace('.labels', '.npy')
        with open(log_file, 'a') as log:
            log.write("File: {}".format(predicted))
            log.close()


        gt_labels = np.loadtxt(ground_truth)
        pred_labels = np.loadtxt(predicted)

        cm = ConfusionMatrix(num_classes)
        cm.increment_from_list(gt_labels, pred_labels)
        cm.print_metrics(log_file)
        cm_global.increment_from_list(gt_labels, pred_labels)

    with open(log_file, 'a') as log:
        log.write("Global Stats")
        log.close()

    cm_global_1 = cm_global.confusion_matrix.astype('float') / cm_global.confusion_matrix.sum(axis=1)[:, np.newaxis]
    print(cm_global_1.diagonal())
    cm_global.print_metrics(log_file)


if __name__ == '__main__':
    input_folder = sys.argv[1]

    get_statistics(input_folder)