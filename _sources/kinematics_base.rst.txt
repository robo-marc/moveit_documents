運動学計算アルゴリズム基底クラス（KinematicsBase）の仕様
===========================================================

-----------------
クラス図
-----------------

.. uml::

   KinematicsBase <|-- KDLKinematicsPlugin
   KinematicsBase <|-- IKFastKinematicsPlugin
   KinematicsBase <|-- LMAKinematicsPlugin

各運動学計算アルゴリズムは、KinematicsBaseを基底クラスとして実装されており、自由に切り替えて利用できます。

既存の運動学計算アルゴリズムを使うだけでなく、独自のアルゴリズムを実装することもできます。
MoveItでは、ROSのpluginlibの仕組みを使って独自アルゴリズムの既存システムへのプラグインを実現しています。
詳しい方法については、以下の外部ドキュメントを参照してください。

https://ros-planning.github.io/moveit_tutorials/doc/creating_moveit_plugins/plugin_tutorial.html

一般に運動学の計算に解析解を使ったアルゴリズムの方が、数値解を使ったアルゴリズム（KDLKinematicsPluginなど）よりも高速で安定した解が得られます。

すでにロボットの解析解が得られている場合、それをプラグインの形で実装することを推奨します。

単純な形のロボットであれば、IKFastを利用すると、解析解を自動で計算することもできます。

解析解が得られていないロボットについても、数値解を使ったアルゴリズム（KDLKinematicsPluginなど）とURDF形式のロボット構造データを組み合わせることで、逆運動学が計算できます。

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

Orocos-KDLライブラリ（https://www.orocos.org/kdl）を使った逆運動学計算アルゴリズムを利用できます。

KDLKinematicsPlugin
------------------------

.. doxygenclass:: kdl_kinematics_plugin::KDLKinematicsPlugin
   :members:

---------------------------
IKFast運動学計算プラグイン
---------------------------

IKFastは、OpenRAVEに含まれる逆運動学の解析解を自動で求めてくれるC++コードジェネレータです。

詳しい使い方は、以下の外部ドキュメントを参照してください。

http://docs.ros.org/kinetic/api/moveit_tutorials/html/doc/ikfast/ikfast_tutorial.html

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

