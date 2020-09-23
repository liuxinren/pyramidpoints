import os, sys
import numpy as np
from fileutils import FileUtils
from metric import ConfusionMatrix
from sklearn.metrics import accuracy_score
from utils.ply import read_ply, write_ply
import ipdb

utils = FileUtils()

num_classes = 9

label_names = ['unclassified','ground','veg','cars','trucks','powerlines','fences/hedges','poles','buildings']

data_dir = '/home/vlab/Nina/SemanticSegmentation/KPConv/Data/NPM3D/test_points/'

def get_rgb_color_codes(preds):

    rgb = np.zeros((preds.shape[0],3))
    rgb[np.where(preds == 0)[0],:] = [0,0,100]
    rgb[np.where(preds == 1)[0],:] = [0,0,255]
    rgb[np.where(preds == 2)[0],:] = [0,153,0]
    rgb[np.where(preds == 3)[0],:] = [255,0,255]
    rgb[np.where(preds == 4)[0],:] = [255,0,255]
    rgb[np.where(preds == 5)[0],:] = [255,255,0]
    rgb[np.where(preds == 6)[0],:] = [255,128,0]
    rgb[np.where(preds == 7)[0],:] = [0,255,255]
    rgb[np.where(preds == 8)[0],:] = [255,0,0]

    rgb = rgb/255
    return rgb





def get_statistics(predict_folder):
    log_file = os.path.join(predict_folder, 'results.txt')

    classified_files = utils.get_files_with_ext(data_dir, '.ply')
    cm_global = ConfusionMatrix(num_classes)



    for file in classified_files:

        data = read_ply(file)
        gt_labels = data['class']
        base = os.path.basename(file)

        pred_file = os.path.join(predict_folder, base)
        pred_data = read_ply(pred_file)
        pred_labels = pred_data['preds']




        rgb = get_rgb_color_codes(pred_labels)
        results = {}
        results['x'] = data['x']
        results['y'] = data['y']
        results['z'] = data['z']
        results['red'] = rgb[:,0]
        results['green'] = rgb[:, 1]
        results['blue'] = rgb[:, 2]
        results['correct'] = np.equal(gt_labels, pred_labels).astype(np.int32)
        results['preds'] = pred_data['preds']
        results['ground_truth'] = data['class']

        test = [results['x'],results['y'],results['z'],results['red'],results['green'],results['blue'],results['correct'],results['preds'],results['ground_truth'] ]

        write_ply(pred_file.replace('.ply', '_color.ply'), test,['x', 'y', 'z', 'red', 'green', 'blue', 'correct', 'preds', 'ground_truth'] )






        predicted = file.replace('.labels', '.txt')
        with open(log_file, 'a') as log:
            log.write("File: {}".format(predicted))
            log.close()


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