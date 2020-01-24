move_groupサーバの仕様
====================================================

.. image:: moveit.ros.org/assets/images/diagrams/move_group.png

.. note::

   Above image is from http://moveit.ros.org/


プランニングの実行
---------------------

.. ros:autoaction:: moveit_msgs/MoveGroup
   :base: ../doxygen/
   :field-comment: up

.. ros:automessage:: moveit_msgs/MotionPlanRequest
   :base: ../doxygen/
   :field-comment: up

.. ros:automessage:: moveit_msgs/MoveItErrorCodes
   :base: ../doxygen/
   :field-comment: up

.. ros:automessage:: moveit_msgs/RobotTrajectory
   :base: ../doxygen/
   :field-comment: up

プランニング結果の実行
-----------------------

.. ros:autoaction:: moveit_msgs/ExecuteTrajectory
   :base: ../doxygen/
   :field-comment: up


高レベルのプランニング命令
---------------------------

.. ros:autoaction:: moveit_msgs/Pickup
   :base: ../doxygen/
   :field-comment: up

.. ros:autoaction:: moveit_msgs/Place
   :base: ../doxygen/
   :field-comment: up


MoveGroupCapability基底クラス
------------------------------

move_groupサーバは、各種サービスを実装する際に、MoveGroupCapabilityクラスを基底クラスとして利用します。

.. doxygenclass:: move_group::MoveGroupCapability
   :members:
