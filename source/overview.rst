MoveIt!の全体構成
=======================================

MoveIt!の全体のソフトウェア構造を以下の図に示します。


.. image:: moveit.ros.org/assets/images/diagrams/moveit_pipeline.png

.. note::

   Above image is from http://moveit.ros.org/


ユーザ向けライブラリ
---------------------------------

MoveIt!は、ROS上に構築されていますが、ROSの知識を必要としないで利用できるユーザ向けライブラリが用意されています。

MoveIt Commanderは、Python用のユーザ向けライブラリで、ロボットの動作計画の基本APIをROSの知識なく利用できます。

MoveGroupInterfaceは、C++用のユーザ向けライブラリで、ロボットの動作計画の基本APIをROSの知識なく利用できます。


ROS通信
--------------------------------

MoveItの各内部モジュールはROS通信を行っており、MoveItを利用する際には、ROS通信を直接使うこともできます。

MoveItのユーザ向けAPIのほとんどはROS Actionの仕組みを使って呼び出します。


Planning Interface
------------------------------------------

MoveItには、CHOMP、OMPL、SBPLなどの各種プランニングアルゴリズムが実装されています。
それらプランニングアルゴリズムは、Planning Interfaceクラスを基底クラスとして実装されていますので、自由に切り替えて使うことができます。

開発者は、Planning Interfaceを継承した独自のクラスを実装することで、独自のアルゴリズムを使ってプランニングを実行することもできます。


Colllision Detection Interface
------------------------------------------

MoveItには、FCL、PCDなどの各種干渉計算アルゴリズムが実装されています。
それら干渉計算アルゴリズムは、Collision Detection Interfaceクラスを基底クラスとして実装されていますので、自由に切り替えて使うことができます。

開発者は、Collision Detection Interfaceを継承した独自のクラスを実装することで、独自のアルゴリズムを使ってプランニングを実行することもできます。


Planning Scene
------------------------------------------

MoveItでは、ロボット自身の形状はURDF形式のデータを用いますが、ロボット周辺の環境の形状を考慮したプランニングを行うこともできます。

Planning Sceneモジュールでは、ROS通信を用いて、ポイントクラウド情報を取り込んだり、各種プリミティブ形状を生成したりするインターフェースが用意されています。

これら環境情報は、MoveIt全体の制御を行うMove Groupモジュールを経由してCollision Detectionモジュールで利用されます。