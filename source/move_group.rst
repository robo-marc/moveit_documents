move_groupサーバの仕様
====================================================

move_groupサーバの全体構成を以下に示します。

プランニングと実行などの長期のタスクを実行する際には、ROSアクション（図中赤線）が用いられます。

その他のサービスは、ROSサービス（図中青線）を用いて提供されます。

環境情報のアップデートは、一方向通信のROSトピック（図中緑線）が用いられます。

.. image:: moveit.ros.org/assets/images/diagrams/move_group.png

.. note::

   Above image is from http://moveit.ros.org/


---------------------
ROS Action一覧
---------------------

ROSアクションを各言語で呼び出すにはROSのactionlibを使います。
詳細な使い方は、以下の外部ドキュメントを参照してください。

http://wiki.ros.org/ja/actionlib

ROSアクション呼び出しは、内部的にはROSメッセージの送信（ゴール情報の送信）と受信（フィードバックメッセージと結果メッセージ）の双方向通信として実現されます。

.. uml::

   アプリケーションプログラム -> ROSアクション: ゴール情報メッセージ
   アプリケーションプログラム <- ROSアクション: フィードバックメッセージ
   ...ゴール状態が達成されるまでフィードバックを繰り返す...
   アプリケーションプログラム <- ROSアクション: 結果メッセージ

ROSアクションはactionlibを通して、実行途中でキャンセルすることもできます。以下はその場合のシーケンスです。

.. uml::

   アプリケーションプログラム -> ROSアクション: ゴール情報メッセージ
   アプリケーションプログラム <- ROSアクション: フィードバックメッセージ
   ...フィードバックを繰り返す...
   アプリケーションプログラム -> ROSアクション: キャンセルメッセージ
   アプリケーションプログラム <- ROSアクション: 結果メッセージ

MoveGroup
----------

軌跡の計算と実行を行うアクションです

.. ros:autoaction:: moveit_msgs/MoveGroup
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

ExecuteTrajectory
-------------------

軌跡の実行を行うアクションです

.. ros:autoaction:: moveit_msgs/ExecuteTrajectory
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

Pickup
----------

ピッキング動作を行う高レベルアクションです

.. ros:autoaction:: moveit_msgs/Pickup
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

Place
----------

プレース動作を行う高レベルアクションです

.. ros:autoaction:: moveit_msgs/Place
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

----------------
ROSサービス一覧
----------------

ROSサービスを各言語で呼び出す方法については、以下の外部ドキュメントを参照してください。

C++でシンプルなサービスとクライアントを書く
http://wiki.ros.org/ja/ROS/Tutorials/WritingServiceClient%28c%2B%2B%29

シンプルなサービスとクライアントを書く (Python)
http://wiki.ros.org/ja/ROS/Tutorials/WritingServiceClient%28python%29

ROSサービス呼び出しは、内部的にはROSメッセージの送信（リクエスト）と受信（応答）の双方向通信として実現されます。

.. uml::

   アプリケーションプログラム -> ROSサービス: リクエストメッセージ
   アプリケーションプログラム <- ROSサービス: 応答メッセージ

ROSサービスを呼び出すには以下に列挙するメッセージの型情報と共に、ROSトピック名が必要です。
利用したいROSサービスのトピック名を調べるには、rosserviceコマンドを使います。
例えば、「moveit_msgs/ApplyPlanningScene」サービスを提供するトピック名を調べるには、以下のコマンドを実行してください::

   rosservice find moveit_msgs/ApplyPlanningScene

move_groupサーバの各ROSサービスは後述するプラグインの仕組みを使って実装されています。
もし上記のコマンドでROSトピック名が発見されなかった場合は、利用したいサービスを提供するプラグインが有効になっているかどうかを確認してください。

ApplyPlanningScene
---------------------

planning sceneを適用するサービス

.. ros:autoservice:: moveit_msgs/ApplyPlanningScene
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

GetPlanningScene
---------------------

planning sceneを取得するサービス

.. ros:autoservice:: moveit_msgs/GetPlanningScene
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

ExecuteKnownTrajectory
-------------------------

軌跡を実行するサービス

.. ros:autoservice:: moveit_msgs/ExecuteKnownTrajectory
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

GetCartesianPath
-------------------

CP制御のためのプランニングを行うサービス

.. ros:autoservice:: moveit_msgs/GetCartesianPath
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

GetMotionPlan
---------------

動作計画を行うサービス

.. ros:autoservice:: moveit_msgs/GetMotionPlan
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

SetPlannerParams
------------------

プランナーのパラメータ設定を行うサービス

.. ros:autoservice:: moveit_msgs/SetPlannerParams
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

GetPlannerParams
------------------

プランナーのパラメータ取得を行うサービス

.. ros:autoservice:: moveit_msgs/GetPlannerParams
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

GetPositionFK
----------------

順運動学を計算するサービス

.. ros:autoservice:: moveit_msgs/GetPositionFK
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

GetPositionIK
----------------

逆運動学を計算するサービス

.. ros:autoservice:: moveit_msgs/GetPositionIK
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

GetStateValidity
------------------

ロボットの状態が与えた制約を満たしているかどうかを判定するサービス

.. ros:autoservice:: moveit_msgs/GetStateValidity
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

QueryPlannerInterfaces
------------------------

利用できるプランナー一覧を取得するサービス

.. ros:autoservice:: moveit_msgs/QueryPlannerInterfaces
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

GraspPlanning
------------------

把持計画を実行するサービス

.. ros:autoservice:: moveit_msgs/GraspPlanning
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

SaveMap
----------

干渉マップを保存するサービス

.. ros:autoservice:: moveit_msgs/SaveMap
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

LoadMap
----------

干渉マップをロードするサービス

.. ros:autoservice:: moveit_msgs/LoadMap
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

SaveRobotStateToWarehouse
--------------------------

ロボットの状態をデータベース（MongoDB）に保存するサービス

.. ros:autoservice:: moveit_msgs/SaveRobotStateToWarehouse
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

GetRobotStateFromWarehouse
-----------------------------

ロボットの状態をデータベース（MongoDB）からロードするサービス

.. ros:autoservice:: moveit_msgs/GetRobotStateFromWarehouse
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

DeleteRobotStateFromWarehouse
-------------------------------

ロボットの状態をデータベース（MongoDB）から削除するサービス

.. ros:autoservice:: moveit_msgs/DeleteRobotStateFromWarehouse
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

CheckIfRobotStateExistsInWarehouse
--------------------------------------

ロボットの状態がデータベース（MongoDB）に保存されているか確認するサービス

.. ros:autoservice:: moveit_msgs/CheckIfRobotStateExistsInWarehouse
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

ListRobotStatesInWarehouse
--------------------------

データベース（MongoDB）に保存されたロボットの状態を一覧するサービス

.. ros:autoservice:: moveit_msgs/ListRobotStatesInWarehouse
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

RenameRobotStateInWarehouse
------------------------------

データベース（MongoDB）に保存されたロボットの状態の名前を変更するサービス

.. ros:autoservice:: moveit_msgs/RenameRobotStateInWarehouse
   :base: ../doxygen/
   :field-comment: up
   :description: 0:0

MoveGroupCapability基底クラス
------------------------------

move_groupサーバは、各種サービスを実装する際に、MoveGroupCapabilityクラスを基底クラスとして利用します。

.. doxygenclass:: move_group::MoveGroupCapability
   :members:
