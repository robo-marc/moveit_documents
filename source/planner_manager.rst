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

-----------------
OMPLプランナー
-----------------

OMPLPlannerManager
------------------------

.. doxygenclass:: ompl_interface::OMPLPlannerManager
   :members:

OMPLPlanningContext
------------------------

.. doxygenclass:: ompl_interface::OMPLPlanningContext
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
