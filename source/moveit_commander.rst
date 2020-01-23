Python用ユーザライブラリ（moveit_commander）の仕様
====================================================

クラス図、コンポーネント図
--------------------------

moveit_commanderは、boost::pythonを使って、C++のMoveGroupInterfaceを呼び出します。
その際に、MoveGroupInterfaceWrapperクラスを用います。

.. uml::

   planning_interface::MoveGroupInterface <|-- planning_interface::MoveGroupInterfaceWrapper
   planning_interface::MoveGroupInterfaceWrapper .. moveit_commander


MoveGroupInterfaceは、ROS通信（ROS Action）を使って、プランニング命令をROSのmove_groupサービスに送信します。

.. uml::

   [MoveGroupInterface] .. [move_group] : ROS Action


RobotCommander
---------------

.. doxygenclass:: moveit_commander::robot::RobotCommander
   :members:

MoveGroupCommander
-------------------

.. doxygenclass:: moveit_commander::move_group::MoveGroupCommander
   :members:

PlanningSceneInterface
------------------------

.. doxygenclass:: moveit_commander::planning_scene_interface::PlanningSceneInterface
   :members:
