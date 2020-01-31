C++用ユーザライブラリ（MoveGroupInterface）の仕様
====================================================

コンポーネント図
-----------------

MoveGroupInterfaceは、ROS通信を使って、プランニング命令をROSのmove_groupサーバに送信します。

.. uml::

   [MoveGroupInterface] -right-> [move_group] : ROS通信


move_groupサーバで提供されている各サービスとROS通信の詳細については、 :doc:`move_group` を参照してください。

コードサンプル
--------------

本文書では、クラスの仕様のみを記述します。コードサンプルについては、以下の外部ドキュメント参照してください。

http://docs.ros.org/melodic/api/moveit_tutorials/html/doc/move_group_interface/move_group_interface_tutorial.html


MoveGroupInterface
--------------------

.. doxygenclass:: moveit::planning_interface::MoveGroupInterface
   :members:


PlanningSceneInterface
------------------------

.. doxygenclass:: moveit::planning_interface::PlanningSceneInterface
   :members:
