プランニングアルゴリズム基底クラス（PlannerManager）の仕様
===========================================================

-----------------
クラス図
-----------------

.. uml::

   planning_interface::PlannerManager <|-- chomp_interface::CHOMPPlannerManager
   planning_interface::PlannerManager <|-- ompl_interface::OMPLPlannerManager

.. uml::

   planning_interface::PlanningContext <|-- chomp_interface::CHOMPPlanningContext
   planning_interface::PlanningContext <|-- ompl_interface::OMPLPlanningContext

各プランニングアルゴリズムは、PlannerManagerおよびPlanningContextを基底クラスとして実装されており、自由に切り替えて利用できます。

既存のプランニングアルゴリズムを使うだけでなく、独自のアルゴリズムを実装することもできます。
MoveItでは、ROSのpluginlibの仕組みを使って独自アルゴリズムの既存システムへのプラグインを実現しています。
詳しい方法については、以下の外部ドキュメントを参照してください。

https://ros-planning.github.io/moveit_tutorials/doc/creating_moveit_plugins/plugin_tutorial.html

--------------
シーケンス図
--------------

アプリケーションプログラムは、pluginlibのClassLoaderを利用してPlannerManagerプラグインをロードします。

個々のプランニングは、PlannerManagerからPlanningContextを生成して実行されます。

.. uml::

   アプリケーションプログラム -> ClassLoader: インスタンス生成
   アプリケーションプログラム -> ClassLoader: createUnmanagedInstance()
   ClassLoader -> PlannerManager: インスタンス生成
   アプリケーションプログラム <- ClassLoader: PlannerManagerインスタンス
   アプリケーションプログラム -> PlannerManager: initialize()
   アプリケーションプログラム -> PlannerManager: getPlanningContext()
   PlannerManager -> PlanningContext: インスタンス生成
   アプリケーションプログラム <- PlannerManager: PlanningContextインスタンス
   アプリケーションプログラム -> PlanningContext: solve()
   アプリケーションプログラム <- PlanningContext: プランニング結果

--------------
コードサンプル
--------------

本文書では、クラスの仕様のみを記述します。コードサンプルについては、以下の外部ドキュメントを参照してください。

http://docs.ros.org/melodic/api/moveit_tutorials/html/doc/motion_planning_api/motion_planning_api_tutorial.html

-----------------
基底クラス
-----------------

PlannerManager
------------------------

.. doxygenclass:: planning_interface::PlannerManager
   :members:

PlanningContext
------------------------

.. doxygenclass:: planning_interface::PlanningContext
   :members:

.. -----------------
プラン実行クラス
-----------------

.. .. doxygenclass:: planning_pipeline::PlanningPipeline

-----------------
OMPLプランナー
-----------------

OMPLPlannerManager
------------------------

.. doxygenclass:: ompl_interface::OMPLPlannerManager
   :members:

ModelBasedPlanningContext
--------------------------

.. doxygenclass:: ompl_interface::ModelBasedPlanningContext
   :members:

-----------------
CHOMPプランナー
-----------------

CHOMPPlannerManager
------------------------

.. doxygenclass:: chomp_interface::CHOMPPlannerManager
   :members:

CHOMPPlanningContext
------------------------

.. doxygenclass:: chomp_interface::CHOMPPlanningContext
   :members:
