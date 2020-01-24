import os
import glob

print('''ROSメッセージ一覧
=====================
''')

for f in sorted(glob.glob('doxygen/moveit_msgs/msg/*.msg')):
    print('''.. ros:automessage:: moveit_msgs/{0}
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0
'''.format(os.path.splitext(os.path.basename(f))[0]))