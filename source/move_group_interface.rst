C++用ユーザライブラリ（planning_interface）の仕様
====================================================

コンポーネント図
-----------------

MoveGroupInterfaceは、ROS通信（ROS Action）を使って、プランニング命令をROSのmove_groupサービスに送信します。

.. uml::

   [MoveGroupInterface] .. [move_group] : ROS Action


MoveGroupInterface
--------------------

.. doxygenclass:: moveit::planning_interface::MoveGroupInterface
   :members:


PlanningSceneInterface
------------------------

.. doxygenclass:: moveit::planning_interface::PlanningSceneInterface
   :members:
