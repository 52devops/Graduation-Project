#!/usr/bin/env python

'''
face detection using haar cascades

USAGE:
    facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''

# Python 2/3 compatibility
# from __future__ import print_function

import cv2
from Intelligent.My_Pro.video import create_capture
import os
import sys, getopt
from Intelligent.My_Pro.common import clock, draw_str


# cv2.createca
class face_det():
    def detect(self,img, cascade):
        rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                         flags=cv2.CASCADE_SCALE_IMAGE)
        if len(rects) == 0:
            return []
        rects[:,2:] += rects[:,:2]           #得到图片的起始点和终点
        return rects

    def draw_rects(self,img, rects, color):
        for x1, y1, x2, y2 in rects:
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)


    def To_start(self):
        args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
        try:
            video_src = video_src[0]
        except:
            video_src = 0
        args = dict(args)
        cascade_fn = args.get('--cascade', "./haarcascades/haarcascade_frontalface_alt.xml")
        nested_fn  = args.get('--nested-cascade', "./haarcascades/haarcascade_eye.xml")

        cascade = cv2.CascadeClassifier(cascade_fn)
        nested = cv2.CascadeClassifier(nested_fn)

        cam = create_capture(video_src, fallback='synth:bg=./lena.jpg:noise=0.05')
        count = 0
        time = 0
        dirname = os.getcwd()
        while True:
            count += 1
            ret, img = cam.read()
            # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # gray = cv2.equalizeHist(gray)

            # t = clock()
            # rects = self.detect(gray, cascade)
            rects = self.detect(img, cascade)
            vis = img.copy()
            self.draw_rects(vis, rects, (0, 255, 0))
            if not nested.empty():
                for x1, y1, x2, y2 in rects:
                    # roi = gray[y1:y2, x1:x2]
                    roi = img[y1:y2, x1:x2]
                    if count == 30:
                        # print("%s\\face_data\\%s.jpg"%(dirname,time))
                        # cv2.imwrite("%s\\face_data\\%s.jpg"%(dirname,time),gray)
                        cv2.imwrite("%s\\face_data\\%s.jpg"%(dirname, time),img)
                        count = 0
            time += 1
            #         roi = gray[y1:y2, x1:x2]
                    # vis_roi = vis[y1:y2, x1:x2]
                    # subrects = detect(roi.copy(), nested)
                    # draw_rects(vis_roi, subrects, (255, 0, 0))
            # dt = clock() - t
            #
            # draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))

            cv2.imshow('facedetect', vis)
            if 0xFF & cv2.waitKey(5) == 27:
                break
        cv2.destroyAllWindows()
if __name__ == '__main__':
    aa = face_det()
    aa.To_start()
