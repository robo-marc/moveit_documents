運動学計算アルゴリズム基底クラス（KinematicsBase）の仕様
===========================================================

-----------------
クラス図
-----------------

.. uml::

   KinematicsBase <|-- KDLKinematicsPlugin
   KinematicsBase <|-- IKFastKinematicsPlugin
   KinematicsBase <|-- LMAKinematicsPlugin

-----------------
基底クラス
-----------------

KinematicsBase
------------------------

.. doxygenclass:: kinematics::KinematicsBase
   :members:

-----------------------
KDL運動学計算プラグイン
-----------------------

KDLKinematicsPlugin
------------------------

.. doxygenclass:: kdl_kinematics_plugin::KDLKinematicsPlugin
   :members:

---------------------------
IKFast運動学計算プラグイン
---------------------------

IKFastKinematicsPlugin
------------------------

.. doxygenclass:: _NAMESPACE_::IKFastKinematicsPlugin
   :members:

-----------------------
LMA運動学計算プラグイン
-----------------------

LMAKinematicsPlugin
------------------------

.. doxygenclass:: lma_kinematics_plugin::LMAKinematicsPlugin
   :members:

