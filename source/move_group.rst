move_groupサーバの仕様
====================================================

.. image:: moveit.ros.org/assets/images/diagrams/move_group.png

.. note::

   Above image is from http://moveit.ros.org/


ROS Action一覧
---------------------

.. ros:autoaction:: moveit_msgs/MoveGroup
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoaction:: moveit_msgs/ExecuteTrajectory
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoaction:: moveit_msgs/Pickup
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoaction:: moveit_msgs/Place
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

ROSサービス一覧
----------------

.. ros:autoservice:: moveit_msgs/ApplyPlanningScene
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoservice:: moveit_msgs/ExecuteKnownTrajectory
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoservice:: moveit_msgs/GetCartesianPath
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoservice:: moveit_msgs/GetMotionPlan
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoservice:: moveit_msgs/GetPlannerParams
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoservice:: moveit_msgs/SetPlannerParams
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoservice:: moveit_msgs/GetPlanningScene
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoservice:: moveit_msgs/GetPositionFK
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoservice:: moveit_msgs/GetPositionIK
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoservice:: moveit_msgs/GetRobotStateFromWarehouse
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoservice:: moveit_msgs/GetStateValidity
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoservice:: moveit_msgs/GraspPlanning
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoservice:: moveit_msgs/SaveMap
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoservice:: moveit_msgs/LoadMap
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoservice:: moveit_msgs/QueryPlannerInterfaces
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoservice:: moveit_msgs/SaveRobotStateToWarehouse
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoservice:: moveit_msgs/DeleteRobotStateFromWarehouse
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoservice:: moveit_msgs/CheckIfRobotStateExistsInWarehouse
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoservice:: moveit_msgs/ListRobotStatesInWarehouse
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

.. ros:autoservice:: moveit_msgs/RenameRobotStateInWarehouse
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

MoveGroupCapability基底クラス
------------------------------

move_groupサーバは、各種サービスを実装する際に、MoveGroupCapabilityクラスを基底クラスとして利用します。

.. doxygenclass:: move_group::MoveGroupCapability
   :members:
