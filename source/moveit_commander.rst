Python用ユーザライブラリ（moveit_commander）の仕様
====================================================

クラス図
------------

moveit_commanderは、boost::pythonを使って、C++のMoveGroupInterfaceを呼び出します。
その際に、MoveGroupInterfaceWrapperクラスを用います。

.. uml::

   MoveGroupInterface <|-- MoveGroupInterfaceWrapper
   MoveGroupInterfaceWrapper .. moveit_commander

C++で実装されたMoveGroupInterfaceの詳細については、 :doc:`move_group_interface` を参照してください。


コンポーネント図
-------------------

MoveGroupInterfaceは、ROS通信を使って、プランニング命令をROSのmove_groupサーバに送信します。

.. uml::

   [moveit_commander(MoveGroupInterface)] -right-> [move_group] : ROS通信


move_groupサーバで提供されている各サービスとROS通信の詳細については、 :doc:`move_group` を参照してください。

RobotCommander
---------------

.. autoclass:: moveit_commander.RobotCommander
   :members:

.. autoclass:: moveit_commander.RobotCommander.Joint
   :members:

.. autoclass:: moveit_commander.RobotCommander.Link
   :members:

MoveGroupCommander
-------------------

.. autoclass:: moveit_commander.MoveGroupCommander
   :members:

   .. automethod:: __init__

PlanningSceneInterface
------------------------

.. autoclass:: moveit_commander.PlanningSceneInterface
   :members:

   .. automethod:: __init__
